__author__ = 'Afzal'
#if you want to encrypt or decrypt a password then this program will do for you.
print("Do you want to encrypt a passwrod or decrypt a password?")
print("\n if you want to encrypt\n Press 1\nif you want to decrypt\n Press 2")
Press=int(input("Press 1or 2: "))
if Press==1:
#below code is use to encrypt your password
    dictionary={"A":"0","B":"1","C":"9","D":"2","E":"8","F":"3","G":"7","H":"4","I":"6","J":"5","k":"!","L":"+","M":"@","N":"_",
            "I":"#","P":")",
    "Q":"$","R":"(","S":"%","T":"*","U":"^","V":"&","W":"=","X":"-","Y":"]","Z":"[","1":"L",
            "2":"K","3":"J","4":"H","4":"I","5":"P","6":"C","7":"T",
    "   8":"O","9":"X","0":"A"}
    password=input("Enter the password: ").upper()
    encrypted_password=""
    for var in password:
        if var in dictionary:
            encrypted_password=encrypted_password+dictionary[var]
        else:
            encrypted_password=encrypted_password+var
    print(encrypted_password.lower())

elif Press==2:
#This below code is use to decrypt your password
    dictionary={"0":"A","1":"B","9":"C","2":"D","8":"E","3":"F","7":"G","4":"H","6":"I","5":"J","!":"K","+":"L","@":"M","_":"N",
    "#":"I",")":"P",
    "$":"Q","(":"R","%":"S","*":"T","^":"U","&":"V","=":"W","-":"X","]":"Y","[":"Z","L":"1",
        "K":"2","J":"3","H":"4","I":"4","P":"5","C":"6","T":"7",
    "   O":"8","X":"9","A":"0"}
    password=input("Enter the password: ").upper()
    decrypted_password=""
    for var in password:
        if var in dictionary:
            decrypted_password=decrypted_password+dictionary[var]
        else:
            decrypted_password=decrypted_password+var
    print(decrypted_password.lower())

else:
    print("Please Enter the valid number")