import unittest
from voter_checker import is_eligible_to_vote


class TestVoterEligibility(unittest.TestCase):
    def test_valid_voter(self):
        self.assertTrue(is_eligible_to_vote(18, True))

    def test_eligible_voter(self):
        self.assertTrue(is_eligible_to_vote(20, True))

    def test_underage_voter(self):
        self.assertFalse(is_eligible_to_vote(16, False))

    def test_non_citizen(self):
        self.assertFalse(is_eligible_to_vote(25, False))

    def test_underage_and_non_citizen(self):
        self.assertFalse(is_eligible_to_vote(16, False))

    def test_exactly_18_and_non_citizen(self):
        self.assertTrue(is_eligible_to_vote(18, True))

    def test_negative_age(self):
        self.assert(is_eligible_to_vote(-0, False))


if __name__ == "__ main __":
    unittest.main
