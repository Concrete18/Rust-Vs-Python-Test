from time import perf_counter, sleep
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
        return end - start


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
        return end - start


class SpeedTest:

    python = Python()
    rust = Rust()

    @staticmethod
    def convert_times(elapsed_time):
        ms = round((elapsed_time) * 1000, 2)
        us = round((elapsed_time) * 1000 * 1000, 2)
        return ms, us

    @staticmethod
    def get_factor(slower_time, faster_time):
        """
        ph
        """
        return round(slower_time / faster_time, 1)

    def count(self):
        """
        Tests Python and Rust speed when counting to 1 Million.
        """
        # counting speed test
        NUM = 1_000_000
        print(f"\nTesting Count to {NUM:,}")

        # runs each test
        python_time = self.python.count(NUM)
        python_ms, python_us = self.convert_times(python_time)

        rust_time = self.rust.count(NUM, 10)
        rust_ms, rust_us = self.convert_times(rust_time)

        sleep(3)

        # prints times
        input("\nPress enter to show Python Time")
        print(f"Python Completion Time: {python_ms} ms")

        input("\nPress enter to show Rust Time")
        print(f"Rust Completion Time: {rust_ms} ms or {rust_us} μs")

        # get differenct
        input("\nPress enter to show Rust Speed Factor")
        factor = self.get_factor(python_time, rust_time)
        print(f"\nRust ran {factor} times faster then Python")

        input("\nPress Enter to Continue")

        print("\nRedoing Rust Speed Test")
        rust_time = self.rust.count(NUM)
        factor = self.get_factor(python_time, rust_time)
        print(f"Rust actually ran {factor} times faster then Python")


def main():
    print("\n\nRust VS Python Speed Test")
    test = SpeedTest()
    input("\nPress Enter to start first test")
    test.count()
    print("\n\n")


if __name__ == "__main__":
    main()
