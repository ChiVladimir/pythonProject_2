numbers_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pairs_4_pswd = []
for k in numbers_1:
    for m in range (1, 20):
        for n in range (1, 20):
            #print(k, m, n)
            j = n + m
            if m >= n:
                #print(n, ">", m)
                continue
            elif k % j == 0:
                #print (k, ' кратно сумме', m, "+", n, "=", j)
                pairs_4_pswd.append(m)
                pairs_4_pswd.append(n)
    print(k, pairs_4_pswd)
    pairs_4_pswd.clear()