'''
user_string = input('Please enter a string: ')
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

str_length = len(user_string)
mid_index = int(str_length / 2)

mid_char = user_string[mid_index]
result_str = first_char + mid_char + last_char
print(result_str)
'''
# Question 2
'''
input_str = input('Please enter a string: ')
print(input_str)
mid_index = int(len(input_str)/2)

res_str = input_str[mid_index-1:mid_index+2]
print(res_str)
'''
# Question 3
'''
input_str1 = input('Please enter the first string: ')
input_str2 = input('Please enter the second string: ')

print(input_str1)
mid_index = int(len(input_str1)/2)

first_half = input_str1[:mid_index:1]

first_half = first_half + input_str2

final_str = first_half + input_str1[mid_index:]

print(final_str)
'''
# Question #4
'''
input_str = input('Please enter a string: ')
print(input_str)
reverse_str = input_str[::-1]
print(reverse_str)
'''

# Question 5
# "The total value of 10 products purchased along with the tas is 150"
 given_str = "The total value of 10 products purchased along with the tas is 150"
 print(given_str[-3:])
