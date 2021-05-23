# Enter two numbers and an opperator

def calculator(number1,number2,opperator):
    
    while True:
    
        if opperator=="+":
            return (number1+number2)
    
        elif opperator=="-":
            return (number1-number2) 
        
        elif opperator=="*":
            return (number1*number2) 
     
        elif opperator=="/" and number2==0:
            return ("Not divisible!")
        
        elif opperator=="/":
            return (number1/number2) 
        
        else:
            print("Try again")
            break
            
def main():
    number1=int(input("Enter first number: "))
    number2=int(input("Enter second number: "))
    opperator=input("Choose an opperator between '+','-','*','/': ")
    
    print(calculator(number1,number2,opperator))
    
if __name__ == '__main__':
    main()    
