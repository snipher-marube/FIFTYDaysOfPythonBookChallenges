# separate the figures as a thousand
def separate_thousand(num):
    num = str(num)
    if len(num) <= 3:
        return num
    else:
        return separate_thousand(num[:-3]) + ',' + num[-3:]

# get the input
print('Please input the number of figures you want to separate as a thousand:')
num = int(input())

# output the result
print(separate_thousand(num))
