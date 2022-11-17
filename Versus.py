from time import perf_counter, sleep
import rust_vs_python_test


class Python:
    def count(self, num):
        """
        Counts to `num` from 0.
        """
        # start timer
        start = perf_counter()
        # start count
        n = 0
        while n < num:
            n += 1
        # end timer
        end = perf_counter()
        return end - start


class Rust:
    def count(self, num, run_count=1):
        """
        Counts to `num` from 0 using the imported Rust Library.
        """
        # start timer
        start = perf_counter()
        # start count
        while run_count:
            rust_vs_python_test.count(num)
            run_count -= 1
        # end timer
        end = perf_counter()
        return end - start


class SpeedTest:

    python = Python()
    rust = Rust()

    @staticmethod
    def convert_time(elapsed_time):
        """
        Converts output from perf_counter into miliseconds and microseconds.
        """
        ms = round((elapsed_time) * 1000, 2)
        us = round((elapsed_time) * 1000 * 1000, 2)
        return ms, us

    @staticmethod
    def get_factor(low_num, high_num):
        """
        Gets the factor of a `low_num` and a `high_num`.
        """
        return round(low_num / high_num, 1)

    def run_test(self, num, rust_run_count=1):
        """
        Runs tests for Python and Rust. Rust runs a number of times equal to `rust_run_count`.
        """
        # runs each test
        python_time = self.python.count(num)
        python_ms, python_us = self.convert_time(python_time)

        rust_time = self.rust.count(num, rust_run_count)
        rust_ms, rust_us = self.convert_time(rust_time)
        return python_ms, python_us, rust_ms, rust_us

    def count(self):
        """
        Tests Python and Rust speed when counting to 1 Million.
        """
        # counting speed test
        NUM = 1_000_000
        print(f"\nTesting Count to {NUM:,}")

        rust_run_count = 10
        python_ms, python_us, rust_ms, rust_us = self.run_test(NUM, rust_run_count)
        # sets up return values
        sleep(3)

        # prints times
        input("\nPress enter to show Python Time")
        print(f"Python Completion Time: {python_ms} ms")

        input("\nPress enter to show Rust Time")
        print(f"Rust Completion Time: {rust_ms} ms or {rust_us} μs")

        # get differenct
        input("\nPress enter to show Rust Speed Factor")
        factor = self.get_factor(python_ms, rust_ms)
        print(f"\nRust ran {factor} times faster then Python")
        input("\nPress Enter to Continue")
        # retest code
        print(f"Rust actually ran {rust_run_count} times while Python only ran once.")

        input("\nPress enter to rerun Speed Tests.")
        python_ms, python_us, rust_ms, rust_us = self.run_test(NUM)
        print(f"Rust's Actual Completion Time: {rust_ms} ms or {rust_us} μs")
        factor = self.get_factor(python_ms, rust_ms)
        print(f"\nRust actually ran {factor} times faster then Python")


def main():
    print("\nRust VS Python Speed Test")
    test = SpeedTest()
    input("\nPress Enter to start test.")
    test.count()
    print("\n")


if __name__ == "__main__":
    main()
