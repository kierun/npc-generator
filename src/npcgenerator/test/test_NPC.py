# -*- coding: utf-8 -*-
"""Unit and Component tests for SUT: NPC
"""
import unittest
from mock import patch, mock_open
from npcgenerator.NPC import NPC as SUT
from npcgenerator.generic_data.proficencies import SKILLS_COMPETENCE


class UnitTestRandom(unittest.TestCase):
    """Unit test cases."""

    def setUp(self):
        """Setup before each test case."""
        self.sut = SUT(['John'], ['Jane'], ['Doe'])
        self.assertEqual(self.sut.last_name, 'Doe')
        self.assertEqual(self.sut.first_name_female, 'Jane')
        self.assertEqual(self.sut.first_name_male, 'John')
        for entry in [self.sut.personality,
                      self.sut.demeanor,
                      self.sut.eyes,
                      self.sut.hair,
                      self.sut.skin,
                      self.sut.body_type,
                      self.sut.body_shape,
                      self.sut.primary_history,
                      self.sut.secondary_history]:
            self.assertEqual("None", entry)
        self.assertEqual(self.sut.primary_skill, ("None", "(+0) Mediocre"))
        self.assertEqual(self.sut.secondary_skill, ("None", "(+0) Mediocre"))
        self.assertEqual(self.sut.hobby_skill, ("None", "(+0) Mediocre"))
        self.assertEqual(self.sut.fear, ("None", "None"))

    def tearDown(self):
        """Cleans up after each test case."""

    def test_skill(self):
        result = self.sut.get_skill()
        self.assertTrue(result[0] in self.sut.SKILLS)
        self.assertTrue(result[1] in SKILLS_COMPETENCE)

    def test_get_npc(self):
        result = self.sut.get_markdown()
        for entry in ['Name',
            'Personality',
            'Demeanor',
            'Physical',
            'Body type',
            'Primary skills',
            'Secondary skills',
            'Hobby skills',
            'Major past event',
            'Minor past event']:
            self.assertTrue(entry in result)

    def test_get_new_data(self):
        old = self.sut.get_all_data
        self.sut.get_new_data()
        new = self.sut.get_all_data
        self.assertNotEqual(old, new)
