# Rust VS Python

## Why?

I made this for a workshop that demonstrates the speed differences of Rust and shows how that can allow you to speed up Python using Maturin to import Rust code into python projects.

## How To

This will show you 2 ways to learn how to use Rust in Python.

### Initial Setup

Start with the following instructions and then choose the next step depending on if you want to run this project or start your own.

- Install [Rust](https://www.rust-lang.org/) and [Python](https://www.python.org/) (if not installed)
- Create Python Virtual Environment using `python -m venv .env`
- Run `pip install maturin` [Maturin](https://github.com/PyO3/maturin)

#### Maturin Setup for this project

Use this these instructions to use the code within this project.

- Run `Maturin develop`
- Run Python3 Versus.py

#### Maturin Setup for a new project

Use these instructions to create your own Python project with Rust functions.

- Write Python code that uses
- Run `Maturin New`
- Write Rust code
- Run `Maturin develop`
- Import new Rust module into Python
