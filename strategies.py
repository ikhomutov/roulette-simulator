import random
from dataclasses import dataclass
from typing import Protocol

from roulette import Pocket


@dataclass
class PlayerBet:
    bet: str
    amount: int


class Strategy(Protocol):
    def make_choice(
        self,
        *,
        available_bets: dict[str, dict],
        spin_history: list[Pocket],
        bankroll: int
    ) -> PlayerBet:
        pass


class RandomStrategy:
    def make_choice(self, *, available_bets, **kwargs):
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
