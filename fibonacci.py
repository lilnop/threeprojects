prev_num = 10
next_num = 12

output = "{},{},".format(prev_num, next_num)

while ((prev_num+next_num) < 200):
    new_val = prev_num+next_num
    output += "{},".format(new_val)
    prev_num = next_num
    next_num = new_val

output = output[:-1]
print(output)
