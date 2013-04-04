# -*- coding: utf-8 -*-
"""Unit and Component tests for SUT: Random
"""
import unittest
from mock import patch, mock_open
from npcgenerator.Random import Random as SUT


class UnitTestRandom(unittest.TestCase):
    """Unit test cases."""

    def setUp(self):
        """Setup before each test case."""

    def tearDown(self):
        """Cleans up after each test case."""

    def test_file(self):
        with patch('codecs.open',
                   mock_open(read_data='Stup!d monkey'),
                   create=True) as mock_file:
            test_file = '/path/to/file'
            sut = SUT(data=test_file)
            mock_file.assert_called_once_with(test_file, 'r', 'utf-8')
            self.assertEqual(sut._data, ['Stup!d monkey'])
            self.assertEqual('Stup!d monkey', sut.get_a_value())

    def test_list(self):
        this = ['Stup!d monkey']
        sut = SUT(data=this)
        self.assertEqual(sut._data, ['Stup!d monkey'])
        self.assertEqual('Stup!d monkey', sut.get_a_value())

    def test_nada(self):
        self.assertRaises(RuntimeError, SUT)
