# Challenge 2
#Number machine

def reverse(number):
    d_input= 0
    d_output = 0
    
    while (number>0):
        d_input = number%10
        d_output = d_output*10+d_input
        number=int(number/10) 
    return d_output 

def gen_new (num):
    while True:
        final = str(num)
        if len(str(num))==5:
            first = int(final[0])
            second = int(final[-4])
            third = int(final[-3])
            fourth = int(final[-2])
            last = int(final[-1])
            addition = str(first + 1)+""+str(second + 1)+""+str(third + 1)+""+str(fourth + 1)+""+str(last + 1)
            print("The new number after adding 1 to each digit =",addition)
            break
        elif len(str(num))>5:
            
            first = int(final[0])
            second = int(final[-5])
            third = int(final[-4])
            fourth = int(final[-3])
            last = int(final[-2])
            other = int(final[-1])
            addition = str(first + 1)+""+str(second + 1)+""+str(third + 1)+""+str(fourth + 1)+""+str(last + 1)+""+str(other + 1)
            print("The new number after adding 1 to each digit =",addition)
            break
        else:
            print("Catch-All Error")

            
number = int(input("Enter 5 digit number:  "))
while True:
    if len(str(number))!=5:
        number = int(input("Enter 5 digit number:  "))
    elif len(str(number))==5:
        number = int(number)
        rev=reverse(number)
        print("Before the tranformation the digit number was : ", number)
        print("Reverse number is: ", rev)
        
        
        num = rev + number
        num = int(num)
        print("The sum of the digit number:", rev,'+', number,'=',num)
        gen_new(num)
        break
    else:
        print("Catch-All Error")