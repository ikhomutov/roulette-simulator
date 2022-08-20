import random
from dataclasses import dataclass
from typing import Dict, List


class Pocket(str):
    pass


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
    {
        'code': 'high',
        'multiplier': 2,
        'winning_pockets':[
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
            '12', '13', '14', '15', '16', '17', '18'
        ],
    },
    {
        'code': 'low',
        'multiplier': 2,
        'winning_pockets':[
            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
            '30', '31', '32', '33', '34', '35', '36'
        ],
    },
    {
        'code': 'even',
        'multiplier': 2,
        'winning_pockets':[
            '2', '4', '6', '8', '10', '12', '14', '16', '18', '20',
            '22', '24', '26', '28', '30', '32', '34', '36',
        ],
    },
    {
        'code': 'odd',
        'multiplier': 2,
        'winning_pockets':[
            '1', '3', '5', '7', '9', '11', '13', '15', '17', '19',
            '21', '23', '25', '27', '29', '31', '33', '35',
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
    def generate_bets() -> dict[str, dict]:
        bets = {
            str(i): dict(multiplier=36, winning_pockets=[Pocket(i)])
            for i in range(37)
        }
        for bet in bets_config:
            bets.update({
                bet['code']: dict(
                    multiplier=bet['multiplier'],
                    winning_pockets=[Pocket(i) for i in bet['winning_pockets']]
                )
            })
        return bets

    def spin(self) -> Pocket:
        return random.choice(self.board)
