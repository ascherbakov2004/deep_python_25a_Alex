import unittest
from custom_meta import CustomMeta


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEAR_DOWN")

    def test_one_cls_attribute(self):
        class TestClass(metaclass=CustomMeta):
            x = 50

        self.assertTrue(hasattr(TestClass, "custom_x"))
        self.assertFalse(hasattr(TestClass, "x"))
        self.assertEqual(50, TestClass.custom_x)

    def test_two_cls_attributes(self):
        class TestClass(metaclass=CustomMeta):
            x = 50
            y = "string"

        self.assertTrue(hasattr(TestClass, "custom_x"))
        self.assertFalse(hasattr(TestClass, "x"))
        self.assertEqual(50, TestClass.custom_x)

        self.assertTrue(hasattr(TestClass, "custom_y"))
        self.assertFalse(hasattr(TestClass, "y"))
        self.assertEqual("string", TestClass.custom_y)

    def test_one_init_attribute(self):
        class TestClass(metaclass=CustomMeta):
            def __init__(self):
                self.var = 42

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_var"))
        self.assertFalse(hasattr(cls_inst, "var"))
        self.assertEqual(42, cls_inst.custom_var)

    def test_cls_and_init_attribute(self):
        class TestClass(metaclass=CustomMeta):
            x = "str"

            def __init__(self):
                self.var = 42

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_var"))
        self.assertFalse(hasattr(cls_inst, "var"))
        self.assertEqual(42, cls_inst.custom_var)

        self.assertTrue(hasattr(cls_inst, "custom_x"))
        self.assertFalse(hasattr(cls_inst, "x"))
        self.assertEqual("str", cls_inst.custom_x)

    def test_cls_and_init_attribute_rewrite(self):
        class TestClass(metaclass=CustomMeta):
            x = "str"

            def __init__(self):
                self.x = 42

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_x"))
        self.assertFalse(hasattr(cls_inst, "x"))
        self.assertEqual(42, cls_inst.custom_x)

    def test_one_cls_func(self):
        class TestClass(metaclass=CustomMeta):
            def func(self):
                return 42

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_func"))
        self.assertFalse(hasattr(cls_inst, "func"))
        self.assertEqual(42, cls_inst.custom_func())

    def test_two_cls_func(self):
        class TestClass(metaclass=CustomMeta):
            def func1(self):
                return 42

            def func2(self):
                return 43

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_func1"))
        self.assertFalse(hasattr(cls_inst, "func1"))
        self.assertEqual(42, cls_inst.custom_func1())

        self.assertTrue(hasattr(cls_inst, "custom_func2"))
        self.assertFalse(hasattr(cls_inst, "func2"))
        self.assertEqual(43, cls_inst.custom_func2())

    def test_magicmethod(self):
        class TestClass(metaclass=CustomMeta):
            def __str__(self):
                return "Custom_by_metaclass"

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "__str__"))
        self.assertFalse(hasattr(cls_inst, "custom___str__"))
        self.assertFalse(hasattr(cls_inst, "__custom_str__"))
        self.assertEqual("Custom_by_metaclass", str(cls_inst))

    def test_not_magicmethod(self):
        class TestClass(metaclass=CustomMeta):
            def str__(self):
                return "Custom_by_metaclass"

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "custom_str__"))
        self.assertFalse(hasattr(cls_inst, "str__"))

    def test_nonpublic_attr_and_method(self):
        class TestClass(metaclass=CustomMeta):
            _var = 42

            def __init__(self):
                self._var2 = 2

            def _func(self):
                return 4

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "_custom_var"))
        self.assertTrue(hasattr(cls_inst, "_custom_var2"))
        self.assertTrue(hasattr(cls_inst, "_custom_func"))

    def test_private_attr_and_method(self):
        class TestClass(metaclass=CustomMeta):
            __var = 42

            def __init__(self):
                self.__var2 = 2

            def __func(self):
                return 4

        cls_inst = TestClass()
        self.assertTrue(hasattr(cls_inst, "_custom_TestClass__var"))
        self.assertTrue(hasattr(cls_inst, "_custom_TestClass__var2"))
        self.assertTrue(hasattr(cls_inst, "_custom_TestClass__func"))

    def test_dynamic_attr_cls(self):
        class TestClass(metaclass=CustomMeta):
            pass

        TestClass.var = 1

        self.assertTrue(hasattr(TestClass, "custom_var"))
        self.assertFalse(hasattr(TestClass, "var"))
        self.assertEqual(1, TestClass.custom_var)

    def test_dynamic_func_cls(self):
        class TestClass(metaclass=CustomMeta):
            pass

        TestClass.func = lambda x: x + 1

        self.assertTrue(hasattr(TestClass, "custom_func"))
        self.assertFalse(hasattr(TestClass, "func"))
        self.assertEqual(2, TestClass.custom_func(1))

    def test_dynamic_func_cls(self):
        class TestClass(metaclass=CustomMeta):
            pass

        TestClass.func = lambda x: x + 1

        self.assertTrue(hasattr(TestClass, "custom_func"))
        self.assertFalse(hasattr(TestClass, "func"))
        self.assertEqual(2, TestClass.custom_func(1))

    def test_dynamic_attr_and_func_inst(self):
        class TestClass(metaclass=CustomMeta):
            pass

        cls_inst = TestClass()
        cls_inst.var = 1
        cls_inst.func = lambda x: x + 1

        self.assertTrue(hasattr(cls_inst, "custom_var"))
        self.assertFalse(hasattr(cls_inst, "var"))
        self.assertEqual(1, cls_inst.custom_var)

        self.assertTrue(hasattr(cls_inst, "custom_func"))
        self.assertFalse(hasattr(cls_inst, "func"))
        self.assertEqual(2, cls_inst.custom_func(1))

    def test_attrs_two_cls_inst(self):
        class TestClass(metaclass=CustomMeta):
            pass

        cls_inst1 = TestClass()
        cls_inst2 = TestClass()
        cls_inst1.var = 1
        cls_inst2.var = 2

        self.assertTrue(hasattr(cls_inst1, "custom_var"))
        self.assertFalse(hasattr(cls_inst1, "var"))
        self.assertEqual(1, cls_inst1.custom_var)

        self.assertTrue(hasattr(cls_inst2, "custom_var"))
        self.assertFalse(hasattr(cls_inst2, "var"))
        self.assertEqual(2, cls_inst2.custom_var)

    def test_func_two_cls_inst(self):
        class TestClass(metaclass=CustomMeta):
            pass

        cls_inst1 = TestClass()
        cls_inst2 = TestClass()
        cls_inst1.func = lambda x: x + 1
        cls_inst2.func = lambda x: x + 2

        self.assertTrue(hasattr(cls_inst1, "custom_func"))
        self.assertFalse(hasattr(cls_inst1, "func"))
        self.assertEqual(1, cls_inst1.custom_func(0))

        self.assertTrue(hasattr(cls_inst2, "custom_func"))
        self.assertFalse(hasattr(cls_inst2, "func"))
        self.assertEqual(2, cls_inst2.custom_func(0))

    def test_cls_attr_two_classes_inst(self):
        class TestClass(metaclass=CustomMeta):
            var = 1
            pass

        cls_inst1 = TestClass()
        cls_inst2 = TestClass()
        cls_inst2.custom_var = 2

        self.assertTrue(hasattr(cls_inst1, "custom_var"))
        self.assertFalse(hasattr(cls_inst1, "var"))
        self.assertEqual(1, cls_inst1.custom_var)

        self.assertTrue(hasattr(cls_inst2, "custom_var"))
        self.assertFalse(hasattr(cls_inst2, "var"))
        self.assertEqual(2, cls_inst2.custom_var)

    def test_setattr_magicmethod(self):
        class TestClass(metaclass=CustomMeta):
            var = 1
            pass

        cls_inst = TestClass()
        cls_inst.__magic__ = 1

        self.assertTrue(hasattr(cls_inst, "__magic__"))
        self.assertFalse(hasattr(cls_inst, "custom___magic__"))
        self.assertFalse(hasattr(cls_inst, "_custom___magic__"))
        self.assertEqual(1, cls_inst.__magic__)