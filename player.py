from dataclasses import dataclass
from typing import List

from roulette import Pocket, Roulette
from strategies import PlayerBet, Strategy


@dataclass
class Player:
    strategy: Strategy
    balance: int = 1000

    def make_bets(
        self, *, roulette: Roulette, spin_history: List[Pocket]
    ) -> List[PlayerBet]:
        bets = self.strategy.make_choice(
            available_bets=roulette.available_bets,
            spin_history=spin_history,
            bankroll=self.balance
        )
        for bet in bets:
            self.balance -= bet.amount

        return bets

    def collect_reward(self, amount) -> None:
        self.balance += amount
