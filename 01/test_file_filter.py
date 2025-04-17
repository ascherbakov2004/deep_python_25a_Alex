import unittest
import io
from unittest import mock
from file_filter_gen import file_filter_gen


class TestFilterGen(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_filter_words(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре
        восемь воды 
        """

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["день", "восемь"])
            self.assertEqual("яблоко сова день", next(gen_filter).strip())
            self.assertEqual("восемь воды", next(gen_filter).strip())

    def test_filter_file_words_upstring(self):
        mock_file_content = """
        яблоко сова день
        УтРо заря четыре
        восемь воды 
        """

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["утро"])
            self.assertEqual("УтРо заря четыре", next(gen_filter).strip())
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_arg_words_upstring(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре
        восемь воды 
        """

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["УтРо"])
            self.assertEqual("утро заря четыре", next(gen_filter).strip())
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_many_words_one_line(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре
        восемь воды 
        """
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["утро", "заря", "четыре"])
            self.assertEqual("утро заря четыре", next(gen_filter).strip())

    def test_filter_many_words_one_line_with_uppercase_lowercasw(self):
        mock_file_content = """
        яблоко сова день
        утро заря ЧЕТЫРЕ
        восемь воды 
        """
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["утро", "ЗАРЯ", "четыре"])
            self.assertEqual("утро заря ЧЕТЫРЕ", next(gen_filter).strip())

    def test_filter_with_none(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре
        None
        восемь воды 
        """
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["утро", "восемь"])
            self.assertEqual("утро заря четыре", next(gen_filter).strip())
            self.assertEqual("восемь воды", next(gen_filter).strip())

    def test_filter_with_empry_word_to_find(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре
        восемь воды 
        """
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["", "восемь"])
            self.assertEqual("восемь воды", next(gen_filter).strip())
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_empty_line_with_empry_word_to_find(self):
        mock_file_content = """
        яблоко сова день
        утро заря четыре\n\n
        
        восемь воды 
        """
        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
            create=True,
        ):
            gen_filter = file_filter_gen("file.txt", ["", "восемь"])
            self.assertEqual("восемь воды", next(gen_filter).strip())
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_empty_file(self):
        mock_file_content = ""

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            gen_filter = file_filter_gen("file.txt", ["день", "восемь"])
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_no_match(self):
        mock_file_content = """
        Яблоко сова день
        Утро заря четыре
        Восемь воды 
        """

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            gen_filter = file_filter_gen("file.txt", ["пять", "мороженое"])
            with self.assertRaises(StopIteration):
                next(gen_filter)

    def test_filter_with_empty_line(self):
        mock_file_content = "Hello\n\nWorld"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            gen_filter = file_filter_gen("file.txt", ["hello", "world"])
            self.assertEqual("Hello", next(gen_filter).strip())
            self.assertEqual("World", next(gen_filter).strip())

    def test_filter_with_special_characters(self):
        mock_file_content = "The price is $10\n100% complete!"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            gen_filter = file_filter_gen("file.txt", ["$10", "100%"])
            self.assertEqual("The price is $10", next(gen_filter).strip())
            self.assertEqual("100% complete!", next(gen_filter).strip())

    def test_filter_with_numbers(self):
        mock_file_content = "42 ответ\n3.14"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            gen_filter = file_filter_gen("file.txt", ["42", "3.14"])
            self.assertEqual("42 ответ", next(gen_filter).strip())
            self.assertEqual("3.14", next(gen_filter).strip())

    def test_filter_wrong_file_arg(self):
        with self.assertRaises(ValueError):
            gen_filter = file_filter_gen(1234, ["42", "3.14"])
            next(gen_filter)

    def test_filter_wrong_words_arg(self):
        mock_file_content = "42 ответ\n3.14"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            with self.assertRaises(ValueError):
                gen_filter = file_filter_gen("file.txt", 111)
                next(gen_filter)

    def test_filter_wrong_words_arg_list(self):
        mock_file_content = "42 ответ\n3.14"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            with self.assertRaises(ValueError):
                gen_filter = file_filter_gen("file.txt", [1, "2", "word"])
                next(gen_filter)

    def test_filter_wrong_words_arg_list_none(self):
        mock_file_content = "42 ответ\n3.14"

        with unittest.mock.patch(
            "builtins.open",
            new=unittest.mock.mock_open(read_data=mock_file_content),
        ):
            with self.assertRaises(ValueError):
                gen_filter = file_filter_gen("file.txt", [None, "None", "word"])
                next(gen_filter)

    def test_file_obj(self):
        data = "word1\nword2\nword3"
        with io.StringIO(data) as file:
            gen_filter = file_filter_gen(file, ["word2"])
            self.assertEqual("word2", next(gen_filter).strip())