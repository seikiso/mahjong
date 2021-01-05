import random


class Taku:
    def __init__(self):
        self.yama = list(
            ['1m', '1m', '1m', '1m', '2m', '2m', '2m', '2m', '3m', '3m', '3m', '3m', '4m', '4m', '4m', '4m', '5m', '5m',
             '5m', '5m', '6m', '6m', '6m', '6m', '7m', '7m', '7m', '7m', '8m', '8m', '8m', '8m', '9m', '9m', '9m', '9m',
             '1p', '1p', '1p', '1p', '2p', '2p', '2p', '2p', '3p', '3p', '3p', '3p', '4p', '4p', '4p', '4p', '5p', '5p',
             '5p', '5p', '6p', '6p', '6p', '6p', '7p', '7p', '7p', '7p', '8p', '8p', '8p', '8p', '9p', '9p', '9p', '9p',
             '1s', '1s', '1s', '1s', '2s', '2s', '2s', '2s', '3s', '3s', '3s', '3s', '4s', '4s', '4s', '4s', '5s', '5s',
             '5s', '5s', '6s', '6s', '6s', '6s', '7s', '7s', '7s', '7s', '8s', '8s', '8s', '8s', '9s', '9s', '9s', '9s',
             '1z', '1z', '1z', '1z', '2z', '2z', '2z', '2z', '3z', '3z', '3z', '3z', '4z', '4z', '4z', '4z', '5z', '5z',
             '5z', '5z', '6z', '6z', '6z', '6z', '7z', '7z', '7z', '7z'])
        random.shuffle(self.yama)


class Janshi:
    def __init__(self):
        self.tehai = []
        self.sutehai = []

    def get_haipai(self, yama):
        self.tehai = yama[0:13]
        del yama[0:13]

        return self.tehai

    def riipai(self):
        self.tehai = sorted(self.tehai)
        manzu = [s for s in self.tehai if 'm' in s]
        pinzu = [s for s in self.tehai if 'p' in s]
        souzu = [s for s in self.tehai if 's' in s]
        zihai = [s for s in self.tehai if 'z' in s]
        self.tehai = manzu + pinzu + souzu + zihai

    def tsumo(self, yama):
        hai = yama[0]
        del yama[0]
        self.tehai.append(hai)

        return hai

    def dahai(self):
        # TODO ユーザーが打牌選択をできるようにする
        # 現状は、右端を切るだけのロジック（萬子の染め手）
        hai = self.tehai[13]
        del self.tehai[13]
        self.sutehai.append(hai)

        return hai