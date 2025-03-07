#string concatenation
a="hello"
b="sadia"
print(a+b)
# + is used to cocatenate the two strings.
# for string concatenation must b same type of data type of both side of +.
#give error if we concatenate different data type .
#for the solution of error ,
#First we change the data type of the variable and than concatenate the string with tham
a="leptop price is"
b=50000
print(a+str(b)) #there we change the type of variable b into string 
#another mathod to change the data type 
a="the percentage of marks is"
b=75
print(f"{a}{b}") #use f-string mathod
print(f"{a}  {b}")  #we also cocatenate the space