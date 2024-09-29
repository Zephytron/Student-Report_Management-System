import csv

def write():
    fh=open("student.csv","a",newline='\n')
    stuwriter=csv.writer(fh)
    lst=[]                                                                          
    while True:                                                               
            fh=open("student.csv","a",newline="\n") 
            stuwriter=csv.writer(fh)
            R=int(input("Enter Roll No.: "))       
            N=input("Enter name of student: ")
            M1=float(input("Enter marks of FA1: "))
            M2=float(input("Enter marks of FA2: "))
            M3=float(input("Enter marks of FA3: "))
            M4=float(input("Enter marks of FA4: "))
            M5=float(input("Enter Mid Term marks: "))
            M6=float(input("Enter Final Term marks: "))
            T1=M1+M2
            T2=M3+M4
            T3=M5+M6
            Perc_entage=((T1+T2+T3)/320)*100
            rec=[R,N,M1,M2,T1,M3,M4,T2,M5,M6,T3,Perc_entage]   
            lst.append(rec)                                                                   
            a=input("Enter N to Quit and Y to continue: ")
            if a=="N"or a=="n":
                break
    for i in lst:                                              
        stuwriter.writerow(i)
    fh.close()
    
def delete():
    file=open('student.csv','r')
    sreader=csv.reader(file)
    L=[]
    R=int(input('Enter roll of student to be Deleted'))
    Found=False
    for i in sreader:
        if i[0] != str(R):
            Found=True
            L.append(i)
        if i[0]==str(R):
            pass
    file.close()
    if Found==False:
        print('Student Not Found')
    elif Found==True:
        file=open('student.csv','w+',newline='')
        stuwriter=csv.writer(file)
        stuwriter.writerows(L)
        sreader=csv.reader(file)
        for i in sreader:
            print(i)
        file.close()
        print('Successfully deleted!')
    else:
        print('DelError')
        
def read():
    fh=open("student.csv","r",newline="\n")
    sreader=csv.reader(fh)
    for i in sreader:
        print(i)
        
def update():
    file=open('student.csv','r')
    sreader=csv.reader(file)
    L=[]
    R=int(input('Enter roll of student to be updated'))
    Maks=input('Which marks do you wanna update?: [FA1-1/FA2-2/FA3-3/FA4-4/MIDTERM-5/FINALS-6/Roll-no.-7/Name-8] ')
    Found=False
    for i in sreader:
        if i[0]==str(R):
            if Maks=='1':
                Marks=float(i[2])
                Tempo=float(i[4])
                Tempo-=Marks
                Marks=float(input('Enter marks: '))
                i[2]=Marks
                Tempo+=Marks
                i[4]=Tempo
                Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
                i[11]=Perc_entage
                print('Updated!')
            elif Maks=='2':
                Marks=float(i[3])
                Tempo=float(i[4])
                Tempo-=Marks
                Marks=float(input('Enter marks: '))
                i[3]=Marks
                Tempo+=Marks
                i[4]=Tempo
                Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
                i[11]=Perc_entage
                print('Updated!')
            elif Maks=='3':
               Marks=float(i[4])
               Tempo=float(i[7])
               Tempo-=Marks
               Marks=float(input('Enter marks: '))
               i[4]=Marks
               Tempo+=Marks
               i[7]=Tempo
               Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
               i[11]=Perc_entage
               print('Updated!')
            elif Maks=='4':
               Marks=float(i[5])
               Tempo=float(i[7])
               Tempo-=Marks
               Marks=float(input('Enter marks: '))
               i[5]=Marks
               Tempo+=Marks
               i[7]=Tempo
               Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
               i[11]=Perc_entage
               print('Updated!')
            elif Maks=='5':
               Marks=float(i[6])
               Tempo=float(i[10])
               Tempo-=Marks
               Marks=float(input('Enter marks: '))
               i[6]=Marks
               Tempo+=Marks
               i[10]=Tempo
               Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
               i[11]=Perc_entage
               print('Updated!')
            elif Maks=='6':
               Marks=float(i[7])
               Tempo=float(i[10])
               Tempo-=Marks
               Marks=float(input('Enter marks: '))
               i[7]=Marks
               Tempo+=Marks
               i[10]=Tempo
               Perc_entage=((float(i[4])+float(i[7])+float(i[10]))/320)*100
               i[11]=Perc_entage
               print('Updated!')
            elif Maks=='7':
                Rno=int(input('Enter updated roll number: '))
                i[0]=Rno
                print('Updated!')
            elif Maks=='8':
                Name=input('Enter updated Name: ')
                i[1]=Name
                print('Updated!')
            else:
                print('Error....Please enter a number between 1-6 :)')                    
            Found=True
        L.append(i)
    file.close()
    if Found==False:
        print('Student Not Found')
    else:
        file=open('student.csv','w+',newline='')
        stuwriter=csv.writer(file)
        stuwriter.writerows(L)
        sreader=csv.reader(file)
        for i in sreader:
            print(i)
        file.close()

def menu():
    a=input("Press 1 to write and 2 to read and 3 to update and 4 to delete: ")
    if a=="1":
        o=input('Is this your first time running the program?: [Y/N] ')
        if o =='Y' or o =='y':
            fh=open("student.csv","a",newline='\n')
            stuwriter=csv.writer(fh)
            stuwriter.writerow(["Roll No.","Name","FA1","FA2","Total","FA3","FA4","Total","Mid Term","Final Term","Total",'Overall Percentage'])
            stuwriter.writerow(["-","-","40","40","80","40","40","80","80","80","160",'100%'])
            fh.close()
            write()
        elif o=='n' or o=='N':
            write()
    elif a=="2":
        read()        
    elif a=="3":
        update()        
    elif a=='4':
        delete()
menu()
z=input("Press 0 to continue and 1 to quit:")
while z=="0":
    menu()
    z=input("Press 0 to continue and 1 to quit:")
    if z=="1":
        break
        
