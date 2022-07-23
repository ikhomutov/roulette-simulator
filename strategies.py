import random
from dataclasses import dataclass
from typing import List, Protocol

from roulette import Bet, Pocket


@dataclass
class PlayerBet:
    bet: str
    amount: int


class Strategy(Protocol):
    def make_choice(
        self,
        *,
        available_bets: List[Bet],
        spin_history: List[Pocket],
        bankroll: int
    ) -> PlayerBet:
        pass


class RandomStrategy:
    def make_choice(self, *, available_bets, spin_history, bankroll):
        return [
            PlayerBet(
                bet=random.choice(list(available_bets.keys())), amount=100
            )
        ]


class ColorStrategy:
    def __init__(self, color: str = 'black'):
        self.color = color

    def make_choice(self, *args, **kwargs):
        return [PlayerBet(bet=self.color, amount=100)]
