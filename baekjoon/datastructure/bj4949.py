# 균형잡힌 세계
while True:
    s = input()
    if s == ".": break   
    sol = [0]
    balanced = True 
    for c in s:
        if c == "(" or c == "[":
            sol.append(c)
        elif c == ")":
            if sol[-1] == "(": sol.pop()
            else:
                balanced = False
                break
        elif c == "]":
            if sol[-1] == "[": sol.pop()
            else:
                balanced = False
                break
    if balanced and sol[-1] == 0:
        print("yes")
    else:
        print("no")