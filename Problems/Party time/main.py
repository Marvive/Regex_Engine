line = None
friend_list = []
while line != ".":
    line = input()
    if line != ".":
        friend_list.append(line)

print(f"{friend_list}\n{len(friend_list)}")
