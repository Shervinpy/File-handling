
print("<<<<<wellcome>>>>>")
user_name = input("enter your username : ")
passcode = input("enter your password : ")

user = False

while True:

    with open("file.txt" , "r") as f:
        for line in f:
            data = line.split()
            if user_name == data [0] and passcode == data [1]:
                user = True
    if user ==True:
        print("open with sucsefuly")
        break
    else:
        print("not found")
        asq = input("do you have create accont(yes/no)? ")
        if asq == "yes":
            user_form = input("enter your username : ")
            user_pass = input("enter your password: ")

            with open ("file.txt","r") as f:
                for i in f:
                    info = i.split()
                    if user_form == info[0] and user_pass == info[1]:
                     print("you cant create reapeat account")
                     print("try again ")
                    break
            with open("file.txt","a") as f:
                        f.writelines("\n")
                        f.writelines(user_form)
                        f.writelines(" ")
                        f.writelines(user_pass)
                        print("acount createed")
                        break
        else:
                print("thank you for see")
                break