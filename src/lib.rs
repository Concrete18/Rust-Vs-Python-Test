use pyo3::prelude::*;

fn count_to_num(num: usize) {
    let mut n = 0;
    while n < num {
        n += 1
    }
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn count(num: usize) {
    count_to_num(num)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_vs_python_test(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count, m)?)?;
    Ok(())
}
