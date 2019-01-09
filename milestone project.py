import os
print("Welcome..!!!")
x = " "
while x == " ":
    x = input("Player 1 Enter X or O to select the symbol you want to continue with \n")
    p1 = ""
    p2 = ""
    if x.lower() == "x":
        p1 = "X"
        p2 = "O"
    elif x.lower() == "o":
        p1 = "O"
        p2 = "X"
    else:
        print("Invalid Input. Please enter a valid input")
        x = " "

print(f"Player 1-> '{p1}' and Player 2-> '{p2}'")
l1 = {1:' ',2: ' ',3:' ',4:' ',5: ' ',6:' ',7:' ',8: ' ',9:' '}

def the_board():
    print(l1)
    print(f" {l1[7]} || {l1[8]} || {l1[9]} ")
    print("==============")
    print(f" {l1[4]} || {l1[5]} || {l1[6]} ")
    print("==============")
    print(f" {l1[1]} || {l1[2]} || {l1[3]} ")
set_1 = set()
for num in range(1,10):
    os.system('cls')
    if num%2!=0:
        if position in set_1:

        try:
            position = int(input("Player 1, please enter the position you want"))
        except:
            print("Invalid position")
            position = 0

        while position<1 or position>9:
            if position in set_1:
                try:
                    position = int(input("Please enter a valid position from 1 to 9"))
                except:
                    print("Invalid position")
                    position = 0
            else:
                try:
                    position = int(input("Please enter a valid position from 1 to 9"))
                except:
                    print("Invalid position")
                    position = 0
        l1[position] = p1
        set_1.add(position)
        the_board()
        if l1[1]==l1[2]==l1[3]==p1 or l1[4]==l1[5]==l1[6]==p1 or l1[7]==l1[8]==l1[9]==p1 or l1[3]==l1[6]==l1[9]==p1 or l1[2]==l1[5]==l1[8]==p1 or l1[1]==l1[4]==l1[7]==p1 or l1[1]==l1[5]==l1[9]==p1 or l1[3]==l1[5]==l1[7]==p1:
            print("Congratulatons..!!! Player 1 wins")
            break
    elif num%2 == 0:
        position = int(input("Player 2, please enter the position you want"))
        l1[position] = p2
        the_board()
        if l1[1]==l1[2]==l1[3]==p2 or l1[4]==l1[5]==l1[6]==p2 or l1[7]==l1[8]==l1[9]==p2 or l1[3]==l1[6]==l1[9]==p2 or l1[2]==l1[5]==l1[8]==p2 or l1[1]==l1[4]==l1[7]==p2 or l1[1]==l1[5]==l1[9]==p2 or l1[3]==l1[5]==l1[7]==p2:
            print("Congratulatons..!!! Player 2 wins")
            break
