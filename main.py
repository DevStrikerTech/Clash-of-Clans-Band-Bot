import time

from routes.band import get_post
from commands.clan import Clan
from commands.player import Player
from commands.warlog import Warlog


class BandBot:
    def __init__(self):
        print('Bot is online!')

        while True:
            self.get_all_post = get_post()
            Clan(self.get_all_post)
            Player(self.get_all_post)
            Warlog(self.get_all_post)

            time.sleep(60)


if __name__ == '__main__':
    BandBot()
