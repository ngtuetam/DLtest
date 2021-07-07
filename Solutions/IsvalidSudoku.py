'''
Problem : Kiem tra ket qua Sudoku
Solution :
- Kiem tra cung dong o (x,y) :
    Voi moi 0 <y<9 , neu j khac y  va a[x][y]==a[x][j] => false
- Kiem tra theo cot o (x,y):
    Voi moi 0 <i <9 , neu x khac y va  a[x][y] == a[i][y] => false
- Kiem tra theo bang con 3x3: (cac bang con co the phan thanh cac cum toa do : 3 dong/cot -> 1 toa do)
-> Toa do rieng cua cac bang con : 0 <= blockx < 3 , 0 <= blocky < 3 . Tu toa do cua cac o gia tri suy ra vi tri cua o nay trong bang con nao:
   + blockx = x/3
   + blocky = y/3
 So sanh o nay voi gia tri trong bang con do voi 3blockx <= i < 3(blockx + 1) , 3blocky <= j < 3(blocky + 1)
 Neu co mau thuan => false, khong => True
- Neu tat ca 3 dieu kien tren dung => "YES" , khong => "NO"
'''
#Code:
def checkBlock(x, y):
    '''Kiem tra bang con
    x : row
    y : col
    '''
    block_x = x // 3
    block_y = y // 3
    count = 0
    for i in range(3*block_x, 3*(block_x + 1)):
        for j in range(3*block_y, 3*(block_y + 1)):
            if table[x][y] == table[i][j]:
                count += 1
    if count > 1:
        return False
    else:
        return True


# Kiem tra hang va cot
def RowCol(x, y):
    for j in range(9):
        if j != y and table[x][y] == table[x][j]:
            return False

    for i in range(9):
        if i != x and table[x][y] == table[i][y]:
            return False
    return True


def main():
    global table
    table = []
    for _ in range(9):
        temp = list(map(int, input().split()))
        table.append(temp)

    for i in range(9):
        for j in range(9):
            if not (RowCol(i, j) and checkBlock(i, j)):
                return False
    return True


if __name__ == "__main__":
    if main():
        print("YES")
    else:
        print("NO")
