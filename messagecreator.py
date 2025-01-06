#This script writes a single input given number of time in message.txt. 
with open ('message.txt', 'w') as f:
    I=input("Enter your message: ")
    n= int(input("Enter the number of times you want to send: ")
    for i in range (n):
        f.write(I +"\n")

