'''
Created on 24/11/2014

@author: daniel
'''
import unittest

from poker.dados import straight_flush2, quadra1, full_house1, doi_pares1, \
    flush1, straigh1, um_par1, trinca1, carta_alta1
from poker.poker import poker, rank_mao


class Test(unittest.TestCase):


    def testPoker(self):
        self.assertEqual(poker[(straight_flush2, quadra1)], straight_flush2)
        self.assertEqual(poker[(full_house1, quadra1)], quadra1)
        self.assertEqual(poker[(straight_flush2, straight_flush2)], None)
        self.assertEqual(poker[(straight_flush2, full_house1)], straight_flush2)
        
        self.assertEqual(poker[(flush1, straigh1)], flush1)
        self.assertEqual(poker[(straigh1, um_par1)], straigh1)
        self.assertEqual(poker[(trinca1, doi_pares1)], trinca1)
        self.assertEqual(poker[(um_par1, doi_pares1)], doi_pares1)
        self.assertEqual(poker[(doi_pares1, flush1)], flush1)
        self.assertEqual(poker[(carta_alta1, um_par1)], um_par1)
        self.assertEqual(poker[(um_par1, carta_alta1)], um_par1)
        self.assertEqual(poker[(straight_flush2, trinca1)], straight_flush2)
        self.assertEqual(poker[(straight_flush2, carta_alta1)], straight_flush2)
    
    def testRank_mao(self):
        self.testRank_mao(rank_mao(straight_flush2), 9)
        self.testRank_mao(rank_mao(quadra1), 8)
        self.testRank_mao(rank_mao(full_house1), 7)
        self.testRank_mao(rank_mao(flush1), 6)
        self.testRank_mao(rank_mao(straigh1), 5)
        self.testRank_mao(rank_mao(trinca1), 4)
        self.testRank_mao(rank_mao(doi_pares1), 3)
        self.testRank_mao(rank_mao(um_par1), 2)
        self.testRank_mao(rank_mao(quadra1), 8)
        self.testRank_mao(rank_mao(carta_alta1), 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
    