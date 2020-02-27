def sockMerchant(n, ar):
    sock_dict = {}
    for i in range(n):
        value = ar[i]
        if value in sock_dict.keys():
            sock_dict[value] += 1
        else:
            sock_dict[value] = 1
    res = 0
    for value in sock_dict.keys():
        res += sock_dict[value] // 2
    return  res

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(len(arr),arr))