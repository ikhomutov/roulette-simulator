import random
from dataclasses import dataclass
from typing import Dict, List


class Pocket(str):
    pass


@dataclass
class Bet:
    code: str
    multiplier: int
    winning_pockets: List[Pocket]

    def __str__(self):
        return self.code


bets_config = [
    {
        'code': 'red',
        'multiplier': 2,
        'winning_pockets': [
            '1', '3', '5', '7', '9', '12', '14', '16', '18', '19',
            '21', '23', '25', '27', '30', '32', '34', '36',
        ],
    },
    {
        'code': 'black',
        'multiplier': 2,
        'winning_pockets': [
            '2', '4', '6', '8', '10', '11', '13', '15', '17', '20',
            '22', '24', '26', '28', '29', '31', '33', '35',
        ],
    },
]


class Roulette:
    def __init__(self):
        self.board = self.generate_board()
        self.available_bets = self.generate_bets()

    @staticmethod
    def generate_board() -> List[Pocket]:
        return [Pocket(i) for i in range(37)]

    @staticmethod
    def generate_bets() -> Dict[str, Bet]:
        bets = {
            str(i): Bet(
                code=str(i), multiplier=36, winning_pockets=[Pocket(i)]
            )
            for i in range(37)
        }
        for bet in bets_config:
            bets.update({
                bet['code']: Bet(
                    code=bet['code'],
                    multiplier=bet['multiplier'],
                    winning_pockets=[Pocket(i) for i in bet['winning_pockets']]
                )
            })
        return bets

    def spin(self) -> Pocket:
        return random.choice(self.board)
