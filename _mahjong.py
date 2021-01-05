import random

from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter


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

    def get_manzu_from_tehai(self):
        return [s for s in self.tehai if 'm' in s]

    def get_pinzu_from_tehai(self):
        return [s for s in self.tehai if 'p' in s]

    def get_souzu_from_tehai(self):
        return [s for s in self.tehai if 's' in s]

    def get_zihai_from_tehai(self):
        return [s for s in self.tehai if 'z' in s]

    def check_houra(self, hai):
        _manzu = ''
        for m in self.get_manzu_from_tehai():
            _manzu += m.replace('m', '')

        _pinzu = ''
        for p in self.get_pinzu_from_tehai():
            _pinzu += p.replace('p', '')

        _souzu = ''
        for s in self.get_souzu_from_tehai():
            _souzu += s.replace('s', '')

        _zihai = ''
        for z in self.get_zihai_from_tehai():
            _zihai += z.replace('z', '')

        # アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=字牌)
        tiles = TilesConverter.string_to_136_array(man=_manzu, pin=_pinzu, sou=_souzu, honors=_zihai)

        _hai = ''
        win_tile = ''
        if 'm' in hai:
            _hai = hai.replace('m', '')
            win_tile = TilesConverter.string_to_136_array(man=_hai)[0]

        if 'p' in hai:
            _hai = hai.replace('p', '')
            win_tile = TilesConverter.string_to_136_array(pin=_hai)[0]

        if 's' in hai:
            _hai = hai.replace('s', '')
            win_tile = TilesConverter.string_to_136_array(sou=_hai)[0]

        if 'z' in hai:
            _hai = hai.replace('z', '')
            win_tile = TilesConverter.string_to_136_array(honors=_hai)[0]

        # 鳴き(なし)
        melds = None

        # ドラ(なし)
        dora_indicators = None

        # オプション(なし)
        config = None

        # 計算
        calculator = HandCalculator()
        result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
        if result.error is None:
            print(result)
            print(result.yaku)
            print(result.cost)

    def tsumo(self, yama):
        hai = yama[0]
        del yama[0]
        self.tehai.append(hai)
        self.check_houra(hai)

        return hai

    def dahai(self):
        dahai = input()
        hai = self.tehai[int(dahai)]
        del self.tehai[int(dahai)]
        self.sutehai.append(hai)

        return hai
