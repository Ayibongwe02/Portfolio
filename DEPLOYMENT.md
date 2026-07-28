# GitHub Actions Setup Instructions

## Configure Docker Hub Secrets

To use this CI/CD pipeline, you must add your Docker Hub credentials as GitHub repository secrets:

1. Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add:
   - **Name:** `DOCKERHUB_USERNAME`  
     **Value:** `ayibongwe02`
   - **Name:** `DOCKERHUB_TOKEN`  
     **Value:** Your Docker Hub Personal Access Token (PAT)

3. Click **Add secret** for each

## Workflow Details

The workflow (`.github/workflows/build-and-push.yml`) runs on:
- **Push to `main` branch** → builds and pushes image with tags: `latest`, branch name, commit SHA
- **Pull requests to `main`** → builds image (does NOT push)

### Tags Applied:
- `latest` (only on default branch pushes)
- `main-<commit-sha>` (commit-specific tag)
- `<branch-name>` (branch name tag)

### Features:
- Multi-stage build caching for faster rebuilds
- Trivy vulnerability scanning with SARIF output
- Results uploaded to GitHub Security tab (Dependabot alerts)

## Local Push (Manual)

To manually push the image to Docker Hub:

```bash
docker tag portfolio:latest ayibongwe02/portfolio:latest
docker push ayibongwe02/portfolio:latest
```

## Verify Push

After committing to `main` and the workflow completes, verify at:  
https://hub.docker.com/r/ayibongwe02/portfolio

---

**Note:** Keep your Docker Hub PAT secure. Never commit it to version control. GitHub Secrets encrypt it automatically.
