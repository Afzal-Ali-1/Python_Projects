__author__ = 'Afzal Ali'
try:

    file=open(input("Enter the path of the file : "),"r")
    data=file.read().lower().strip()
    len_of_data=len(data)
    others=0;a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;m=0;n=0;o=0;p=0;q=0;r=0;s=0;t=0;u=0;v=0;w=0;x=0;y=0;z=0

    for var in data:
        if var=="a":
            a+=1
        elif var=="b":
            b+=1
        elif var=="c":
            c+=1
        elif var=="d":
            d+=1
        elif var=="e":
            e+=1
        elif var=="f":
            f+=1
        elif var=="g":
            g+=1
        elif var=="h":
            h+=1
        elif var=="i":
            i+=1
        elif var=="j":
            j+=1
        elif var=="k":
            k+=1
        elif var=="l":
            l+=1
        elif var=="m":
            m+=1
        elif var=="n":
            n+=1
        elif var=="0":
            o+=1
        elif var=="p":
            p+=1
        elif var=="q":
            q+=1
        elif var=="r":
            r+=1
        elif var=="s":
            s+=1
        elif var=="t":
            t+=1
        elif  var=="u":
            u+=1
        elif var=="v":
            v+=1
        elif var=="w":
            w+=1
        elif var=="x":
            x+=1
        elif var=="y":
            y+=1
        elif var=="z":
            z+=1
    else:
        others+=1

except:
    print("file is not found !\n please enter the right path of the file.")
else:
    print("The perceage of a in given file is {}".format((a/len_of_data)*100),"%")
    print("The perceage of b in given file is {}".format((b/len_of_data)*100),"%")
    print("The perceage of c in given file is {}".format((c/len_of_data)*100),"%")
    print("The perceage of d in given file is {}".format((d/len_of_data)*100),"%")
    print("The perceage of e in given file is {}".format((e/len_of_data)*100),"%")
    print("The perceage of f in given file is {}".format((f/len_of_data)*100),"%")
    print("The perceage of g in given file is {}".format((g/len_of_data)*100),"%")
    print("The perceage of h in given file is {}".format((h/len_of_data)*100),"%")
    print("The perceage of i in given file is {}".format((i/len_of_data)*100),"%")
    print("The perceage of j in given file is {}".format((j/len_of_data)*100),"%")
    print("The perceage of k in given file is {}".format((k/len_of_data)*100),"%")
    print("The perceage of l in given file is {}".format((l/len_of_data)*100),"%")
    print("The perceage of m in given file is {}".format((m/len_of_data)*100),"%")
    print("The perceage of n in given file is {}".format((n/len_of_data)*100),"%")
    print("The perceage of o in given file is {}".format((o/len_of_data)*100),"%")
    print("The perceage of p in given file is {}".format((p/len_of_data)*100),"%")
    print("The perceage of q in given file is {}".format((q/len_of_data)*100),"%")
    print("The perceage of r in given file is {}".format((r/len_of_data)*100),"%")
    print("The perceage of s in given file is {}".format((s/len_of_data)*100),"%")
    print("The perceage of t in given file is {}".format((t/len_of_data)*100),"%")
    print("The perceage of u in given file is {}".format((u/len_of_data)*100),"%")
    print("The perceage of v in given file is {}".format((v/len_of_data)*100),"%")
    print("The perceage of w in given file is {}".format((w/len_of_data)*100),"%")
    print("The perceage of x in given file is {}".format((x/len_of_data)*100),"%")
    print("The perceage of y in given file is {}".format((y/len_of_data)*100),"%")
    print("The perceage of z in given file is {}".format((z/len_of_data)*100),"%")
    print("The perceage of others in given file is {}".format((others/len_of_data)*100),"%")
    file.close()