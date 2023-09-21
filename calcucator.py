def check_correct_input(str):
    allowed_characters = set('0123456789+-*/()^.')

    if all(char in allowed_characters for char in str):
        return True
    else:
        return False
    
def check_parantheses(str):
    parantheses_stack = []
    substring_list = []
    substring_start = None

    for i, char in enumerate(str):
        if char == '(':
            if not parantheses_stack:
                substring_start = i
            parantheses_stack.append('(')
        elif char == ')' and parantheses_stack:
            parantheses_stack.pop()
            if not parantheses_stack:
                substring = "".join(substring_list)
                substring_list = []

                # result = 
                for j in range(substring_start, i + 1):
                    output_string = result
        elif parantheses_stack:
            substring_list.append(char)

def calculate(str):
    numbers_set = set('0123456789')
    arithmetic_signs_set = set('+-*/()^')
    numbers = []
    arithmetic_signs = []
    number = ''

    for i, char in enumerate(str):
        if char.isdigit():
            number += char
        elif char in arithmetic_signs_set:
            numbers.append(int(number))
            arithmetic_signs.append(char)
            number = ''
        elif i + 1 == len(str):
            numbers.append(int(number))
            number = ''

    numbers.append(int(number))

    for i, sign in enumerate(arithmetic_signs):
        if sign == '*':
            # value_to_replace = [numbers[i], numbers[i + 1]]
            numbers[i] = numbers[i] * numbers[i + 1]
            numbers.pop(i + 1)
            arithmetic_signs.pop(i)
        elif sign == '/':
            numbers[i] = numbers[i] / numbers[i + 1]
            numbers.pop(i + 1)
            arithmetic_signs.pop(i)

    result = numbers[0]
    numbers.pop(0)
    for i, sign in enumerate(arithmetic_signs):
        match sign:
            case '+':
                result += numbers[i]
            case '-':
                result -= numbers[i]

    return result
                





user_input = input('enter an algebraic expression: ')
# user_input = user_input.split(' ')
result = calculate(user_input)
print(result)
# check_result = check_correct_input(user_input)
# number_str = ''
# arithmetic_signs = set('+-*/()^.')
# first_number = None
# second_number = None
# arithmetic_sign = None
# result = None

# # 12+9/8
# if check_result:
#     for char in user_input:
#         if char.isdigit():
#             number_str += char
#         elif char in arithmetic_signs:
#             if first_number is None:
#                 first_number = int(number_str)
#             else:
#                 second_number = int(number_str)
                
#             arithmetic_sign = char

#         if arithmetic_sign is not None and result is None:
#             match arithmetic_sign:
#                 case "+":
#                     result += first_number + second_number
#                 case "-":
#                     result += first_number - second_number
#                 case "*":
#                     result += first_number * second_number
#                 case "/":
#                     result += first_number / second_number
#                 case "^":
#                     result += first_number ** second_number
