import unittest
from unittest.mock import patch
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def _cust_lists_equal(self, cust_list_left, cust_list_right):
        if len(cust_list_left) != len(cust_list_right):
            return False

        for left_elem, right_elem in zip(cust_list_left, cust_list_right):
            if left_elem != right_elem:
                return False

        return True

    def test_compare_cust_lists(self):
        cust_list1 = CustomList([1, 2, 3])
        cust_list2 = CustomList([4, 5, 6])
        cust_list3 = CustomList([9, 6])
        self.assertTrue(cust_list1 < cust_list2)
        self.assertTrue(cust_list1 <= cust_list2)
        self.assertTrue(cust_list2 > cust_list1)
        self.assertTrue(cust_list2 >= cust_list1)
        self.assertTrue(cust_list2 == cust_list3)
        self.assertTrue(cust_list2 >= cust_list3)
        self.assertTrue(cust_list2 <= cust_list3)

    def test_add_cust_lists(self):
        cust_list1 = CustomList([1, 2, 3])
        cust_list2 = CustomList([1, 2, 4])

        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 4, 7]), cust_list1 + cust_list2)
        )

    def test_add_cust_lists_left_bigger(self):
        cust_list1 = CustomList([1, 2])
        cust_list2 = CustomList([1, 2, 4])

        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 4, 4]), cust_list1 + cust_list2)
        )

    def test_add_cust_lists_left_smaller(self):
        cust_list1 = CustomList([1, 2, 3])
        cust_list2 = CustomList([1, 2])

        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 4, 3]), cust_list1 + cust_list2)
        )

    def test_cust_add_original_list(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 4]), cust_list + orig_list)
        )

    def test_original_add_cust_list(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 4]), orig_list + cust_list)
        )

    def test_original_add_cust_list_left_smaller(self):
        cust_list = CustomList([1, 2])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 1]), orig_list + cust_list)
        )

    def test_original_add_cust_list_left_bigger(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 3]), orig_list + cust_list)
        )

    def test_original_add_cust_list_right_smaller(self):
        cust_list = CustomList([1, 2])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 1]), cust_list + orig_list)
        )

    def test_original_add_cust_list_right_bigger(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([2, 3, 3]), cust_list + orig_list)
        )

    def test_sub_cust_lists(self):
        cust_list1 = CustomList([1, 2, 3])
        cust_list2 = CustomList([1, 2, 4])

        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 0, -1]), cust_list1 - cust_list2)
        )

    def test_sub_cust_lists_left_bigger(self):
        cust_list1 = CustomList([1, 2])
        cust_list2 = CustomList([1, 2, 4])

        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 0, -4]), cust_list1 - cust_list2)
        )

    def test_sub_cust_lists_left_smaller(self):
        cust_list1 = CustomList([1, 2, 3])
        cust_list2 = CustomList([1, 2])

        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 0, 3]), cust_list1 - cust_list2)
        )

    def test_cust_sub_original_list(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 1, 2]), cust_list - orig_list)
        )

    def test_original_sub_cust_list(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, -1, -2]), orig_list - cust_list)
        )

    def test_original_sub_cust_list_left_smaller(self):
        cust_list = CustomList([1, 2])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, -1, 1]), orig_list - cust_list)
        )

    def test_original_sub_cust_list_left_bigger(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, -1, -3]), orig_list - cust_list)
        )

    def test_original_sub_cust_list_right_smaller(self):
        cust_list = CustomList([1, 2])
        orig_list = [1, 1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 1, -1]), cust_list - orig_list)
        )

    def test_original_sub_cust_list_right_bigger(self):
        cust_list = CustomList([1, 2, 3])
        orig_list = [1, 1]
        self.assertTrue(
            self._cust_lists_equal(CustomList([0, 1, 3]), cust_list - orig_list)
        )

    def test_extend_zeros(self):
        cust_list_short = CustomList([1, 2])
        cust_list_long = CustomList([1, 2, 3, 4])

        add = cust_list_short + cust_list_long
        sub = cust_list_short - cust_list_long
        self.assertTrue(self._cust_lists_equal(CustomList([2, 4, 3, 4]), add))
        self.assertTrue(self._cust_lists_equal(CustomList([0, 0, -3, -4]), sub))

    def test_empty_extend_zeros(self):
        cust_list_short = CustomList([])
        cust_list_long = CustomList([1, 2, 3, 4])

        add = cust_list_short + cust_list_long
        sub = cust_list_short - cust_list_long
        self.assertTrue(self._cust_lists_equal(CustomList([1, 2, 3, 4]), add))
        self.assertTrue(self._cust_lists_equal(CustomList([-1, -2, -3, -4]), sub))

    def test_args_not_change(self):
        cust_list = CustomList([1, 2, 3])
        cust_list2 = [0, 2] + cust_list + [1]
        cust_list2 = cust_list2 + [2]
        self.assertTrue(self._cust_lists_equal(CustomList([1, 2, 3]), cust_list))

    def test_complex_expression(self):
        cust_list = CustomList([1, 2, 3])
        cust_list2 = CustomList([1, 1])
        res = [1] + cust_list + [0, 0, 1] + cust_list2
        ans = CustomList([3, 3, 4])
        self.assertTrue(self._cust_lists_equal(ans, res))

    def test_print(self):
        cust_list1 = CustomList([1, 2, 3])
        self.assertEqual("elements: [1, 2, 3] sum: 6", str(cust_list1))

        cust_list2 = CustomList([-1, 1])
        self.assertEqual("elements: [-1, 1] sum: 0", str(cust_list2))

    def test_not_changed_after_sum(self):
        cust_list_short = CustomList([1, 2])
        cust_list_long = CustomList([1, 2, 3, 4])

        add = cust_list_short + cust_list_long
        self.assertTrue(self._cust_lists_equal(CustomList([1, 2]), cust_list_short))
        self.assertTrue(
            self._cust_lists_equal(CustomList([1, 2, 3, 4]), cust_list_long)
        )

    def test_not_changed_after_sub(self):
        cust_list_short = CustomList([1, 2])
        cust_list_long = CustomList([1, 2, 3, 4])

        sub = cust_list_short - cust_list_long
        self.assertTrue(self._cust_lists_equal(CustomList([1, 2]), cust_list_short))
        self.assertTrue(
            self._cust_lists_equal(CustomList([1, 2, 3, 4]), cust_list_long)
        )