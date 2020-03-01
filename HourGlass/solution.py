def hourglassSum(arr):
    first= True
    max_sum = 0
    for j in range((len(arr)//2 )+1):
        for i in range((len(arr)//2 )+1):
            temp = 0
            temp+=int(arr[j][i])
            temp+=int(arr[j][i+1])
            temp+=int(arr[j][i+2])
            temp+=int(arr[j+1][i+1])
            temp+=int(arr[j+2][i])
            temp+=int(arr[j+2][i+1])
            temp+=int(arr[j+2][i+2])
            if first == True:
                max_sum = temp
                first = False
            if temp>max_sum:
                max_sum=temp
    return max_sum
if __name__ == '__main__':
    print("here")
    arr = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""
    arr = arr.split("\n")
    arr = [i.split(" ") for i in arr]
    print(arr)

    hourglassSum(arr)