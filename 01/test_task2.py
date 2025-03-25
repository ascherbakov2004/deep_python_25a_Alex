import unittest
from tempfile import NamedTemporaryFile
from vk_2 import gen


class TestGenFunction(unittest.TestCase):
    def write_temp_file(self, content):
        tmp = NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8")
        tmp.write(content)
        tmp.seek(0)
        return tmp

    def test_basic_match(self):
        tmp = self.write_temp_file("hello world\n")
        result = list(gen(tmp.name, ["hello"], []))
        self.assertEqual(result, ["hello world\n"])

    def test_with_stopword(self):
        tmp = self.write_temp_file("hello world\n")
        result = list(gen(tmp.name, ["hello"], ["world"]))
        self.assertEqual(result, [])

    def test_no_keywords(self):
        tmp = self.write_temp_file("just text here\n")
        result = list(gen(tmp.name, ["jUst"], ["just"]))
        self.assertEqual(result, [])

    def test_case_insensitive(self):
        tmp = self.write_temp_file("HeLLo WoRLD\n")
        result = list(gen(tmp.name, ["hello"], []))
        self.assertEqual(result, ["HeLLo WoRLD\n"])

    def test_stopword_case(self):
        tmp = self.write_temp_file("HeLLo WoRLD\n")
        result = list(gen(tmp.name, ["hello"], ["world"]))
        self.assertEqual(result, [])

    def test_multiple_lines(self):
        tmp = self.write_temp_file("yes match\nno stop\nmaybe nothing\n")
        result = list(gen(tmp.name, ["yes"], ["stop"]))
        self.assertEqual(result, ["yes match\n"])

    def test_numeric_keyword(self):
        tmp = self.write_temp_file("error 404\n")
        result = list(gen(tmp.name, ["404"], []))
        self.assertEqual(result, ["error 404\n"])

    def test_numeric_stop(self):
        tmp = self.write_temp_file("error 404\n")
        result = list(gen(tmp.name, ["error"], ["404"]))
        self.assertEqual(result, [])

    def test_substring_not_word(self):
        tmp = self.write_temp_file("helloworld\n")
        result = list(gen(tmp.name, ["hello"], []))
        self.assertEqual(result, [])

    def test_multiple_valid_lines(self):
        tmp = self.write_temp_file("one two\nthree four\nfive six\n")
        result = list(gen(tmp.name, ["one", "three", "five"], []))
        self.assertEqual(result, ["one two\n", "three four\n", "five six\n"])


if __name__ == "__main__":
    unittest.main()
