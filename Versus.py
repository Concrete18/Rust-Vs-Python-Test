from time import perf_counter
import rust_vs_python_test


class Python:
    def count(self, num):
        print(f"\nPython count to {num:,}")
        # start timer
        start = perf_counter()
        # start count
        n = 0
        while n < num:
            n += 1
        # end timer
        end = perf_counter()
        elapsed = round((end - start) * 1000, 2)
        print(f"Completion Time: {elapsed} ms")
        return elapsed


class Rust:
    def count(self, num):
        print(f"\nRust count to {num:,}")
        # start timer
        start = perf_counter()
        # start count
        rust_vs_python_test.count(num)
        # end timer
        end = perf_counter()
        elapsed = round((end - start) * 1000, 2)
        print(f"Completion Time: {elapsed} ms")
        return elapsed


def test():
    python = Python()
    rust = Rust()

    num = 1_000_000_000_000

    python_time = python.count(num)
    rust_time = rust.count(num)

    diff = round(python_time / rust_time, 1)
    print(f"\nRust ran {diff} times faster then Python")


if __name__ == "__main__":
    test()
