################ Old test showcase #####################

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual("foo".upper(), "FOO")
#
# if __name__ == "__main__":
#     unittest.main()


def test_assert():
    assert "foo".upper() == "FOO"
    assert "foo".upper() == "fOO"
