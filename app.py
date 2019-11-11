'''
toDo 更新を入れる
toDO 名前以外を入れたらエラー
toDO 体重のところで01、もしくは小数点をいれたら動かず変な挙動をするのをなんとかする
toDO 入力の時点で整数かどうかをチェックする方法をちゃんとする

'''
# import os
import sys

from add import add_menbers
from display import display_users
from dl_all import delete_all
from dl_individual import dl_indvidual
from upd_weigt import upd_weight

print('\n体重管理アプリ\n')


def main():
    # os.system('clear')  # 画面が新しくなるはずだができない。

    print('1.登録 2.表示 3.更新 4.削除 5.終了')
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

        display_users()
        print()  # 改行
        main()

    if command_num == 3:
        print()  # 改行
        display_users()  # 選んでもらう
        upd_weight()  # 更新する関数
        main()

    if command_num == 4:  # 削除コマンド
        while True:  # 1,2 以外の数字をいれると動かないようにしてる。
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
            print()  # 改行
            display_users()  # 選んでもらう

            dl_indvidual()  #消す関数

            main()

    if command_num == 5:
        print('\n 終了しました。')
        sys.exit()

    if not command_num in range(1, 6):  # 1~4 以外の数字をいれると動かないようにしてる。リストなので in
        print('\n  注)正しいコマンドを入力して下さい。\n')
        main()

    # if not isinstance(command, int):  # 整数でなければ https://www.whyit.work/entry/2018/08/14/235416
    #     print('\n 注)正しいコマンドを入力して下さい。')
    #     main()


if __name__ == '__main__':
    main()
