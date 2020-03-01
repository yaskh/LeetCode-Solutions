
def minimumSwaps1(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != i+1 :
            temp = arr[i]
            arr[temp - 1] = temp
            arr[i] = i + 1
            count += 1
    for i in range(len(arr)):
        try:
            if arr[i]>arr[i+1]:
                print(False)
        except:
            print(i)
    return count

def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] != i+1:
            tmp = arr[i]
            arr[i] = arr[tmp-1]
            arr[tmp - 1] = arr[i]
            numSwaps += 1
            pass
        else:
            i += 1
    return numSwaps

# with open("input.txt","r") as fp:
#     data = fp.read()
#
# data = data.split("\n")
#
# data = data[1].split(" ")
# data = [int(i) for i in data]
#
# print(minimumSwaps(data))

arr= [4, 3, 1, 2]
print(minimumSwaps(arr))

