import unittest
from unittest import mock

from predict_mood import SomeModel, predict_message_mood


class TestPredictMessage(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_predict_otl(self) -> None:
        model = SomeModel()
        with mock.patch("predict_mood.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.9
            self.assertEqual("отл", predict_message_mood("Чапаев", model))

    @mock.patch("predict_mood.SomeModel.predict")
    def test_predict_neud(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.2
        self.assertEqual("неуд", predict_message_mood("Чапаев", model))

    @mock.patch("predict_mood.SomeModel.predict")
    def test_predict_norm(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.5
        self.assertEqual("норм", predict_message_mood("Вулкан", model))

    @mock.patch("predict_mood.SomeModel.predict")
    def test_predict_neud_with_changed_thresholds(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.4
        self.assertEqual(
            "неуд",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )
        mock_predict.return_value = 0.6
        self.assertEqual(
            "норм",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )
        mock_predict.return_value = 0.9
        self.assertEqual(
            "отл",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_predict_bad_treshold(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.2
        self.assertEqual(
            "норм", predict_message_mood("Вулкан", model, bad_thresholds=0.2)
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_predict_good_treshold(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.9
        self.assertEqual(
            "норм", predict_message_mood("Вулкан", model, good_thresholds=0.9)
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_wrong_thresholds_order(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.5
        self.assertEqual(
            None,
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.8, good_thresholds=0.7
            ),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_wrong_thresholds_strings(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.0
        self.assertEqual(
            None,
            predict_message_mood(
                "Вулкан", model, bad_thresholds="aaa", good_thresholds="bbb"
            ),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_wrong_message_int(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.0
        self.assertEqual(
            None,
            predict_message_mood(1234, model),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_wrong_message_none(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.0
        self.assertEqual(
            None,
            predict_message_mood(None, model),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_wrong_message_empty(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.0
        self.assertEqual(
            None,
            predict_message_mood(None, model),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_on_thresholds(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.4
        self.assertEqual(
            "норм",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.4, good_thresholds=0.7
            ),
        )
        mock_predict.return_value = 0.7
        self.assertEqual(
            "норм",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.4, good_thresholds=0.7
            ),
        )

    @mock.patch("predict_mood.SomeModel.predict")
    def test_near_treshold(self, mock_predict):
        model = SomeModel()
        mock_predict.return_value = 0.499999999
        self.assertEqual(
            "неуд",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )
        mock_predict.return_value = 0.500000001
        self.assertEqual(
            "норм",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )
        mock_predict.return_value = 0.7000000001
        self.assertEqual(
            "отл",
            predict_message_mood(
                "Вулкан", model, bad_thresholds=0.5, good_thresholds=0.7
            ),
        )