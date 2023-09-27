name = 'Shaik Dawood Shameem Ahamed'  # (1) REPLACE THE VARIABLE WITH YOUR NAME in string type
student_num = '7364283' # (2) REPLACE THIS VARIABLE WITH YOUR UOW ID in string type
subject_code = 'CSIT110'
# ========== (3) insert solution here========= # 

def hocuspocus(N):
    n = int(N)
    #List the number from 1 to end of input of the user
    number_list = list(range(1,n+1))
    for i in range (0, len(number_list)):
        if (number_list[i]%9==0 and number_list[i]%5==0):
            number_list[i] = "HocusPocus"
        elif (number_list[i]%5==0):
            number_list[i] = "Hocus"
        elif (number_list[i]%9==0):
            number_list[i] = "Pocus"
    print(number_list)
    return number_list

def question_2():
    user_input1 = input("Enter Current Age:")
    age = int(user_input1)
    user_input2 = input("Enter Current Amount in OA:")
    oa = float(user_input2)
    user_input3 = input("Enter Current Amount in SA:")
    sa = float(user_input3)
    user_input4 = input("Enter Current Amount in MA:")
    ma = float(user_input4)
    if (age < 55):
        #Multiplying the interest for each account
        newOA = oa*0.025
        newSA = sa*0.04
        newMA = ma*0.04
        #If more than 20000 in OA, only add the 20000 to the total extra interest
        if (oa>=20000):
            total = 20000 + sa + ma
            #If total exceeds 60000, only add the interest of 60000 to the total interest
            if (total>=60000):
                extra = 60000*0.01 + newOA + newSA + newMA
            else:
                extra = total*0.01 + newOA + newSA + newMA
        else:
            total = oa + sa + ma
            if (total>=60000):
                extra = 60000*0.01 + newOA + newSA + newMA
            else:
                extra = total*0.01 + newOA + newSA + newMA
    else:
        user_input5 = input("Enter Current Amount in RA:")
        ra = float(user_input5)
        newOA = oa*0.025
        newSA = sa*0.04
        newMA = ma*0.04
        newRA = ra*0.04
        if (oa>=20000):
            total = 20000 + sa + ma + ra
            #If total interest is less than 30000, add the interest of the total to the other interest
            #else if its between 30000 and 60000, get the interest of the first 30000 and then the interest of the remainder and add the rest of the interest
            #else if it exceeds 60000, the fixed interest becomes 30000*0.02 and 30000*0.01
            if (total<30000):
                extra = total *0.02  + newOA + newSA + newMA + newRA
            elif (total>=30000 and total<60000):
                subtracted = total - 30000
                extra = 30000*0.02 + subtracted * 0.01 + newOA + newSA + newMA + newRA
            elif (total>=60000):
                extra = 30000*0.02 + 30000*0.01 + newOA + newSA + newMA + newRA
        else:
            total = oa + sa + ma + ra
            if (total<30000):
                extra = total *0.02 + newOA + newSA + newMA + newRA
            elif (total>=30000 and total<60000):
                subtracted = total - 30000
                extra = 30000*0.02 + subtracted * 0.01  + newOA + newSA + newMA + newRA
            elif (total>=60000):
                extra = 30000*0.02 + 30000*0.01  + newOA + newSA + newMA + newRA
    format_extra = "{:.2f}".format(extra)
    print("Your interest rate this year will be $" , format_extra)


def question_3():
    user_input1 = input("Number of Single rooms: ")
    singlerm = int(user_input1)
    user_input2 = input("Number of Twin rooms: ")
    twinrm = int(user_input2)
    user_input3 = input("Number of Deluxe rooms: ")
    deluxrm = int(user_input3)
    user_input4 = input("Number of Suite: ")
    suite = int(user_input4)
    user_input5 = input("Length of stay(number of nights): ")
    stays = int(user_input5)
    print(end ='\n')
    print("Summary of your bookings for",stays,"night(s)")
    
    #Calculating the cost of each room
    scost = singlerm *90*stays
    tcost = twinrm *150*stays
    dcost = deluxrm *250*stays
    suitec = suite *1050*stays

    #Calculating the total number of rooms
    totalrms = singlerm + twinrm + deluxrm + suite

    #Calculating the total cost of all rooms with the gst and getting the formatted string needed to print
    totalCost = scost + tcost + dcost + suitec
    withGST = totalCost + (totalCost*0.07)
    room = "Single room"
    number = singlerm
    format_cost = (str)(format(scost,'.2f'))
    #adding the dollar sign to the string cost
    cost = "$"+format_cost
    print(f"{room:<13}{number:^3}{cost:>10}")

    room = "Twin room"
    number = twinrm
    format_cost = (str)(format(tcost,'.2f'))
    cost = "$"+format_cost
    print(f"{room:<13}{number:^3}{cost:>10}")

    room = "Deluxe room"
    number = deluxrm
    format_cost = (str)(format(dcost,'.2f'))
    cost = "$"+format_cost
    print(f"{room:<13}{number:^3}{cost:>10}")

    room = "Suite"
    number = suite
    format_cost = (str)(format(suitec,'.2f'))
    cost = "$"+format_cost
    print(f"{room:<13}{number:^3}{cost:>10}")

    number = totalrms
    format_cost = (str)(format(totalCost,'.2f'))
    cost = "$"+format_cost
    print(f"{'Subtotal':<13}{number:^3}{cost:>10}")

    number = totalrms
    format_cost = (str)(format(withGST,'.2f'))
    cost = "$"+format_cost
    print(f"{'Total(7% g.s.t)':<16}{cost:>10}")
    
def recover_files() ->str:
    #Making fcn a variable to hold the function
    filename =""
    while True:
        user_input = input ("Filename?")
        if (user_input ==""):
            break
        clean =""
        bad = 0

        #Scanning th string the user have typed and for each "{" it adds a positive and does not include to the new string
        #It is only included in the new string once the value of bad = 0 
        for c in user_input:
            if c == '{':
                bad+=1
            elif c == "}":
                bad -=1
            elif bad ==0:
                clean +=c
        
        if(filename ==""):
            filename = filename + clean
        else:
            filename = filename + ","+ clean
    return filename

    

def main():  # do not change this line
    print("Assignment2")  # do not change this line
    # (4)test code here

    #Qn1
    x = hocuspocus(45)

    #Qn2
    question_2()

    #Qn3
    question_3()

    #Qn4
    x = recover_files()
    print(x)



if __name__ == '__main__':  # do not change this line
    main()  # do not change this line
