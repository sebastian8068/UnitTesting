import platform
import unittest

SERVER = "server_b"


class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(5, 5, "Values should be equal")
        self.assertEqual("hello", "hello", "Strings should be equal")
        self.assertEqual([1, 2, 3], [1, 2, 3], "Lists should be equal")
        self.assertEqual((1, 2), (1, 2), "Tuples should be equal")
        self.assertEqual({"a": 1}, {"a": 1}, "Dictionaries should be equal")
        self.assertAlmostEqual(
            0.1 + 0.2, 0.3, places=7, msg="Floats should be almost equal"
        )
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_not_equal(self):
        self.assertNotEqual(5, 3, "Values should not be equal")

    def test_assert_true_or_false(self):
        self.assertTrue(3 < 5, "Condition should be true")
        self.assertFalse(5 < 3, "Condition should be false")
        self.assertTrue(True, "Value should be true")
        self.assertFalse(False, "Value should be false")
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_true(self):
        self.assertTrue(3 < 5, "Condition should be true")

    def test_assert_false(self):
        self.assertFalse(5 < 3, "Condition should be false")

    def test_assert_is_none(self):
        self.assertIsNone(None, "Value should be None")

    def test_assert_is_not_none(self):
        self.assertIsNotNone(5, "Value should not be None")

    def test_assert_is(self):
        a = b = [1, 2, 3]
        self.assertIs(a, b, "Both should refer to the same object")

    def test_assert_is_not(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertIsNot(a, b, "Both should not refer to the same object")

    def test_assert_raises(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0  # Division by zero

    def test_assert_raises_with_message(self):
        with self.assertRaises(ValueError, msg="Should raise ValueError"):
            int("invalid")
        with self.assertRaises(ValueError):
            int("I am not a number")

    def test_assert_raises_regex(self):
        with self.assertRaisesRegex(ValueError, "invalid literal"):
            int("invalid")

    def test_assert_greater(self):
        self.assertGreater(5, 3, "First value should be greater than second")

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(
            5, 5, "First value should be greater than or equal to second"
        )

    def test_assert_in(self):
        self.assertIn(3, [1, 2, 3], "Value should be in the list")
        self.assertIn("a", "apple", "Character should be in the string")
        self.assertIn(1, {1, 2, 3}, "Value should be in the set")
        self.assertIn(
            "key", {"key": "value"}, "Key should be in the dictionary"
        )
        self.assertIn(2, (1, 2, 3), "Value should be in the tuple")
        self.assertIn(10, [2, 4, 5, 10])
        self.assertIn("H", "Hola")

    def test_assert_not_in(self):
        self.assertNotIn(4, [1, 2, 3], "Value should not be in the list")
        self.assertNotIn("b", "apple", "Character should not be in the string")
        self.assertNotIn(4, {1, 2, 3}, "Value should not be in the set")
        self.assertNotIn(
            "missing_key",
            {"key": "value"},
            "Key should not be in the dictionary",
        )
        self.assertNotIn(4, (1, 2, 3), "Value should not be in the tuple")
        self.assertNotIn(5, [2, 4, 10])
        self.assertNotIn("z", "Hola")

    def test_assert_is_empty(self):
        self.assertEqual(len([]), 0, "List should be empty")
        self.assertEqual(len(""), 0, "String should be empty")
        self.assertEqual(len({}), 0, "Dictionary should be empty")
        self.assertEqual(len(set()), 0, "Set should be empty")
        self.assertEqual(len(()), 0, "Tuple should be empty")
        self.assertEqual(len([]), 0)
        self.assertEqual(len(""), 0)
        self.assertEqual(len({}), 0)
        self.assertEqual(len(set()), 0)
        self.assertEqual(len(()), 0)

    def test_assert_is_not_empty(self):
        self.assertNotEqual(len([1]), 0, "List should not be empty")
        self.assertNotEqual(len("a"), 0, "String should not be empty")
        self.assertNotEqual(
            len({"key": "value"}), 0, "Dictionary should not be empty"
        )
        self.assertNotEqual(len({1}), 0, "Set should not be empty")
        self.assertNotEqual(len((1,)), 0, "Tuple should not be empty")
        self.assertNotEqual(len([1]), 0)
        self.assertNotEqual(len("a"), 0)
        self.assertNotEqual(len({"key": "value"}), 0)
        self.assertNotEqual(len({1}), 0)
        self.assertNotEqual(len((1,)), 0)

    def test_assert_count_equal(self):
        self.assertCountEqual(
            [1, 2, 2, 3],
            [3, 2, 1, 2],
            "Both lists should have the same elements with the same frequency",
        )
        self.assertCountEqual(
            ["a", "b", "b"],
            ["b", "a", "b"],
            "Both lists should have the same elements with the same frequency",
        )
        self.assertCountEqual(
            [1, 2, 3],
            [1, 2, 3],
            "Both lists should have the same elements with the same frequency",
        )
        self.assertCountEqual([], [], "Both lists should be empty")

    def test_assert_multi_line_equal(self):
        self.assertMultiLineEqual(
            "Hello\nWorld",
            "Hello\nWorld",
            "Both multi-line strings should be equal",
        )
        self.assertMultiLineEqual(
            "Line1\nLine2\nLine3",
            "Line1\nLine2\nLine3",
            "Both multi-line strings should be equal",
        )

    def test_assert_sequence_equal(self):
        self.assertSequenceEqual(
            [1, 2, 3], [1, 2, 3], "Both sequences should be equal"
        )
        self.assertSequenceEqual(
            (1, 2), (1, 2), "Both sequences should be equal"
        )
        self.assertSequenceEqual("abc", "abc", "Both sequences should be equal")

    def test_assert_list_equal(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3], "Both lists should be equal")
        self.assertListEqual([], [], "Both lists should be empty")

    def test_assert_tuple_equal(self):
        self.assertTupleEqual((1, 2), (1, 2), "Both tuples should be equal")
        self.assertTupleEqual((), (), "Both tuples should be empty")

    def test_assert_dict_equal(self):
        self.assertDictEqual(
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
            "Both dictionaries should be equal",
        )
        self.assertDictEqual({}, {}, "Both dictionaries should be empty")

    def test_assert_set_equal(self):
        self.assertSetEqual({1, 2, 3}, {3, 2, 1}, "Both sets should be equal")
        self.assertSetEqual(set(), set(), "Both sets should be empty")

    def test_assert_count(self):
        self.assertEqual(len([1, 2, 3]), 3, "List should have 3 elements")
        self.assertEqual(len("abc"), 3, "String should have 3 characters")
        self.assertEqual(
            len({"a": 1, "b": 2}), 2, "Dictionary should have 2 key-value pairs"
        )
        self.assertEqual(len({1, 2, 3}), 3, "Set should have 3 elements")
        self.assertEqual(len((1, 2)), 2, "Tuple should have 2 elements")

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(
            0.1 + 0.2, 0.3, places=7, msg="Floats should be almost equal"
        )
        self.assertAlmostEqual(
            1.0000001, 1.0000002, places=6, msg="Floats should be almost equal"
        )

    def test_assert_not_almost_equal(self):
        self.assertNotAlmostEqual(
            0.1 + 0.2, 0.4, places=7, msg="Floats should not be almost equal"
        )
        self.assertNotAlmostEqual(
            1.0001, 1.0002, places=4, msg="Floats should not be almost equal"
        )

    def test_assert_dicts(self):
        self.assertDictEqual(
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
            "Both dictionaries should be equal",
        )
        self.assertDictEqual({}, {}, "Both dictionaries should be empty")
        user = {"name": "Alice", "age": 30}
        expected_user = {"name": "Alice", "age": 30}
        self.assertDictEqual(
            user, expected_user, "User dictionaries should be equal"
        )
        self.assertDictEqual({"key": "value"}, {"key": "value"})
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"}, user
        )
        self.assertSetEqual({1, 2, 3}, {1, 2, 3})
        self.assertSetEqual(
            {"python", "java", "c++"}, {"c++", "java", "python"}
        )

    def test_assert_is_instance(self):
        self.assertIsInstance(5, int, "Value should be an instance of int")

    def test_assert_not_is_instance(self):
        self.assertNotIsInstance(
            5, str, "Value should not be an instance of str"
        )

    @unittest.skip("Work in progress, will be enable soon")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(
        SERVER == "server_b", "Skipped bcs you are not in server_a"
    )
    def test_skip_if(self):
        self.assertEqual(1, 1)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual("a", "b")

    @unittest.skipUnless(
        platform.system() == "Linux", "This test only runs on Linux"
    )
    def test_skip_unless(self):
        self.assertEqual(1, 1)
