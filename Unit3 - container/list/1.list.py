digits = [1, 8, 2, 8]

len(digits)
#4

digits[3]
#8

[2, 7] + digits * 2
#[2,7,1,8,2,8,1,8,2,8]

pairs = [[10, 20], [30, 40]]

pairs[1]
#【30, 40】

pairs[1][0]
#30

#slicing
num = [1, 2, 3, 4, 5, 6]
start = num[:1]
middle = num[1:5]
end = num[5:]

