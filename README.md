# Personal Expense Tracker

A Python command-line app that logs expenses, tracks a daily spending limit,
shows spending totals by category, and lets you search by category or date.

## Run locally

Install Python 3, then open a terminal in the folder containing `expense.py`
and run:

```bash
python expense.py
```

The app uses Python's standard library and creates `list.csv` and `settings.txt`
in the working folder on first run.

## Try it

Set a daily limit of ₦1,000, log ₦250 for lunch under Food, and search for
the Food category. The app should show ₦750 remaining in your daily budget.
