# -*- coding: utf-8 -*-
"""Generates an NPC.

`The Briggs Meyers personality types
    <http://en.wikipedia.org/wiki/Myers-Briggs_Type_Indicator>`_
"""
from npcgenerator.Random import Random
from npcgenerator.generic_data.demeanors import DEMEANORS
from npcgenerator.generic_data.history import HISTORY
from npcgenerator.generic_data.body import EYES
from npcgenerator.generic_data.body import HAIR
from npcgenerator.generic_data.body import SKIN
from npcgenerator.generic_data.body import MALE_BODY
from npcgenerator.generic_data.body import FEMALE_BODY
from npcgenerator.generic_data.proficencies import SKILLS_COMPETENCE
from npcgenerator.generic_data.personalities import BRIGGS_MYERS
from npcgenerator.generic_data.fears import FEARS
from npcgenerator.generic_data.fears import FEAR_SEVERITY


class NPC(object):
    """Generates a random NPC."""

    # A list of super generic skills.
    SKILLS = [
        u"Soldier",
        u"Law Enforcer",
        u"Petty Criminal",
        u"Under World",
        u"Academic",
        u"Researcher",
        u"Artisan",
        u"Entertainer",
        u"Religious",
        u"Administrator",
    ]

    def __init__(self, male, female, last, skills=SKILLS):
        """Initiator."""
        self._name_first_male = Random(data=male)
        self._name_first_female = Random(data=female)
        self._name_last = Random(data=last)
        self._personality_type = Random(data=BRIGGS_MYERS)
        self._skills = Random(data=skills)
        self._competance = Random(data=SKILLS_COMPETENCE)
        self._body_eyes = Random(data=EYES)
        self._body_hair = Random(data=HAIR)
        self._body_skin = Random(data=SKIN)
        self._history = Random(data=HISTORY)
        self._demeanors = Random(DEMEANORS)
        self._body_type_male = Random(data=MALE_BODY)
        self._body_type_female = Random(data=FEMALE_BODY)
        self._fears = Random(data=FEARS)
        self._fear_severities = Random(data=FEAR_SEVERITY)
        #self.get_new_data()
        self._last_name = "Doe"
        self._first_name_female = "Jane"
        self._first_name_male = "John"
        self._personality = "None"
        self._demeanor = "None"
        self._eyes = "None"
        self._hair = "None"
        self._skin = "None"
        self._body_type = "None"
        self._body_shape = "None"
        self._skill_primary = ("None", "(+0) Mediocre")
        self._skill_secondary = ("None", "(+0) Mediocre")
        self._skill_hobby = ("None", "(+0) Mediocre")
        self._history_primary = "None"
        self._history_secondary = "None"
        self._fear = ("None", "None")

    @property
    def last_name(self):
        """Accessor."""
        return self._last_name

    @property
    def first_name_female(self):
        """Accessor."""
        return self._first_name_female

    @property
    def first_name_male(self):
        """Accessor."""
        return self._first_name_male

    @property
    def personality(self):
        """Accessor."""
        return self._personality

    @property
    def demeanor(self):
        """Accessor."""
        return self._demeanor

    @property
    def eyes(self):
        """Accessor."""
        return self._eyes

    @property
    def hair(self):
        """Accessor."""
        return self._hair

    @property
    def skin(self):
        """Accessor."""
        return self._skin

    @property
    def body_type(self):
        """Accessor."""
        return self._body_type

    @property
    def body_shape(self):
        """Accessor."""
        return self._body_shape

    @property
    def primary_skill(self):
        """Accessor."""
        return self._skill_primary

    @property
    def secondary_skill(self):
        """Accessor."""
        return self._skill_secondary

    @property
    def hobby_skill(self):
        """Accessor."""
        return self._skill_secondary

    @property
    def primary_history(self):
        """Accessor."""
        return self._history_primary

    @property
    def secondary_history(self):
        """Accessor."""
        return self._history_secondary

    @property
    def fear(self):
        """Accessor."""
        return self._fear

    @property
    def get_all_data(self):
        """Accessor."""
        return (self.last_name, self.first_name_female, self.first_name_male,
                self.personality, self.demeanor,
                self.eyes, self.hair, self.skin,
                self.body_type, self.body_shape,
                self.primary_skill, self.secondary_skill, self.hobby_skill,
                self.primary_history, self.secondary_history,
                )

    def get_skill(self):
        """Returns a tuple of skill name and proficiency."""
        return (self._skills.get_a_value(), self._competance.get_a_value())

    def get_fear(self):
        """Returns a tuple of a fear with its severity."""
        return (self._fear_severities.get_a_value(),
                self._fears.get_a_value())

    def get_new_data(self):
        """Creates new NPC data."""
        self._last_name = self._name_last.get_a_value().title()
        self._first_name_female = self._name_first_female.get_a_value()
        self._first_name_male = self._name_first_male.get_a_value()
        self._personality = self._personality_type.get_a_value()
        self._demeanor = self._demeanors.get_a_value().title()
        self._eyes = self._body_eyes.get_a_value()
        self._hair = self._body_hair.get_a_value()
        self._skin = self._body_skin.get_a_value()
        self._body_type = self._body_type_male.get_a_value()
        self._body_shape = self._body_type_female.get_a_value()
        self._skill_primary = self.get_skill()
        self._skill_secondary = self.get_skill()
        self._skill_hobby = self.get_skill()
        self._history_primary = self._history.get_a_value()
        self._history_secondary = self._history.get_a_value()
        self._fear = self.get_fear()

    def get_markdown(self):
        """Outputs as markdown to stdout."""
        return u"""[[!table  data=\"\"\"
What                | Description
Name                | __%s__; \u2640 _%s_ - \u2642 _%s_
Personality         | %s
Demeanor            | %s.
Physical            | %s eyes, %s hair, and %s complexion.
Body type           | %s (%s).
Fear                | (%s) %s.
Primary skills      | %s %s.
Secondary skills    | %s %s.
Hobby skills        | %s %s.
Major past event    | %s.
Minor past event    | %s.
\"\"\"]]""" % (
            self._last_name, self._first_name_female, self._first_name_male,
            self._personality, self._demeanor,
            self._eyes, self._hair, self._skin,
            self._body_type, self._body_shape,
            self._fear[0], self._fear[1],
            self._skill_primary[0], self._skill_primary[1],
            self._skill_secondary[0], self._skill_secondary[1],
            self._skill_hobby[0], self._skill_hobby[1],
            self._history_primary, self._history_secondary,
        )
