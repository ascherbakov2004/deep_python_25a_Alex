import unittest
from unittest.mock import patch
from vk_1 import predict_message_mood


class TestPredictMessageMood(unittest.TestCase):
    @patch("vk_1.SomeModel.predict", return_value=0.9)
    def test_excellent_default_threshold(self, mock_predict):
        self.assertEqual(predict_message_mood("Текст"), "отл")

    @patch("vk_1.SomeModel.predict", return_value=0.1)
    def test_bad_default_threshold(self, mock_predict):
        self.assertEqual(predict_message_mood("Плохой текст"), "неуд")

    @patch("vk_1.SomeModel.predict", return_value=0.5)
    def test_normal_default_threshold(self, mock_predict):
        self.assertEqual(predict_message_mood("Нейтральный текст"), "норм")

    @patch("vk_1.SomeModel.predict", return_value=0.3)
    def test_borderline_bad(self, mock_predict):
        self.assertEqual(predict_message_mood("Граница 0.3"), "норм")

    @patch("vk_1.SomeModel.predict", return_value=0.8)
    def test_borderline_good(self, mock_predict):
        self.assertEqual(predict_message_mood("Граница 0.8"), "норм")

    @patch("vk_1.SomeModel.predict", return_value=0.79)
    def test_custom_thresholds_good(self, mock_predict):
        self.assertEqual(predict_message_mood("", good_thresholds=0.78), "отл")

    @patch("vk_1.SomeModel.predict", return_value=0.4)
    def test_custom_thresholds_normal(self, mock_predict):
        self.assertEqual(
            predict_message_mood("Сложный случай", bad_thresholds=0.35), "норм"
        )

    @patch("vk_1.SomeModel.predict", return_value=0.2)
    def test_custom_thresholds_bad(self, mock_predict):
        self.assertEqual(
            predict_message_mood("Очень плохо", bad_thresholds=0.25), "неуд"
        )

    @patch("vk_1.SomeModel.predict", return_value=0.31)
    def test_low_normal_range(self, mock_predict):
        self.assertEqual(predict_message_mood("чуть выше неуд"), "норм")

    @patch("vk_1.SomeModel.predict", return_value=0.79)
    def test_high_normal_range(self, mock_predict):
        self.assertEqual(predict_message_mood("чуть ниже отл"), "норм")


if __name__ == "__main__":
    unittest.main()
