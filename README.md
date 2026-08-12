# Python Learning Journey

A structured collection of Python programs, Jupyter notebooks, and small projects — from core language fundamentals to data analysis, visualization, and algorithm practice.

## Overview

This repository documents hands-on Python learning organized by topic. It includes chapter-wise exercises, data science notebooks (NumPy, Pandas, Matplotlib), DSA implementations, interview prep, and a mini expense tracker project.

## Repository Structure

```
Python/
├── Chapter 1/              # Basics: variables, types, input/output
├── Chapter 2/              # Strings, conditionals, functions
├── Chapter 3/              # Lists, tuples, and list methods
├── Chapter 4/              # Dictionaries and sets
├── Chapter 5/              # Loops, range, break/continue
├── Chapter 6/              # Functions and recursion
├── Chapter 7 File I/O/     # File handling and text operations
├── Numpy/                  # NumPy arrays, indexing, broadcasting
├── Pandas/                 # DataFrames, CSV handling, missing data
├── Matplotlib/             # Plotting and data visualization
├── DSA_Python/             # Data structures & algorithms
├── Expense_Tracker/        # CSV-based expense tracking CLI app
├── Interview(141Q)/        # Python interview preparation notebooks
├── IE&DS/                  # Industrial Engineering & Data Science labs
├── AI LAB/                 # AI lab exercises (e.g., BFS)
├── magic_square.py         # Magic square utility script
├── finonacci.py            # Fibonacci sequence (loop-based)
└── test.ipynb              # Miscellaneous notebook experiments
```

## Topics Covered

| Area | Contents |
|------|----------|
| **Python Fundamentals** | Variables, data types, control flow, functions, recursion |
| **Data Structures** | Lists, tuples, dictionaries, sets |
| **File I/O** | Reading, writing, searching, and replacing text in files |
| **NumPy** | Arrays, matrix operations, broadcasting, indexing & slicing |
| **Pandas** | Series, DataFrames, CSV operations, handling missing data |
| **Matplotlib** | Bar plots and visualization demos |
| **Projects** | Expense Tracker (add, view, summarize expenses via CSV) |
| **DSA** | Fibonacci and other algorithm exercises |
| **Interview Prep** | Python concept review notebook |

## Getting Started

### Prerequisites

- Python 3.8+
- [Jupyter Notebook](https://jupyter.org/) or [JupyterLab](https://jupyterlab.readthedocs.io/) (for `.ipynb` files)
- Recommended packages:

```bash
pip install numpy pandas matplotlib jupyter
```

### Running Python Scripts

```bash
# Example: run a chapter exercise
python "Chapter 1/FirstProgram.py"

# Example: run the expense tracker
cd Expense_Tracker
python expense_tracker.py
```

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Then open any `.ipynb` file from the relevant folder (e.g., `Pandas/`, `Numpy/`, `Matplotlib/`).

## Expense Tracker

A command-line expense manager that stores data in `expenses.csv`.

**Features:**
- Add new expenses with date, category, amount, and notes
- View all recorded expenses
- View category-wise spending summary

```bash
cd Expense_Tracker
python expense_tracker.py
```

## Sample Datasets

The `Pandas/` folder includes CSV files used in notebook exercises:

- `netflix_titles.csv` — Netflix titles dataset for data manipulation practice
- `industry_sic.csv`, `header_change.csv`, and other smaller sample files

## Notes

- Chapter folders follow a progressive learning path from beginner to intermediate Python.
- Some root-level files (`file.txt`, `numbers.txt`, etc.) are used as practice inputs for File I/O exercises.
- Jupyter checkpoint folders and Anaconda project metadata are excluded via `.gitignore`.

## License

This project is for educational purposes. Feel free to use and learn from it.

## Author

Pradeep — Python learner and developer.
