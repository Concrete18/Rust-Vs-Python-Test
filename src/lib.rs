use pyo3::prelude::*;

fn count_to_num(num: usize) -> String {
    let mut n = 0;
    while n < num {
        n += 1
    }
    "sadadsa".to_string()
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn count(num: usize) -> PyResult<String> {
    Ok(count_to_num(num))
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_vs_python_test(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count, m)?)?;
    Ok(())
}
