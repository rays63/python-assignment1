def calculate(op1):
    if "+" in op1:
        num_list = op1.split("+")
        while '' in num_list:
            num_list.remove('')
        while " " in num_list:
            num_list.remove(' ')
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] + space_stripped[1]
        print("{} + {} = {}".format(space_stripped[0], space_stripped[1], result))

    elif "/" in op1:
        num_list = op1.split("/")
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] / space_stripped[1]
        print("{} / {} = {}".format(space_stripped[0], space_stripped[1], result))

    elif "*" in op1:
        num_list = op1.split("*")
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] * space_stripped[1]
        print("{}  * {} = {}".format(space_stripped[0], space_stripped[1], result))

    elif "-" in op1:
        num_list = op1.split("-")
        strip_lst = [num.strip() for num in num_list]
        while strip_lst[0] == '' in strip_lst:
            strip_lst.remove('')
            strip_lst[0] = int(strip_lst[0]) * -1
            strip_lst[0] = str(strip_lst[0])
        while strip_lst[1] == "" in strip_lst:
            strip_lst.remove('')
            strip_lst[1] = int(strip_lst[1]) * -1
            strip_lst[1] = str(strip_lst[1])
        space_stripped = [int(num) for num in strip_lst]
        result = space_stripped[0] - space_stripped[1]
        print("{} - {} = {}".format(space_stripped[0], space_stripped[1], result))
    else:
        print('Invalid input')


print("For addition enter expression : a + b")
print("For substraction enter expression : a - b")
print("For muliplication enter expression : a * b")
print("For division enter expression : a / b")

data = input('Enter Operation: ')

calculate(data)
