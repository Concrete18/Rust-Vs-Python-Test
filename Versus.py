from time import perf_counter
import rust_vs_python_test


class Python:
    def count(self, num):
        # start timer
        start = perf_counter()
        # start count
        n = 0
        while n < num:
            n += 1
        # end timer
        end = perf_counter()
        elapsed = round((end - start) * 1000, 2)
        print(f"Python Completion Time: {elapsed} ms")
        return elapsed


class Rust:
    def count(self, num, run_count=1):
        # start timer
        start = perf_counter()
        # start count
        while run_count:
            rust_vs_python_test.count(num)
            run_count -= 1
        # end timer
        end = perf_counter()
        ms = round((end - start) * 1000, 2)
        us = round((end - start) * 1000 * 1000, 2)
        print(f"Rust Completion Time: {ms} ms or {us} μs")
        return ms


class SpeedTest:

    python = Python()
    rust = Rust()

    def count(self):
        # counting speed test
        NUM = 1_000_000
        print(f"\nTesting Count to {NUM:,}")

        print("\nStarting Python")
        python_time = self.python.count(NUM)
        print("\nStarting Rust")
        rust_time = self.rust.count(NUM, 15)

        diff = round(python_time / rust_time, 1)
        print(f"\nRust ran {diff} times faster then Python")

        input("\nPress Enter to Start Next Speed Test")

        print("\nRedoing Rust Speed Test")

        rust_time = self.rust.count(NUM)
        diff = round(python_time / rust_time, 1)
        print(f"\nRust actually ran {diff} times faster then Python")


def main():
    print("Rust VS Python Speed Test")
    input("\nPress Enter to start first test")
    test = SpeedTest()
    test.count()


if __name__ == "__main__":
    main()
