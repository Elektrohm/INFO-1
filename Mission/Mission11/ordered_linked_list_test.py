import unittest
# from ordered_linked_list import OrderedLinkedList
from ordered_linked_list_inheritance import OrderedLinkedList


class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.emptylist = OrderedLinkedList()
        self.twolist = OrderedLinkedList([1, 2])
        self.threelist = OrderedLinkedList()
        self.threelist.add(3)
        self.threelist.add(2)
        self.threelist.add(1)
        self.longlist = OrderedLinkedList(["abc", "def", "xyz"])

    def test_init(self):
        self.assertEqual(self.emptylist.size(), 0)
        self.assertIsNone(self.emptylist.first())

    def test_size(self):
        self.assertEqual(self.emptylist.size(), 0)
        self.assertEqual(self.twolist.size(), 2)
        self.assertEqual(self.longlist.size(), 3)

    def test_first(self):
        self.assertIsNone(self.emptylist.first())
        self.assertEqual(self.twolist.first().value(), 1)
        self.assertEqual(self.longlist.first().value(), "abc")
        self.assertEqual(self.twolist.first(), self.twolist.Node(1))
        self.assertEqual(self.longlist.first(), self.twolist.Node("abc"))

    def test_add(self):
        self.longlist.add("aaa")
        self.longlist.add("ghi")
        self.longlist.add("def")
        self.longlist.add("zzz")
        self.assertEqual(self.longlist.size(), 7)
        self.assertEqual(self.longlist.first().value(), "aaa")
        self.assertEqual(self.longlist.first().next().value(), "abc")
        self.assertEqual(self.longlist.first().next().next().value(), "def")
        self.assertEqual(self.longlist.first().next().next().next().value(), "def")
        self.assertEqual(self.longlist.first().next().next().next().next().value(), "ghi")
        self.assertEqual(self.longlist.first().next().next().next().next().next().value(), "xyz")
        self.assertEqual(self.longlist.first().next().next().next().next().next().next().value(), "zzz")

    def test_add_2(self):
        l = self.twolist
        self.assertEqual(self.twolist.first().value(), 1)
        l.add(3)
        self.assertEqual(self.twolist.size(), 3)
        self.assertEqual(self.twolist.first().value(), 1)
        l.add(4)
        self.assertEqual(self.twolist.size(), 4)
        self.assertEqual(self.twolist.first().value(), 1)
        l.add(0)
        l.add(5)
        self.assertEqual(self.twolist.size(), 6)
        self.assertEqual(self.twolist.first().value(), 0)

    def test_remove(self):
        l = self.threelist
        self.assertEqual(l.size(), 3)
        self.assertEqual(l.first().value(), 1)
        l.remove(1)
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.first().value(), 2)
        l.remove(3)
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.first().value(), 2)
        l.remove(3)
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.first().value(), 2)
        l.remove(2)
        self.assertEqual(l.size(), 0)
        self.assertIsNone(l.first())
        l.remove(2)
        self.assertEqual(l.size(), 0)
        self.assertIsNone(l.first())

    def test_add_and_remove(self):
        self.twolist.remove(2)
        self.twolist.remove(1)
        self.twolist.add(1)
        self.twolist.add(2)
        self.assertEqual(self.twolist.size(), 2)
        self.assertEqual(self.twolist.first().value(), 1)
        self.assertEqual(self.twolist.first().next().value(), 2)

    def test_find(self):
        self.assertEqual(self.longlist.find("abc").value(), "abc")
        self.assertEqual(self.longlist.find("qqq"), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
