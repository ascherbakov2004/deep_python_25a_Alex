import unittest
from process_json import process_json
from unittest.mock import Mock


class TestProcessJson(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_find_two_words_one_key(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1 word2", "key2": "word2 word3"}'
        process_json(
            json_str,
            required_keys=["key1"],
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertEqual(
            [(("key1", "word1"),), (("key1", "word2"),)], keyw_callb_mock.call_args_list
        )

    def test_find_words_multiple_keys(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1 word2", "key2": "word2 word3 word4"}'
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertEqual(
            [(("key1", "word1"),), (("key1", "word2"),), (("key2", "word2"),)],
            keyw_callb_mock.call_args_list,
        )

    def test_found_two_equal_words_in_one_key(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1 word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1"],
            tokens=["word1"],
            callback=keyw_callb_mock,
        )
        self.assertEqual(
            [
                (("key1", "word1"),),
                (("key1", "word1"),),
            ],
            keyw_callb_mock.call_args_list,
        )

    def test_register_keywords_lowercase(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "WORD1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1"],
            tokens=["word1"],
            callback=keyw_callb_mock,
        )
        self.assertEqual(
            [
                (("key1", "WORD1"),),
            ],
            keyw_callb_mock.call_args_list,
        )

    def test_register_keywords_uppercase(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1"],
            tokens=["WORD1"],
            callback=keyw_callb_mock,
        )
        self.assertEqual(
            [
                (("key1", "word1"),),
            ],
            keyw_callb_mock.call_args_list,
        )

    def test_empty_json_no_args(self):
        key_callb_mock = Mock(return_value=None)
        process_json("{}", callback=key_callb_mock)
        self.assertFalse(key_callb_mock.called)

    def test_empty_json_with_args(self):
        keyw_callb_mock = Mock(return_value=None)
        process_json(
            "{}",
            required_keys=["key1"],
            tokens=["Word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_no_fields_found(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"field1": "value1 word1", "field2": "value2 word2"}'
        process_json(
            json_str,
            required_keys=["key1"],
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_no_keywords_found(self):
        keyw_callb_mock = Mock()
        json_str = '{"key1": "value1 word1", "key2": "value2 word2"}'
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            tokens=["word3"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_empty_required_fields(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=[],
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_no_required_fields(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_empty_keywords(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            tokens=[],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_no_keywords(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_json_is_not_str(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = 11
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_fields_is_not_str_list(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=0,  
            tokens=["word1", "word2"],
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)

    def test_keywords_is_not_str_list(self):
        keyw_callb_mock = Mock(return_value=None)
        json_str = '{"key1": "word1", "key2": "word2"}'
        process_json(
            json_str,
            required_keys=["key1", "key2"],
            tokens=0,  
            callback=keyw_callb_mock,
        )
        self.assertFalse(keyw_callb_mock.called)
