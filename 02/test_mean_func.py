import unittest
import time
from unittest.mock import Mock, patch
from mean_func import mean


class TestMeanFunction(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_positive_n(self):
        try:
            decorator = mean(5)
        except Exception:
            self.fail("Исключение не должно возникать при положительном n")

    def test_zero_n(self):
        with self.assertRaises(RuntimeError):
            decorator = mean(0)

    def test_negative_n(self):
        with self.assertRaises(RuntimeError):
            decorator = mean(-5)

    def test_mean_calculation(self):
        @mean(3)
        def func():
            time.sleep(0.1)

        with patch("builtins.print") as mock_print:
            func()
            func()
            func()
            mock_print.assert_called_with(
                "Время выполнения последних 3 итераций функции func : 0.100"
            )

    def test_function_execution(self):
        with patch("builtins.print") as mock_print:

            @mean(1)
            def func():
                nonlocal executed
                executed = True

            executed = False
            func()
            self.assertTrue(executed, "Функция не была выполнена")

    def test_no_print(self):
        @mean(3)
        def func():
            pass

        with patch("builtins.print") as mock_print:
            func()
            func()
            mock_print.assert_not_called()

    def test_mean_differnt_time(self):
        @mean(5)
        def func(work_time):
            time.sleep(work_time)

        with patch("builtins.print") as mock_print:
            for work_time in range(5):
                func(work_time / 10)
            # 0.200 так как (0 + 0.1 + 0.2 + 0.3 + 0.4)/5 = 0.2
            mock_print.assert_called_with(
                "Время выполнения последних 5 итераций функции func : 0.200"
            )

    def test_mean_same_time_with_interval(self):
        @mean(3)
        def func(work_time):
            time.sleep(work_time)

        with patch("builtins.print") as mock_print:
            for _ in range(3):
                func(0.05)
                time.sleep(0.02)

            mock_print.assert_called_with(
                "Время выполнения последних 3 итераций функции func : 0.050"
            )

    def test_mean_many_iterations(self):
        @mean(500)
        def func(work_time):
            time.sleep(work_time)

        with patch("builtins.print") as mock_print:
            for _ in range(1000):
                func(0.001)

            self.assertEqual(501, mock_print.call_count)

            mock_print.assert_called_with(
                "Время выполнения последних 500 итераций функции func : 0.001"
            )

    def test_mean_many_func(self):
        @mean(1)
        def func1():
            time.sleep(0.1)

        @mean(3)
        def func2():
            time.sleep(0.2)

        with patch("builtins.print") as mock_print:
            func2()
            func1()
            func2()
            mock_print.assert_called_with(
                "Время выполнения последних 1 итераций функции func1 : 0.100"
            )

    @patch("builtins.print")
    def test_return_result(self, mock_print):
        @mean(3)
        def sum(a, b):
            return a + b

        result = sum(2, 3)
        self.assertEqual(result, 5)

    # Дополнительные тесты

    def test_zero_iterations(self):
        @mean(1)
        def func():
            time.sleep(0.05)
        
        # Протестируем с нулевым временем
        with patch("builtins.print") as mock_print:
            func()
            mock_print.assert_called_with(
                "Время выполнения последних 1 итераций функции func : 0.050"
            )

    def test_large_n_value(self):
        @mean(1000)
        def func():
            time.sleep(0.001)

        with patch("builtins.print") as mock_print:
            for _ in range(2000):
                func()
            # Время выполнения последних 1000 итераций должно быть близко к 0.001
            mock_print.assert_called_with(
                "Время выполнения последних 1000 итераций функции func : 0.001"
            )

    def test_function_with_arguments(self):
        @mean(3)
        def add(a, b):
            time.sleep(0.1)
            return a + b
        
        with patch("builtins.print") as mock_print:
            result = add(2, 3)
            mock_print.assert_called_with(
                "Время выполнения последних 3 итераций функции add : 0.100"
            )
            self.assertEqual(result, 5)

    def test_no_time_mean(self):
        @mean(2)
        def func():
            return 42  # нет времени на выполнение

        with patch("builtins.print") as mock_print:
            result = func()
            mock_print.assert_called_with(
                "Время выполнения последних 2 итераций функции func : 0.000"
            )
            self.assertEqual(result, 42)

    def test_decorator_works_with_multiple_functions(self):
        @mean(2)
        def func1():
            time.sleep(0.2)
            return "func1 result"

        @mean(2)
        def func2():
            time.sleep(0.1)
            return "func2 result"

        with patch("builtins.print") as mock_print:
            result1 = func1()
            result2 = func2()
            mock_print.assert_called_with(
                "Время выполнения последних 2 итераций функции func2 : 0.100"
            )
            self.assertEqual(result1, "func1 result")
            self.assertEqual(result2, "func2 result")

    def test_multiple_func_same_time(self):
        @mean(2)
        def func1():
            time.sleep(0.05)

        @mean(2)
        def func2():
            time.sleep(0.05)

        with patch("builtins.print") as mock_print:
            func1()
            func2()
            mock_print.assert_called_with(
                "Время выполнения последних 2 итераций функции func2 : 0.050"
            )

