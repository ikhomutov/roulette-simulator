import logging
from collections import defaultdict
from dataclasses import dataclass

from player import Player
from roulette import Pocket, Roulette

logger = logging.getLogger(__name__)

@dataclass
class Winner:
    player: Player
    reward: int


class Game:
    def __init__(self, players: list[Player], roulette: Roulette):
        self.players = players
        self.roulette = roulette
        self.bets: dict[str, list[tuple]] = defaultdict(list)  # example: {'black': [(<player1 object>, 100),]}
        self.spin_history: list[Pocket] = []

    def place_bets(self) -> None:
        for player in self.players:
            player_bets = player.make_bets(
                roulette=self.roulette, spin_history=self.spin_history
            )
            for player_bet in player_bets:
                self.bets[player_bet.bet].append(
                    (player, player_bet.amount)
                )

    def get_winners(self, spin_result: Pocket) -> list[Winner]:
        winners = []
        for bet, bet_info in self.bets.items():
            roulette_bet = self.roulette.available_bets.get(bet)
            if not roulette_bet:
                continue
            if spin_result not in roulette_bet['winning_pockets']:
                continue
            for player, amount in bet_info:
                winners.append(
                    Winner(
                        player=player, reward=amount * roulette_bet['multiplier']
                    )
                )
        return winners

    def play(self, count: int = 1) -> None:
        for _ in range(count):
            self.place_bets()
            logger.debug(f'{self.bets=}')

            spin_result = self.roulette.spin()
            logger.debug(f'{spin_result=}')
            self.spin_history.append(spin_result)

            winners = self.get_winners(spin_result)
            logger.debug(f'{winners=}')

            for winner in winners:
                winner.player.collect_reward(winner.reward)

            self.bets.clear()