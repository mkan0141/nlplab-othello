
def Put_koma():


    #入力処理
    print("駒をどこに置くか指定してください．(A1 ~ H8)")
    place = input()
    
    tate = int( place[1:2] )
    yoko = place[0:1]
    
    
    
    #縦の処理
    if 8 < tate or tate < 1:
        print("2桁目の数値は 1 ~ 8 の数値で入力してください．")
        tate = NONE
        yoko = NONE
    else:
        tate = tate - 1
    
    
    #横の処理
    if yoko == "A" or yoko == "a":
        yoko = 0
    elif yoko == "B" or yoko == "b":
        yoko = 1
    elif yoko == "C" or yoko == "c":
        yoko = 2
    elif yoko == "D" or yoko == "d":
        yoko = 3
    elif yoko == "E" or yoko == "e":
        yoko = 4
    elif yoko == "F" or yoko == "f":
        yoko = 5
    elif yoko == "G" or yoko == "g":
        yoko = 6
    elif yoko == "H" or yoko == "h":
        yoko = 7
    else :
        print("1桁目の入力は A ~ H　を入力してください．")
        tate = NONE
        yoko = NONE


    #戻り値(NONEをintでキャストした場合はどうなるか知らんｗ)
    return int(tate), int(yoko)




