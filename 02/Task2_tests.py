import unittest
from unittest.mock import patch
from io import StringIO
from task2 import retry_deco

class TestRetryDeco(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_basic_case(self, mock_stdout):
        @retry_deco(3)
        def add(a, b):
            return a + b

        add(4, 2)
        output = mock_stdout.getvalue()
        self.assertIn('run "add" with positional args = (4, 2)', output)
        self.assertIn('result = 6', output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_key_value_args(self, mock_stdout):
        @retry_deco(3)
        def add(a, b):
            return a + b

        add(4, b=3)
        output = mock_stdout.getvalue()
        self.assertIn('run "add" with positional args = (4,)', output)
        self.assertIn("keyword kwargs = {'b': 3}", output)
        self.assertIn('result = 7', output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_exception_and_retry(self, mock_stdout):
        @retry_deco(3)
        def divide(a, b):
            if b == 0:
                raise ValueError("Division by zero")
            return a / b

        divide(4, 0)
        output = mock_stdout.getvalue()
        self.assertIn('run "divide" with positional args = (4, 0)', output)
        self.assertIn('exception = ValueError', output)
        self.assertIn('attempt = 3', output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_exception_not_in_retry_list(self, mock_stdout):
        @retry_deco(3, [ValueError])
        def divide(a, b):
            if b == 0:
                raise ValueError("Division by zero")
            return a / b

        divide(4, 0)
        output = mock_stdout.getvalue()
        self.assertIn('run "divide" with positional args = (4, 0)', output)
        self.assertIn('exception = ValueError', output)
        self.assertNotIn('attempt = 2', output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_no_exception(self, mock_stdout):
        @retry_deco(3)
        def add(a, b):
            return a + b

        add(2, 3)
        output = mock_stdout.getvalue()
        self.assertIn('run "add" with positional args = (2, 3)', output)
        self.assertIn('result = 5', output)


if __name__ == "__main__":
    unittest.main()
