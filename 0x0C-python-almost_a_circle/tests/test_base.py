#!/usr/bin/python3
import unittest
Base = __import__("models.base").base.Base


class TestBase(unittest.TestCase):

    def test_instances(self):

        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(200).id, 200)
        self.assertEqual(Base(id=12).id, 12)
