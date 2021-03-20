def calculate(op1):
    if "+" in op1:
        num_list = op1.split("+")
        while '' in num_list:
            num_list.remove('')
        while " " in num_list:
            num_list.remove(' ')
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] + space_stripped[1]
        print("{} = {}".format(op1, result))

    elif "/" in op1:
        num_list = op1.split("/")
        while '' in num_list:
            num_list.remove('')
        while " " in num_list:
            num_list.remove(' ')
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] / space_stripped[1]
        print("{} = {}".format(op1, result))

    elif "*" in op1:
        num_list = op1.split("*")
        while '' in num_list:
            num_list.remove('')
        while " " in num_list:
            num_list.remove(' ')
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] * space_stripped[1]
        print("{} = {}".format(op1, result))

    elif "-" in op1:
        num_list = op1.split("-")
        while '' in num_list:
            num_list.remove('')
        while " " in num_list:
            num_list.remove(' ')
        space_stripped = [int(num.strip()) for num in num_list]
        result = space_stripped[0] - space_stripped[1]
        print("{} = {}".format(op1, result))

    else:
        print('Invalid input')


data = input('Enter Operation: ')

calculate(data)