#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_instances(self):

        instance_1 = Base()
        instance_2 = Base()
        instance_3 = Base(200)
        instance_4 = Base(None)
        instance_5 = Base(28)
        instance_6 = Base()
        

        self.assertEqual(instance_1.id, 1)
        self.assertEqual(instance_2.id, 2)
        self.assertEqual(instance_3.id, 200)
        self.assertEqual(instance_4.id, 4)
        self.assertEqual(instance_5.id, 28)
        self.assertEqual(instance_6.id, 6)

