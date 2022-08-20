import unittest
from unittest.mock import patch
from game import Game
from roulette import Roulette, Pocket
from player import Player
from strategies import RandomStrategy, PlayerBet


class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.roulette = Roulette()
        cls.player_with_random_strategy = Player(strategy=RandomStrategy())
        return super().setUpClass()

    def test_place_bets(self):
        player_1 = Player(strategy=RandomStrategy())
        game = Game(players=[player_1], roulette=self.roulette)
        with patch.object(Player, 'make_bets', return_value=[PlayerBet('0', 100)]):
            game.place_bets()

            player_1.make_bets.assert_called_once()
        self.assertIn('0', game.bets)
        self.assertEqual(len(game.bets['0']), 1)
        self.assertEqual(game.bets['0'][0], (player_1, 100))

    def test_get_winners(self):
        winner = Player(strategy=RandomStrategy())
        loser = Player(strategy=RandomStrategy())
        game = Game(players=[winner, loser], roulette=self.roulette)
        winning_bet = '0'
        losing_bet = '1'
        game.bets.update({
            winning_bet: [(winner, 100)],
            losing_bet: [(loser, 100)]
        })
        winners = game.get_winners(Pocket(winning_bet))
        self.assertEqual(len(winners), 1)
        self.assertEqual(winners[0].player, winner)

    def test_no_bets_when_no_players(self):
        game = Game(players=[], roulette=self.roulette)
        game.place_bets()
        self.assertDictEqual(game.bets, {})

    def test_bets_are_cleared_after_play(self):
        game = Game(players=[self.player_with_random_strategy], roulette=self.roulette)
        game.bets.update({list(game.roulette.available_bets.keys())[0]: [(self.player_with_random_strategy, 100)]})
        game.play()
        self.assertDictEqual(game.bets, {})


if __name__ == '__main__':
    unittest.main()