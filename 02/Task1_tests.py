import unittest
from unittest.mock import patch
from Task1 import process_json

class TestProcessJson(unittest.TestCase):

    @patch("builtins.print")
    def test_basic_case(self, mock_print):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = ["key1", "KEY2"]
        tokens = ["WORD1", "word2"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_any_call('key1', 'Word1')
        mock_print.assert_any_call('key1', 'word2')

    @patch("builtins.print")
    def test_key_not_found(self, mock_print):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = ["key3"]
        tokens = ["WORD1", "word2"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_token_not_found(self, mock_print):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = ["key1"]
        tokens = ["WORD3"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_token_case_insensitive(self, mock_print):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = ["key1"]
        tokens = ["word1", "WORD2"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_any_call('key1', 'Word1')
        mock_print.assert_any_call('key1', 'word2')

    @patch("builtins.print")
    def test_empty_json(self, mock_print):
        json_str = '{}'
        required_keys = ["key1"]
        tokens = ["WORD1"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_no_keys_to_process(self, mock_print):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = None
        tokens = ["WORD1"]
        process_json(json_str, required_keys, tokens, callback=mock_print)
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
