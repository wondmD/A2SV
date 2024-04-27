for tc in range(int(input())):
    word = input()
    res = []
    cap_pos = []
    sm_pos =[]
    for i in word:
        if i == 'B':
            if cap_pos:
                res[cap_pos.pop()] = ""
        elif i == 'b':
            if sm_pos:
                res[sm_pos.pop()] = ""
        else:
            if i.islower():
                sm_pos.append(len(res))
            else:
                cap_pos.append(len(res))
            res.append(i)
    print("".join(res[:]))