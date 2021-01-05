from pygame.locals import *
import pygame
import sys


def main():
    pygame.init()  # Pygameを初期化
    screen = pygame.display.set_mode((1280, 720))  # 画面を作成
    pygame.display.set_caption("Pygame sample app")  # タイトルを作成

    yoko = 10

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

    for t in janshi1.tehai:
        # 画像の大きさを変える
        img3 = pygame.image.load('static/' + t + '.png')
        img3 = pygame.transform.scale(img3, (80, 100))  # 200 * 130に画像を縮小

        screen.blit(img3, (yoko, 600))

        yoko = yoko + 85

    running = True
    # メインループ
    while running:

        pygame.display.update()  # 描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了


if __name__ == "__main__":
    main()