import time


def measure_time(func, *args, **kwargs):

    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    return end_time - start_time, result


import unittest


class TestMeasureTime(unittest.TestCase):
    def test_simple_function(self):
        def simple_function():
            time.sleep(0.1)  # Затримка на 0.1 секунди
            return "done"

        exec_time, result = measure_time(simple_function)
        self.assertAlmostEqual(exec_time, 0.1, delta=0.02)
        self.assertEqual(result, "done")

    def test_function_with_args(self):
        def sum_function(a, b):
            return a + b

        exec_time, result = measure_time(sum_function, 3, 5)
        self.assertTrue(exec_time >= 0)
        self.assertEqual(result, 8)

    def test_fast_function(self):
        def fast_function():
            return 42

        exec_time, result = measure_time(fast_function)
        self.assertTrue(exec_time >= 0)
        self.assertEqual(result, 42)


if __name__ == "__main__":
    unittest.main()
