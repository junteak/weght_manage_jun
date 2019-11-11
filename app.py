'''

toDO 1.表示をリスト形式にする 2.それを番号付きにしたものを削除モードで作る
toDO 名前以外を入れたらエラー
toDO 体重のところで01、もしくは小数点をいれたら動かず変な挙動をするのをなんとかする
toDO 入力の時点で整数かどうかをチェックする方法をちゃんとする

'''
import sys

from add import add_menbers
from display import display_users
from dl_all import delete_all
from dl_individual import dl_indvidual

print('\n体重管理アプリ\n')


def main():
    print('1.登録 2.表示 3.削除 4.終了')
    command_num = int(input(' コマンドを入力してください > '))

    if command_num == 1:  # 登録コマンド
        name = input("\n 名前を入力してください > ")

        # weight = 0  空で作ろうとしたがWhileの中でも生きてる？
        while True:
            weight = int(input(" 体重を入力してください(Kg) > "))
            if weight >= 2 and weight <= 500:
                break  # ループから抜け出しその下へ
            else:
                print('\n 正しい値を入力してください\n')

        add_menbers(name, weight)  # メンバー登録
        print(f' {name}, {weight}Kg を登録しました。\n')
        main()

    if command_num == 2:  # 表示コマンド
        print()  # 改行
        display_users()
        print()  # 改行
        main()

    if command_num == 3:  # 削除コマンド
        while True:
            command_dl_num = int(input('\n 1.全員を消す 2.個人を消す > '))
            if command_dl_num in range(1, 3):  # リストなので in にする。
                break  # ループから抜け出しその下へ
            else:
                print(' 注)正しいコマンドを入力して下さい。')

        if command_dl_num == 1:
            delete_all()
            print('\n 全員のデータが削除されました。\n')
            main()

        if command_dl_num == 2:  # 個別削除
            print()
            display_users()

            dl_indvidual()

            main()

    if command_num == 4:
        print('\n 終了しました。')
        sys.exit()

    if not command_num in range(1, 5):  # リストなので in にする。
        print('\n  注)正しいコマンドを入力して下さい。\n')
        main()

    # if not isinstance(command, int):  # 整数でなければ https://www.whyit.work/entry/2018/08/14/235416
    #     print('\n 注)正しいコマンドを入力して下さい。')
    #     main()


if __name__ == '__main__':
    main()
