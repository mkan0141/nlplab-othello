class Player():
    def input_valid_position(self, valid_pos):
        for pos in valid_pos:
            pos[0] = chr(ord('A') + int(pos[0]))
            pos[1] += 1

            print('{}{}, '.format(pos[0], pos[1]), end='')
        print()



    def put_stone(self):
        while True :

            Flag = 0
            Flag2 = 0


            #入力処理
            print("駒をどこに置くか指定してください．(A1 ~ H8)")
            place = input()

            tate = int( place[1:2] )
            yoko = place[0:1]

            #縦の処理
            if 8 < tate or tate < 1:
                print("不正な入力値です：2桁目の数値は 1 ~ 8 の数値で入力してください．")
            else:
                tate = tate - 1
                Flag = 1


            #横の処理
            if yoko == "A" or yoko == "a":
                yoko = 0
                Flag2 = 1
            elif yoko == "B" or yoko == "b":
                yoko = 1
                Flag2 = 1
            elif yoko == "C" or yoko == "c":
                yoko = 2
                Flag2 = 1
            elif yoko == "D" or yoko == "d":
                yoko = 3
                Flag2 = 1
            elif yoko == "E" or yoko == "e":
                yoko = 4
                Flag2 = 1
            elif yoko == "F" or yoko == "f":
                yoko = 5
                Flag2 = 1
            elif yoko == "G" or yoko == "g":
                yoko = 6
                Flag2 = 1
            elif yoko == "H" or yoko == "h":
                yoko = 7
                Flag2 = 1
            else :
                print("不正な入力値です：1桁目の入力は A ~ H　を入力してください．")


            if Flag == 1 and Flag2 == 1:
                break

        #戻り値
        return int(tate), int(yoko)

