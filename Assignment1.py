#qs1 

amount_1=100.00
amount_2=80.00
amount_3=10.00
amount_4=50.00

change1=round(amount_1-36.57, 2)
print("\nThe amount tendered is $100, the cost is $36.57")
print('change1:',change1)
num50=change1//50 
change1=change1-50*num50  #in case there were more 50s
print("numbers of fifties:",num50)
num20=change1//20
change1=change1-20*num20
print("numbers of 20s:",num20)
num10=change1//10
change1=change1-10*num10
print("number of 10s:",num10)
num5=change1//5
change1=change1-5*num5
print("number of 5s:",num5)
num1=change1//1
change1=change1-1*num1
print("number of 1s:",num1)
num025=change1//0.25
change1=change1-0.25*num025 # 25cent
print("number of 0.25s:",num025)
num010=change1//0.10 
change1=change1-0.10*num010
print("number of 0.10s:",num010)
num005=change1//0.05
change1=change1-0.05*num005
print("number of 0.05s:",num005)
num001=change1//0.01
print("number of 0.01s:",num001)


#$80 tendered, $64.09 cost 
print("\nThe amount tendered is $80, the cost is $64.09")


change2= round(amount_2-64.09, 2)
print('the change is:',change2)
num50=change2//50
change2=change2-50*num50   #in case there were more than 1 50
print("numbers of fifties:",num50)
num20=change2//20
change2=change2-20*num20
print("number of 20s:",num20)
num10=change2//10
change2=change2-10*num10 
print("number of 10s:",num10)
num5=change2//5
change2=change2-5*num5
print("number of 5s:",num5)
num1=change2//1
change2=change2-1*num1
print("number of 1s:",num1)
num025=change2//0.25
change2=change2-0.25*num025 # 25cent
print("number of 0.25s:",num025)
num010=change2//0.10 
change2=change2-0.10*num010
print("number of 0.10s:",num010)
num005=change2//0.05
change2=change2-0.05*num005
print("number of 0.05s:",num005)
num001=change2//0.01
print("number of 0.01s:",num001)


print("\nThe amount tendered is $10, the cost is $3.81")


change3=round(amount_3-3.81, 2)
print('the change is:',change3)
num50=change3//50
change3=change3-50*num50   #in case there were more than 1 50
print("numbers of fifties:",num50)
num20=change3//20
change3=change3-20*num20
print("number of 20s:",num20)
num10=change3//10
change3=change3-10*num10 
print("number of 10s:",num10)
num5=change3//5
change3=change3-5*num5
print("number of 5s:",num5)
num1=change3//1
change3=change3-1*num1
print("number of 1s:",num1)
num025=change3//0.25
change3=change3-0.25*num025 # 25cent
print("number of quarters:",num025)
num010=change3//0.10 
change3=change3-0.10*num010
print("number of dimes:",num010)
num005=change3//0.05
change3=change3-0.05*num005
print("number of nickeles:",num005)
num001=change3//0.01
print("number of cents:",num001)


print("\n The amount tendered is $50, the cost is $14.36")


change4=round(amount_4-14.36, 2)
print('the change is:',change4)
num50=change4//50
change4=change4-50*num50   #in case there were more than 1 50
print("numbers of fifties:",num50)
num20=change4//20
change4=change4-20*num20
print("number of 20s:",num20)
num10=change4//10
change4=change4-10*num10
print("number of 10s:",num10)
num5=change4//5
change4=change4-5*num5
print("number of 5s:",num5)
num1=change4//1
change4=change4-1*num1
print("number of 1s:",num1)
num025=change4//0.25
change4=change4-0.25*num025 # 25cent
print("number of quarters:",num025)
num010=change4//0.10 
change4=change4-0.10*num010
print("number of dimes:",num010)
num005=change4//0.05
change4=change4-0.05*num005
print("number of nickeles:",num005)
num001=change4//0.01
print("number of cents:",num001)


########2nd part of the assignment#######################
first_name="linus"
middle_name="Benedict"
even_letters=middle_name[1::2]   #gives the even letters of the middle
last_name="Torvalds"
phone="(317)-555-1969"
print("\n\n Student: ",first_name,middle_name,last_name," Phone: ",phone,"\nUsername: ",last_name[0:6]+first_name[0]+middle_name[0],)
print("\nPassword: ",first_name[0:2]+even_letters[0:3]+phone[-4::],"\n\n")  
first_name="Alan"
middle_name="Mathison"
even_letters=middle_name[1::2]
last_name="Turing"
phone="(317)-555-5346"
print("\n\n Student: ",first_name,middle_name,last_name," Phone: ",phone,"\nUsername: ",last_name[0:6]+first_name[0]+middle_name[0],)
print("\nPassword: ",first_name[0:2]+even_letters[0:3]+phone[-4::],"\n\n")
first_name="Stephan"
middle_name="Gary"
even_letters=middle_name[1::2] 
last_name="Wozniak"
phone="(317)-555-3720"
print("\n\n Student: ",first_name,middle_name,last_name," Phone: ",phone,"\nUsername: ",last_name[0:6]+first_name[0]+middle_name[0],)
print("\nPassword: ",first_name[0:2]+even_letters[0:3]+phone[-4::],"\n\n")
first_name="Adele"
middle_name=" "
last_name="Goldberg"
phone="(317)-555-2345"
print("\n\n Student: ",first_name,middle_name,last_name," Phone: ",phone,"\nUsername: ",last_name[0:6]+first_name[0]+middle_name[0],)
print("\nPassword: ",first_name[0:2]+phone[-4::],"\n\n")
