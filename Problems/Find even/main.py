end = int(input())

# for num in range(2, end):
#     if num % 2 == 0:
#         print(num)
num = 2
while num < end:
    if num % 2 == 0:
        print(num)
    num += 1
    if num == end:
        break

