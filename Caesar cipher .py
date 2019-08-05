def to_encrypt(text, delta):
    # a-z 97 - 122 , i > 122 = - 26 , i < 97 = + 26
    aa = []
    for i in text:
        if i.isalpha():
            aa.append(ord(i))
        else:
            aa.append(i)

    bb = []
    for j in aa :
        if type(j) is int :
            bb.append(j + delta)
        else:
            bb.append(j)

    gg =[]
    for t in bb:
        if type(t) is int:
            if t < 97 :
                gg.append(t + 26)   # stay in alphabit of ascii chart
            elif t > 122:
                gg.append(t - 26)   # stay in alphabit
            elif t >= 97 and t <= 122 :
                gg.append(t)
        else:
            gg.append(t)

    cc = []
    for o in gg :
        if type(o) is int :
            cc.append(chr(o))
        else:
            cc.append(o)

    return ''.join(cc)




to_encrypt("important text", 10)




