x=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
y=["z","a","s","i","Z","1","o","q","Y","3","0","j","X","","S","p","s","x","R","T","W","4","b","r","2","U","Q","w","5","V","y","c","n","P","6","m","v","t","M","7","d","O","B","N","L","u","k","J","9","e","I","K","f","g","I","h","G","A","F","B","H","C","D","E"]
d=open("code.txt","w")
e=open("code2.txt","w")
d.writelines(x)
e.writelines(y)
d.close()
e.close()
a=0
y=""
while a==0:
    print "\n"*3
    print "\t"*4,
    print "OPTION"
    print "\n"
    print "\t"*3,
    print "1.Want to code or decode"
    print "\t"*3,
    print "2.Want to play zellers algorithm"
    print "\t"*3,
    choice=input("Enter the choice:")
    print "\t"*3,
    print "\n"*3,
    s=""
    f=open("code.txt","r")
    g=open("code2.txt","r")
    q=f.readlines()
    w=g.readlines()
    if choice==1:
        print "\t"*4,
        print "OPTIONS"
        print "\n"
        print "\t"*3,
        print "1.Want to make a code"
        print "\t"*3,
        print "2.Want to decode a code"
        print "\t"*3,
        ch=input("Enter the choice:")
        if ch==1:
            print "\t"*3,
            c=raw_input("Enter the text you want to get coded:")
            for i in range(len(c)):
                for j in range(len(q[0])):
                    if c[i]==q[0][j]:
                        s+=w[0][j]
                    else:
                        s=s
            print "\n"*3,
            print "\t"*3,
            print "The required code is:",s
            y=s
            print "\n"*3,
            print "\t"*3,
            x=raw_input("Want to play more:")
            print "\n"*2
            if x.upper()=="Y":
                a=0
            else:
                a=1
        if ch==2:
            u=""
            print "\t"*3,
            print "Menu"
            print "1.Want to decode the same code"
            print "2.Want to decode the new code"
            c=raw_input("Enter the choice:")
            if c=="1":
                for a in range(len(y)):
                    for b in range(len(w[0])):
                        if y[a]==w[0][b]:
                            u+=q[0][b]
                        else:
                            u=u
                print "\n"*3,
                print "\t"*3,
                print "Thr required decode is:",u
                print "\t"*3,
                x=raw_input("Want to play more:")
                if x.upper()=="Y":
                    a=0
                else:
                    a=1
            elif c=="2":
                d=raw_input("Enter the code to be decoded:")
                for a in range(len(d)):
                    for b in range(len(w[0])):
                        if d[a]==w[0][b]:
                            u+=q[0][b]
                        else:
                            u=u
                print "\n"*3,
                print "\t"*3,
                print "The required decoide is:",u
                print "\t"*3,
                x=raw_input("Want to play more:")
                if x.upper()=="Y":
                    a=0
                else:
                    a=1
            else:
                print "\t"*3,
                print "\n"*3,
                print "Wrong inpur"
                a=0
    elif choice==2:
        def input_value(input_name,prompt,min_num,max_num):
            while True:
                data=raw_input(prompt)
                if data:
                    try:
                        input_name=int(data)
                    except ValueError:
                        print "Invalid Input..."
                    else:
                        if input_name>=min_num and input_name<=max_num:
                            return input_name
                            break
                        input_name="Please try again:"
                else:
                    print "Goodbye!"
                    break
        month=0
        day=0
        year=0
        century=0
        print "\t"*3,
        month=input_value(month,"Please enter the month(from 1-12,where March is 1 and February is 12):",1,12)
        print "\t"*3,
        day=input_value(day,"Please enter the day (from 1-31):",1,31)
        print "\t"*3,
        year=input_value(year,"Please enter the year(from 0 to 99 eg.88 for 1988):",0,99)
        print "\t"*3,
        century=input_value(century,"Please enter century(from 0 to 99 ef.19 for 1900):",0,19)
        print "\t"*3,
        A=month
        B=day
        C=year
        D=century
        W=(13*A-1)/5
        X=C/4
        Y=D/4
        Z=W+X+Y+B+C-2*D
        R=Z%7
        birthday="You were born on"+str(B)+"/"+str(A+2)+"/"+str(D)+str(C)+"which was a"
        if R==0:
            print "\t"*3,
            print birthday+'Sunday'
        elif R==1:
            print "\t"*3,
            print birthday +'Monday'
        elif R==2:
            print "\t"*3,
            print birthday+'Tuesday'
        elif R==3:
            print "\t"*3,
            print birthday+'Wednesday'
        elif R==4:
            print "\t"*3,
            print birthday+'Thursday'
        elif R==5:
            print "\t"*3,
            print birthday+'Friday'
        elif R==6:
            print "\t"*3,
            print birthday+'Saturday'
        x=raw_input("Want to play mare:")
        if x.upper()=='Y':
            a=0
        else:
            a=1
print "\n"*3,
print "\t"*3,
print "Thanks for playing"
