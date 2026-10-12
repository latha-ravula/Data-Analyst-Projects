History_File='history.txt'
def show_history():
    file=open(History_File,'r')
    Lines=file.readlines()
    if len(Lines)==0:
        print('No history found!')
    else:
        for line in reversed(Lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(History_File,'w')
    file.close()
    print("History cleared")    

def save_history(equation,result):
    file=open(History_File,'a')
    file.write(equation + "=" + str(result)+ "\n")
    file.close()

def Calculate(user_input):
    parts=user_input.split()
    if len(parts) !=3:
        
        print('Invalid input. Use format: number operator number (e.g 8 * 8)\n')
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    
    if op=="+":
        result=num1+num2
    elif op=="-":
         result=num1- num2
    elif op=="*":
         result=num1 * num2  
    elif op== "/":
        if num2==0:
            print("Cannot divide by zero")
            return
        result=num1 /num2  
    else:
        print("Invalid operator. USE ONLY + - * /.")    
        return
    
    if int(result) == result:
        result=int(result)
    print("Result :",result)
    save_history(user_input,result)

def Main():
    print("------SIMPLE CALCULATOR (type history,clear,exit)")    
    while True:
        user_input=input("Enter calculator (+ - * /) or command (history,clear,exit)")
        if user_input =='exit':
            print("Goodbye")
            break
        elif user_input =='history':
            show_history()
        elif user_input =='clear':
            clear_history()
        else:
            Calculate(user_input)
Main()