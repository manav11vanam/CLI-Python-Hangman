from getpass import getpass
from os import system


def posit(string,character):
    li=list()
    for i in range(len(string)):
        if string[i] == character : li.append(i)
    return li
class Hangman:
    def __init__(self):
        self.score = 0
    def hangman(self):
        str1 = ""
        newlist = list()
        anslist = list()
        entered_list = list()
        print("You have limited number of wrong guesses i.e 10")
        count = 10
        str = getpass(prompt = "Enter word: ")
#print(str)
        n = len(str)
        print("The length of the word is",n)
        for i in range(n):
            if str[i]==" ":
                newlist.append(" ")
                anslist.append(" ")
                newlist.append(" ")
                anslist.append(" ")
                continue
            newlist.append(str[i])
            newlist.append(" ")
            anslist.append("_")
            anslist.append(" ")
        print(str1.join(anslist))
        str1 = ""
        while True:
            position_list = []
            str1 = ""
            char = input("Enter a letter: ")
            if len(char)!=1:
                print("Enter only one character!!!")
                continue
            if char in entered_list:
                print("You have tried this character already")
                continue
            entered_list.append(char)
            position_list = posit(str,char)
            #print(position_list)
            if position_list == []:
                print("Uhh huh... Character not present")
                count = count - 1
                if count == 0 :
                    print("You failed")
                    break
                print("You have",count,"chances remaining")
            for pos in position_list:
                anslist[(pos*2)] = char
            print(str1.join(anslist))
    #print(anslist)
    #print(newlist)
            if anslist==newlist:
                print("Well done")
                self.score = self.score + 1
                break

def my_print():
    print("\nPlayer 1:",obj1.score)
    print("Player 2:",obj2.score)
    print("\nPress any key to proceed")

def check():
    if obj1.score>obj2.score:
        print("\t******Player 1 wins******")
    elif obj1.score<obj2.score:
        print("\t******Player 2 wins******")
    else:
        print("!!!It's a draw!!!")

####################################################################################################
while True:
    _ = system("cls")
    print("Welcome to 2 player hangman")
    rounds = int(input("How many rounds would you like to play? "))
    _ = system("cls")
    obj1 = Hangman()
    obj2 = Hangman()


    for i in range(rounds):
        _ = system("cls")
        print("\tPlayer 1 guesses, Player 2 gives the word")
        obj1.hangman()
        my_print()
        unwanted = input("")
        _ = system("cls")
        print("\tPlayer 2 guesses, Player 1 gives the word\n\n")
        obj2.hangman()
        my_print()
        unwanted = input("")

    check()
    ch = input("Do you want to play again(y/n)? ")
    if ch.lower() in ["n","no"]: break
