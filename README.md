# Rust VS Python

## Why?

I made this for a workshop that demonstrates the speed differences of Rust and shows how that can allow you to speed up Python using Maturin to import Rust code into python projects.

[Google Slides](https://docs.google.com/presentation/d/1AkYj3ZzVTnYjSmr6Qgjrki1yd8NvC36VB3p5_TzAwjQ/edit?usp=sharing)

[Workshop Video](https://us02web.zoom.us/rec/play/-c5LzNfo-He876oEdNeg7QYhXcnv8j5UbXfw7OPrqTP46fOKmixVsjr_WhnMJ6WzCGILZECDkF5hCFGs.5o3ht-gBWdYFxuDI?continueMode=true&_x_zm_rtaid=A7WXYVCgQb6ULRviuVMP8w.1669143615711.d74d239d70cc52cd364665c1428f1db9&_x_zm_rhtaid=956)
| Video Code: `.^aW4igv`

## How To

This will show you two ways to learn how to use Rust in Python.

### Initial Setup

Start with the following instructions and then choose the next step depending on if you want to run this project or start your own.

- Install [Rust](https://www.rust-lang.org/) and [Python](https://www.python.org/) (I used 3.8.6) (if not installed)
- Create Python Virtual Environment using `python -m venv .env`
- Activate your venv
- Run `pip install maturin`

Choose only one of the next two steps.

For more detailed instructions go to [Maturin](https://github.com/PyO3/maturin).

#### Maturin Setup for this Rust VS Python Demonstration

Use this these instructions to use the code within this project.

- Run `Maturin develop`
- Run Python3 Versus.py

#### Maturin Setup for a new project of your own

Use these instructions to create your own Python project with Rust functions.

- Write Python code that uses
- Run `Maturin New`
- Write Rust code
- Run `Maturin develop`
- Import new Rust module into Python
