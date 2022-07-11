def password(letters, numbers, special, capitals, password_length=8):
    '''
    --------------------------------------------------------------------------------------------------------------------
    A short function that returns a random alphanumerical string using the numpy random function
    :param letters: abc ('y' or 'n')
    :param numbers: 123 ('y' or 'n')
    :param special: !@# ('y' or 'n')
    :param capitals: ABC ('y' or 'n')
    :param password_length: (any number)
    :return: A random string containing all selected options (caps special characters etc.) of length password_length
    --------------------------------------------------------------------------------------------------------------------
    *Note due to the way character pools are set up numbers are twice as likely in passwords containing both
    letters and capitals. This is to help balance the results and compensate for letters effectively having 2
    chances to be selected as they are represented twice as both 'letters' and 'capitals'. Feel free to adjust
    the weightings yourself.
    --------------------------------------------------------------------------------------------------------------------
    '''
    from numpy import random
    # Debug
    # print("letters =",letters,'\n'"numbers =",numbers, '\n'"special characters =",special, '\n'"capitals =",capitals)
    # print("****************************************")
    result = []
    valid = ['y', 'n']
    cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    spec = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '.', '<', '>', '!', '@', '#', '$', '%', '^', '&', '*', '/',
            '.', '<', '>', '+', '+']
    cap_let = cap + let
    cap_let_num = cap + let + num + num
    cap_let_spec = cap + let + spec
    cap_num = cap + num
    cap_num_spec = cap + num + spec
    cap_spec = cap + spec
    let_num = let + num
    let_num_spec = let + num + spec
    let_spec = let + spec
    num_spec = num + spec
    num_let_spec_cap = num + let + spec + cap
    pass_len = password_length
    # Filter out invalid inputs
    if letters not in valid:
        return print("Error! Invalid input! please enter 'y' for yes or 'n' for no ")
    if numbers not in valid:
        return print("Error! Invalid input! please enter 'y' for yes or 'n' for no ")
    if special not in valid:
        return print("Error! Invalid input! please enter 'y' for yes or 'n' for no ")
    if capitals not in valid:
        return print("Error! Invalid input! please enter 'y' for yes or 'n' for no ")

    # Allocated random input from appropriate pool of possible symbols based on input.
    else:
        if letters == 'y' and numbers == 'y' and special == 'y' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(num_let_spec_cap))

        if letters == 'y' and numbers == 'y' and special == 'y' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(let_num_spec))

        if letters == 'y' and numbers == 'y' and special == 'n' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap_let_num))

        if letters == 'y' and numbers == 'n' and special == 'y' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap_let_spec))

        if letters == 'n' and numbers == 'y' and special == 'y' and capitals == 'y':
            for i in range(10):
                result.append(random.choice(cap_num_spec))

        if letters == 'y' and numbers == 'n' and special == 'n' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap_let))

        if letters == 'n' and numbers == 'y' and special == 'n' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap_num))

        if letters == 'n' and numbers == 'n' and special == 'y' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap_spec))

        if letters == 'y' and numbers == 'y' and special == 'n' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(let_num))

        if letters == 'y' and numbers == 'n' and special == 'y' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(let_spec))

        if letters == 'n' and numbers == 'y' and special == 'y' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(num_spec))

        if letters == 'y' and numbers == 'n' and special == 'n' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(let))

        if letters == 'n' and numbers == 'y' and special == 'n' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(num))

        if letters == 'n' and numbers == 'n' and special == 'y' and capitals == 'n':
            for i in range(pass_len):
                result.append(random.choice(spec))

        if letters == 'n' and numbers == 'n' and special == 'n' and capitals == 'y':
            for i in range(pass_len):
                result.append(random.choice(cap))
        if letters == 'n' and numbers == 'n' and special == 'n' and capitals == 'n':
            print("invalid entry please select 'y' for at least one variable")

        return result
    '''Written by Hugo Turbill 11/07/2022'''
