def checkUndifinedChar(str):
    for char in str:
        if char not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()=+-_":
            return False
    return True

def checkIdentifier(str):
    if str[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new = list(str)
        new[0] = ''
        str = ''.join(new)
    for char in str:
        if char not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            return False
    return True

def tokenizer(str):
    mylist = []
    temp = ""
    for char in str:
        if char in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_":
            temp = temp + char
        else :
            if temp != "":
                mylist.append(temp)
            mylist.append(char)
            temp = ""
    mylist.append(temp)
    return mylist

def garbageCollector(mylist):
    resList = []
    for temp in mylist:
        if not (temp == " " or temp == ""):
            resList.append(temp)
    return resList

def numIdentifier(str):
    if str[0] == "-":
        new = list(str)
        new[0] = ""
        str = ''.join(new)
    if str[0] == "0":
        return False
    for temp in str:
        if temp not in "0123456789":
            return False
    return True

def tokenIdentifier(mylist):
    resList = []
    for temp in mylist:
        if temp == "while":
            resList.append("while keyword")
        elif temp == "if":
            resList.append("if keyword")
        elif temp == "(":
            resList.append("Open Paranthes")
        elif temp == ")":
            resList.append("Close Paranthes")
        elif temp == "=":
            resList.append("Equal Operation")
        elif temp == "+":
            resList.append("Arithmathic Operation")
        elif numIdentifier(temp):
            resList.append("Integer")
        elif checkIdentifier(temp):
            resList.append("Identifier") 
        elif not checkUndifinedChar(temp):
            resList.append("Error undifined Char!")
        else :
            resList.append("Error incorreoct identifier or number!")
    return resList

def getBigestLen(mylist):
    num = 0
    for temp in mylist:
        if len(temp) >= num:
            num = len(temp)
    return num

def printTable(list1, list2):
    for count in range(len(list1)):
        print(list1[count], end=" ")
        for count2 in range(getBigestLen(list1) - len(list1[count])):
            print("",end=" ")
        print("|",end=" ")
        print(list2[count])
        print("-------------------------------------")
        
str = input("write the code : ")
listy = []
#listy = tokenizer("if(while op = 123 + (jsk&d456+ ")
listy = tokenizer(str)
listy = garbageCollector(listy)
reslist = []
reslist = tokenIdentifier(listy)

printTable(listy, reslist)
