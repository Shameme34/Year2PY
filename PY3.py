name = 'Shaik Dawood Shameem Ahamed'  # (1) REPLACE THE VARIABLE WITH YOUR NAME in string type
student_num = '7364283' # (2) REPLACE THIS VARIABLE WITH YOUR UOW ID in string type
subject_code = 'CSIT110'
# ========== (3) insert solution here========= # 

def x231(y) ->float:
    number1 = float(y)
    x = number1 * 231
    final_answer = round(x,1)
    return final_answer

def get_type(x):
    #Making y a variable to hold the data type of x
    y = type(x)
    return y

def get_equation():
    user_input1 = input("Enter first number:")
    #Converts user input to float rounded to 1 decimal place
    x = float(user_input1)
    x1 = round(x,1)
    user_input2 = input("Enter second number:")
    y = float(user_input2)
    y1 = round(y,1)
    sum_of = x1 + y1
    c = (f"{x1} + {y1}")
    #Returning the sum of x1 and y1 and returing a string to be inserted into a print statement
    return sum_of, c
    
def filter_by(fcn, N:int) ->bool:
    #Making fcn a variable to hold the function
    fcn = fcn()
    if (fcn>N):
        return True
    else:
        return False

def format_price(money:float) ->str:
    #Printing a value and returning a string such that it can be inserted into a print statement
    print(f"${money:<.2f} ")
    c = (f"${money:<.2f} ")
    #Prints the formatted price and also returns a str data type to be inserted into a print statement
    return c 
    

def main():  # do not change this line
    print("Assignment 1")  # do not change this line

    #Qn1
    x = x231(100.1)
    print(x)

    #Qn2
    print(get_type(123))
    print(get_type("hohoho"))

    #Qn3
    x,y = get_equation()
    print(x)
    print(y)

    #Qn4
    def test_fcn1():
        return 3*3
    x = filter_by(test_fcn1, 16)
    y = filter_by(test_fcn1, 4)
    print(x)
    print(y)

    #Qn5
    x = format_price(2.3)
    print(x)


if __name__ == '__main__':  # do not change this line
    main()  # do not change this line
