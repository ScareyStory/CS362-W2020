from unittest import TestCase
import testUtility
import Dominion
import testDominion1

class TestCard(TestCase):

    def setUp(self):
        self.nV = testDominion1.nV
        self.nC = testDominion1.nC
        self.player_names = testDominion1.player_names
        self.box = testUtility.GetBoxes(self.nV)
        self.supply = testUtility.GetSupply(self.nV, self.nC, self.supply, self.player_names)

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        # instantiate the card object
        card = Dominion.Coin_card(self.player.name,cost,buypower)

        # verify that the class variables have the expected values
        self.assertEqual('Annie',card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin",card.category)
        self.assertEqual(0, card.vpoints)




    def test_react(self):
        pass
