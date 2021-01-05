# 計算
from mahjong.hand_calculating.hand import HandCalculator
# 麻雀牌
from mahjong.tile import TilesConverter
# 役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
# 鳴き
from mahjong.meld import Meld
# 風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH

# HandCalculator(計算用クラス)のインスタンスを生成
calculator = HandCalculator()
# アガリ形(man=マンズ, pin=ピンズ, sou=ソーズ, honors=字牌)
tiles = TilesConverter.string_to_136_array(man='234555', pin='555', sou='22555')

# アガリ牌(ソーズの5)
win_tile = TilesConverter.string_to_136_array(sou='5')[0]

# 鳴き(なし)
melds = None

# ドラ(なし)
dora_indicators = None

# オプション(なし)
config = None

# 計算
result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
print(result.error)
print(result.yaku)
print(result.cost)
