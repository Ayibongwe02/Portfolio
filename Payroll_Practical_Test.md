# Python Practical Test: Employee Payroll Program

**Time allowed:** 45–60 minutes
**Instructions:** Below are two files from an employee payroll program: `manage.py` and `main.py`. Several lines have been removed and replaced with numbered blanks, e.g. `# ___[1]___`. Read the surrounding code and comments carefully, then write the missing line(s) for each blank in the answer sheet at the end (or directly in the code if submitting the `.py` files).

Do not change any code that is already provided. Each blank is worth marks as indicated.

---

## Part A — `manage.py` (20 marks)

This file contains a function that calculates an employee's pay, including overtime at 1.5x the normal rate for any hours over 40.

```python
def calculate_pay(hours_worked, pay_rate):
    # ___[1]___                                   (3 marks)
    # Write the condition that checks if the employee worked overtime
    # (i.e. more than 40 hours)

        overtime_hours = ___[2]___                 (2 marks)
        # Calculate how many hours were overtime

        overtime_pay = ___[3]___                   (3 marks)
        # Overtime hours are paid at 1.5x the normal pay_rate

        regular_pay = ___[4]___                     (2 marks)
        # The first 40 hours are paid at the normal rate

        gross_pay = ___[5]___                        (2 marks)
        # Total pay = regular pay + overtime pay

    else:
        gross_pay = hours_worked * pay_rate
        regular_pay = gross_pay
        overtime_hours = 0
        overtime_pay = 0

    return {
        "regular_pay": ___[6]___,                    (1 mark)
        "overtime_hours": ___[7]___,                 (1 mark)
        "overtime_pay": ___[8]___,                   (1 mark)
        "gross_pay": ___[9]___,                      (1 mark)
    }
```

**[10] (4 marks)** In your own words, explain why `regular_pay` is set to `40 * pay_rate` in the overtime branch instead of `hours_worked * pay_rate`.

---

## Part B — `main.py` (30 marks)

This file collects employee details from the user, calls `calculate_pay`, displays the results, and saves them to a text file.

### B1 — Setup and Input (8 marks)

```python
___[11]___                                          (2 marks)
# Import the calculate_pay function from the manage module

name_employee = input("Enter employee name: ")
hours_worked = ___[12]___                           (3 marks)
# Get the hours worked from the user as a WHOLE NUMBER

pay_rate = ___[13]___                                (3 marks)
# Get the pay rate from the user as a DECIMAL NUMBER
```

### B2 — Using the function's return value (6 marks)

```python
result = calculate_pay(hours_worked, pay_rate)
regular_pay    = ___[14]___                          (2 marks)
overtime_hours = result["overtime_hours"]
overtime_pay   = ___[15]___                          (2 marks)
gross_pay      = result["gross_pay"]                 (given as example — 0 marks)
```

**[16] (2 marks)** What data type is stored in the variable `result`? How do you know, just by looking at how `regular_pay` is extracted from it?

### B3 — Writing to a file (8 marks)

```python
with open("employee_records.txt", ___[17]___) as file:   (3 marks)
    # We want to ADD each new employee to the bottom of the file
    # WITHOUT erasing employees already saved. Which file mode goes here?

    file.write("=" * 40 + "\n")
    file.write(f"Employee Name:  {name_employee}\n")
    file.write(f"Gross Pay:      R{gross_pay:.2f}\n")
```

**[18] (2 marks)** What would happen to the file's existing contents if `"w"` was used instead of the mode you chose above?

**[19] (3 marks)** Why do we use a `with` statement to open the file instead of just writing `file = open("employee_records.txt", "a")`?

### B4 — Reading the file back (8 marks)

```python
# Read the WHOLE file at once into a single string
with open("employee_records.txt", "r") as file:
    all_content = ___[20]___                          (2 marks)
    print(all_content)

# Read the file ONE LINE AT A TIME (better for large files)
with open("employee_records.txt", "r") as file:
    ___[21]___                                         (3 marks)
    # Write a for-loop header that goes through the file line by line

        clean_line = ___[22]___                        (2 marks)
        # Remove the trailing newline character from each line
        print(clean_line)

# Read the file into a LIST of lines
with open("employee_records.txt", "r") as file:
    lines = ___[23]___                                 (1 mark)
```

---

## Part C — Short Answer (10 marks)

**[24] (3 marks)** If an employee worked exactly 40 hours, what will `overtime_hours` and `overtime_pay` equal, based on the code in Part A? Explain why.

**[25] (3 marks)** List the four file modes commonly used with Python's `open()` function and briefly describe what each one does. (`"r"` and `"a"` have already appeared in this program — name two more.)

**[26] (4 marks)** The program currently trusts that the user will always type a valid whole number for `hours_worked`. What could go wrong if the user typed `"forty"` instead of `40`? Suggest one way the code could be made more robust against this.

---

**Total: 60 marks**
