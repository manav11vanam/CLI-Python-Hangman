from getpass import getpass

def posit(string,character):
    li=list()
    for i in range(len(string)):
        if string[i] == character : li.append(i)
    return li

newlist = list()
anslist = list()
print("Welcome To Hangman")
print("You have limited number of wrong guesses i.e 10")
count = 10
str = getpass(prompt = "Enter word: ")
#print(str)
n = len(str)
print("The length of the word is",n)
for i in range(n):
    newlist.append(str[i])
    anslist.append("_")
#print(anslist)
while True:
    position_list = []
    char = input("Enter a letter: ")
    if len(char)!=1:
        print("Enter only one character!!!")
        continue
    position_list = posit(str,char)
    #print(position_list)
    if position_list == []:
        print("Uhh huh... Character not present")
        count = count - 1
        if count == 0 :
            print("Game over! You failed")
            break
        print("You have",count,"chances remaining")
    for pos in position_list:
        anslist[pos] = char
    print(anslist)
    if anslist==newlist:
        print("Congrats")
        break
