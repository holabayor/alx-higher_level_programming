#!/usr/bin/python3
import unittest
Rectangle = __import__("models.rectangle").rectangle.Rectangle

class TestRectangle(unittest.TestCase):

    def test_normal_init(self):

        rec_1 = Rectangle(3, 4)
        self.assertEqual(rec_1.width, 3)
        self.assertEqual(rec_1.x, 0)
        self.assertEqual(rec_1.y, 0)
        self.assertEqual(rec_1.id, 1)

        rec_2 = Rectangle(3, 4, 2)
        self.assertEqual(rec_2.width, 3)
        self.assertEqual(rec_2.height, 4)
        self.assertEqual(rec_2.x, 2)
        self.assertEqual(rec_2.y, 0)
        self.assertEqual(rec_2.id, 2)
        
        rec_3 = Rectangle(3, 4, 2, 6, 50)
        self.assertEqual(rec_3.width, 3)
        self.assertEqual(rec_3.height, 4)
        self.assertEqual(rec_3.x, 2)
        self.assertEqual(rec_3.y, 6)
        self.assertEqual(rec_3.id, 50)
        
        rec_4 = Rectangle(3, 4, 2, 6)
        self.assertEqual(rec_4.width, 3)
        self.assertEqual(rec_4.height, 4)
        self.assertEqual(rec_4.x, 2)
        self.assertEqual(rec_4.y, 6)
        self.assertEqual(rec_4.id, 4)

    def test_attributes(self):
        with self.assertRaises(TypeError):
            rec_2 = Rectangle(1)
        with self.assertRaises(TypeError):
            rec_1 = Rectangle()

    def test_area(self):
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)
        with self.assertRaises(TypeError):
            rect.area(1)

    def test_str(self):
        rect_1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect_1), "[Rectangle] (12) 2/1 - 4/6")
