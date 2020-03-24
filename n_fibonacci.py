def n_fibonacci():
    base = int(input("On how many previous numbers is the next one based? "))
    length = int(input("How many numbers do you want to print? "))
    to_print = []
    if base == 0 or base == 1:
        for i in range(length):
            to_print.append(0)
    else:
        for i in range(base - 1):
            to_print.append(0)
        to_print.append(1)
        num = 0
        for o in range(length - base):
            for i in range(base):
                index = len(to_print) - 1 - i
                nums = to_print[index]
                num += nums
            to_print += [num]
            num = 0
    sequence = to_print[:length]
    return sequence


print(n_fibonacci())
