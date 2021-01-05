import _mahjong

taku = _mahjong.Taku()
yama = taku.yama
print("山　最初")
print(yama)
print('')

janshi1 = _mahjong.Janshi()
janshi1.get_haipai(yama)
print('手牌')
print(janshi1.tehai)
print('')

print('理牌後　手牌')
janshi1.riipai()
print(janshi1.tehai)
print('')

for i in range(50):
    print('%s順目　手牌' % (i + 1))
    tsumohai = janshi1.tsumo(yama)
    print('自摸' + tsumohai)
    print(janshi1.tehai)
    dahai = janshi1.dahai()
    janshi1.riipai()
    print('打' + dahai)
    print(janshi1.tehai)
    print('')

print('捨て牌')
print(janshi1.sutehai)
print('')

print('山　最後')
print(yama)
