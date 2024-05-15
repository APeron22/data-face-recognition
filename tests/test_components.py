from nbresult import ChallengeResultTestCase


class TestComponents(ChallengeResultTestCase):
    def test_minimal_pc(self):
        self.assertIn(self.result.min_pc, [36, 37, 38, 39])
