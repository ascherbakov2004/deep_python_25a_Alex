import unittest
from descriptors import CardReader, TransactionAmount, OperationName


class TestDescriptors(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_Cardreader_set_and_get(self):
        class Operation:
            card_num = CardReader()

        oper = Operation()
        oper.card_num = "1234567887654321"
        self.assertTrue(hasattr(oper, "card_num"))
        ans = "1234 5678 8765 4321"
        self.assertEqual(ans, oper.card_num)

    def test_Cardreader_not_numbers(self):
        class Operation:
            card_num = CardReader()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.card_num = "y23456788765432e"

    def test_Cardreader_less_16(self):
        class Operation:
            card_num = CardReader()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.card_num = "12345677654321"

    def test_Cardreader_dict_name(self):
        class Operation:
            card_num = CardReader()

        oper = Operation()
        oper.card_num = "1234567887654321"
        self.assertTrue("cardreader_descr_card_num" in oper.__dict__)

    def test_TransactionAmount_set_and_get(self):
        class Operation:
            transact_amount = TransactionAmount()

        oper = Operation()
        oper.transact_amount = 1000
        self.assertTrue(hasattr(oper, "transact_amount"))
        self.assertEqual(1000, oper.transact_amount)

    def test_TransactionAmount_not_num(self):
        class Operation:
            transact_amount = TransactionAmount()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.transact_amount = "str"

    def test_OperationName_set_and_get(self):
        class Operation:
            oper_name = OperationName()

        oper = Operation()
        oper.oper_name = "addition"
        self.assertTrue(hasattr(oper, "oper_name"))
        self.assertEqual("addition", oper.oper_name)

    def test_OperationName_not_str(self):
        class Operation:
            oper_name = OperationName()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.oper_name = []

    def test_all_decr(self):
        class Operation:
            oper_name = OperationName()
            transact_amount = TransactionAmount()
            card_num = CardReader()

            def __init__(self, oper_name, transact_amount, card_num):
                self.oper_name = oper_name
                self.transact_amount = transact_amount
                self.card_num = card_num

        oper = Operation("addition", 1000, "1234567887654321")

        self.assertTrue(hasattr(oper, "oper_name"))
        self.assertEqual("addition", oper.oper_name)

        self.assertTrue(hasattr(oper, "transact_amount"))
        self.assertEqual(1000, oper.transact_amount)

        self.assertTrue(hasattr(oper, "card_num"))
        ans = "1234 5678 8765 4321"
        self.assertEqual(ans, oper.card_num)

    def test_two_cls_inst_oper_name(self):
        class Operation:
            oper_name = OperationName()

        oper1 = Operation()
        oper2 = Operation()
        oper1.oper_name = "salary"
        oper2.oper_name = "tax"

        self.assertTrue(hasattr(oper1, "oper_name"))
        self.assertEqual("salary", oper1.oper_name)

        self.assertTrue(hasattr(oper2, "oper_name"))
        self.assertEqual("tax", oper2.oper_name)

    def test_two_cls_inst_transact_amount(self):
        class Operation:
            transact_amount = TransactionAmount()

        oper1 = Operation()
        oper2 = Operation()
        oper1.transact_amount = 100
        oper2.transact_amount = -100

        self.assertTrue(hasattr(oper1, "transact_amount"))
        self.assertEqual(100, oper1.transact_amount)

        self.assertTrue(hasattr(oper2, "transact_amount"))
        self.assertEqual(-100, oper2.transact_amount)

    def test_two_cls_inst_card_reader(self):
        class Operation:
            card_num = CardReader()

        oper1 = Operation()
        oper2 = Operation()
        oper1.card_num = "1234567887654321"
        oper2.card_num = "8765432112345678"

        self.assertTrue(hasattr(oper1, "card_num"))
        ans = "1234 5678 8765 4321"
        self.assertEqual(ans, oper1.card_num)

        ans = "8765 4321 1234 5678"
        self.assertTrue(hasattr(oper2, "card_num"))
        self.assertEqual(ans, oper2.card_num)

    def test_two_oper_name_in_cls(self):
        class Operation:
            oper_name1 = OperationName()
            oper_name2 = OperationName()

        oper = Operation()

        oper.oper_name1 = "salary"
        oper.oper_name2 = "tax"

        self.assertTrue(hasattr(oper, "oper_name1"))
        self.assertEqual("salary", oper.oper_name1)

        self.assertTrue(hasattr(oper, "oper_name2"))
        self.assertEqual("tax", oper.oper_name2)

    def test_two_transact_amount_in_cls(self):
        class Operation:
            transact_amount1 = TransactionAmount()
            transact_amount2 = TransactionAmount()

        oper = Operation()
        oper.transact_amount1 = 100
        oper.transact_amount2 = -100

        self.assertTrue(hasattr(oper, "transact_amount1"))
        self.assertEqual(100, oper.transact_amount1)

        self.assertTrue(hasattr(oper, "transact_amount2"))
        self.assertEqual(-100, oper.transact_amount2)

    def test_two_card_reader_in_cls(self):
        class Operation:
            card_num1 = CardReader()
            card_num2 = CardReader()

        oper = Operation()
        oper.card_num1 = "1234567887654321"
        oper.card_num2 = "8765432112345678"

        self.assertTrue(hasattr(oper, "card_num1"))
        ans = "1234 5678 8765 4321"
        self.assertEqual(ans, oper.card_num1)

        ans = "8765 4321 1234 5678"
        self.assertTrue(hasattr(oper, "card_num2"))
        self.assertEqual(ans, oper.card_num2)

    def test_no_inst_oper_name(self):
        try:
            self.assertEqual(None, OperationName.__set__(OperationName, None, "str"))
        except Exception as e:
            self.fail(f"Test raised an exception: {str(e)}")

    def test_no_inst_transact_amount(self):
        try:
            self.assertEqual(
                None, TransactionAmount.__set__(TransactionAmount, None, 10)
            )
        except Exception as e:
            self.fail(f"Test raised an exception: {str(e)}")

    def test_no_inst_card_reader(self):
        try:
            self.assertEqual(
                None, CardReader.__set__(CardReader, None, "1234123412341234")
            )
        except Exception as e:
            self.fail(f"Test raised an exception: {str(e)}")

    def test_oper_name_non_valid(self):
        class Operation:
            send = OperationName()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.send = None

    def test_transact_amount_non_valid(self):
        class Operation:
            amount = TransactionAmount()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.amount = None

    def test_card_reader_non_valid(self):
        class Operation:
            card = CardReader()

        oper = Operation()
        with self.assertRaises(ValueError):
            oper.card = None

    def test_oper_name_change_value_non_valid(self):
        class Operation:
            send = OperationName()

        oper = Operation()

        oper.oper_name = "addition"

        with self.assertRaises(ValueError):
            oper.send = 100

        self.assertTrue(hasattr(oper, "oper_name"))
        self.assertEqual("addition", oper.oper_name)

    def test_transact_amount_non_valid(self):
        class Operation:
            transact_amount = TransactionAmount()

        oper = Operation()

        oper.transact_amount = 100

        with self.assertRaises(ValueError):
            oper.transact_amount = "100"

        self.assertTrue(hasattr(oper, "transact_amount"))
        self.assertEqual(100, oper.transact_amount)

    def test_card_reader_change_non_valid(self):
        class Operation:
            card_num = CardReader()

        oper = Operation()
        oper.card_num = "1234567887654321"

        self.assertTrue(hasattr(oper, "card_num"))
        ans = "1234 5678 8765 4321"

        with self.assertRaises(ValueError):
            oper.card_num = "123456789987654321"

        self.assertEqual(ans, oper.card_num)