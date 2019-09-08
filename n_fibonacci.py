def n_fibonacci():
    num_n = int(input("The N-parameter is: "))
    num_m = int(input("The M-parameter is: "))
    to_print = []
    if num_n == 0 or num_n == 1:
        for i in range(num_m):
            to_print.append(0)
    else:
        for i in range(num_n - 1):
            to_print.append(0)
        to_print.append(1)
        num = 0
        for o in range(num_m - num_n):
            for i in range(num_n):
                index = len(to_print) - 1 - i
                nums = to_print[index]
                num += nums
            to_print += [num]
            num = 0
    sequence = to_print[:num_m]
    return(sequence)


print(n_fibonacci())
