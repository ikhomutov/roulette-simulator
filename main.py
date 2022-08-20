import logging

from game import Game
from player import Player
from roulette import Roulette
from strategies import ColorStrategy

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main() -> None:
    player = Player(strategy=ColorStrategy('red'))
    roulette = Roulette()
    game = Game(roulette=roulette, players=[player])
    game.play(3)
    logger.info(f'{player.balance=}')


if __name__ == '__main__':
    main()
