#Input

print("Enter your array")

array = list(map(int, input().split()))

n = len(array)

#Sorting

for i in range(0,n):
    s = i
    c = i

    for j in range(s+1, n):
        if array[j] < array[s]:
            s = j

    temp = array[s]
    array[s] = array[c]
    array[c] = temp

#Output

for element in array:
    print(element, end = " ")
