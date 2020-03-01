


def minimumSwaps(arr):
    count_swaps = 0
    i = 0
    while(i<len(arr)-1):
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i],arr[temp - 1] = arr[temp - 1],arr[i]
            count_swaps += 1
        else:
            i += 1
    return count_swaps








with open("input.txt","r") as fp:
    data = fp.read()

data = data.split("\n")

data = data[1].split(" ")
data = [int(i) for i in data]

print(minimumSwaps(data))

arr= [4, 3, 1, 2]
print(minimumSwaps(arr))

