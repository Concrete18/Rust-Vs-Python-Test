from time import perf_counter


def benchmark(func):
    """
    Prints `func` name and its benchmark time.
    """

    def wrapped(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter()
        elapsed = round(end - start, 2)
        print(f"{func.__name__} Completion Time: {elapsed}")
        return value

    return wrapped


class Python:
    @benchmark
    def count(self):
        n = 0
        while n < 1_000_000_000_000:
            n += 1


class Rust:
    @benchmark
    def count():
        n = 0
        while n < 1_000_000_000_000:
            n += 1


python = Python()
python.count()
