import unittest
from MainCode.table_tennis_ladder import match_played

class TestMatchPlayed(unittest.TestCase):
    
    def match_winner_higher(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma","Alpha","Beta","Delta"]
        new_ladder = match_played(winner,loser,ladder)
        self.assertEqual("Alpha",new_ladder[1])

if __name__ == '__main__':
    unittest.main()
        