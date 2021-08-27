dict_A = {}
dict_B = {}
the_Numbers, the_Pure_Num = [],[]

def inputs():
    print("How many prefix do you want to give for |OPERATOR A| :")
    count_A = int(input())
    print("Please input a total of ",count_A," prefix and prices separated by space")
    for x in range(0, count_A):
        data = input().split(' ')
        dict_A[data[0]] = float(data[1])
    

    print("How many prefix do you want to give for |OPERATOR B| :")
    count_B = int(input())
    print("Please input a total of ",count_B," prefix and prices separated by space")
    for y in range(0, count_B):
        data = input().split(' ')
        dict_B[data[0]] = float(data[1])

    ## Here we will find the highest key
    list_keys_A = list(dict_A.keys())
    list_keys_B = list(dict_B.keys())
    list_value_A = list(dict_A.values())
    list_value_B = list(dict_B.values())
    temp_list = list_keys_A + list_keys_B

    
    longest_prefix = len(str(max(temp_list, key = len)))
    #print(longest_prefix)

    print("How many numbers do you want to calculate the prices for: ")
    total_Number = int(input())

    print("Please input the numbers followed by the enter key:")

    for x in range(0, total_Number):
        numbers = input()
        the_Numbers.append(numbers)
    

    for y in the_Numbers:
        pure_num = ''.join(filter(str.isalnum, y))
        the_Pure_Num.append(pure_num)

    # print (the_Pure_Num)
    # print(list_keys_A)
    # print(list_keys_B)

    for j in range (0, len(the_Pure_Num)):
        number(the_Pure_Num[j], longest_prefix, list_keys_A, list_keys_B, temp_list, list_value_A, list_value_B)




def number(mainNum, longest_prefix, list_keys_A, list_keys_B, templist, list_value_A, list_value_B):
    opNum = mainNum[:longest_prefix]
    for i in range(0,longest_prefix):
        if len(opNum) == 1 and opNum not in templist:
            print("No Operator Found for number", mainNum)
        if opNum in templist:
            if opNum in list_keys_A and opNum in list_keys_B:
                # print("The ", opNum,"is provided by both OP")
                index1 = list_keys_A.index(opNum)
                comp1 = list_value_A[index1]
                index2 = list_keys_B.index(opNum)
                comp2 = list_value_B[index2]
                if comp1 > comp2:
                    print("The Code of the num *",mainNum, "* is +",opNum,"provided by Operator A the cheaper cost of *",comp1, "*")
                if comp1 < comp2:
                    print("The Code of the num *",mainNum, "* is +",opNum,"provided by Operator A the cheaper cost of *",comp2, "*")
                if comp1 == comp2:
                    print("The Code of the num *",mainNum, "* is +",opNum,"provided by both operators at the same cost of *",comp2, "*")
                break

            if opNum in list_keys_A and opNum not in list_keys_B:
                # print("The ",opNum," is provided by OP A")
                index = list_keys_A.index(opNum)
                print("The Code of the num *",mainNum, "* is +",opNum,"provided only by Operator A at cost *",list_value_A[index], "*")
                break

            if opNum in list_keys_B and opNum not in list_keys_A:
                # print("The",opNum," is provided by OP B") 
                index = list_keys_B.index(opNum)  
                print("The Code of the num *",mainNum, "* is +",opNum,"provided only by Operator B at cost *",list_value_B[index], "*")
                
                break
        elif len(opNum) != 0: 
            opNum = opNum[:-1]
        

    # print("Done for the number ", mainNum)ś
inputs()
