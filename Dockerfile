# Build stage
FROM python:3.12-slim as builder

WORKDIR /build

# Install dependencies in a virtual environment
COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Switch to non-root user
USER appuser

EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/').read()"

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "sync", "--max-requests", "1000", "app:app"]
