#given the arrival and departure time of all trains that reach a railway station,
#find the minimum number of platforms required for the railway station so that no train waits.
#We are given two arrays which represent arrival and departure times of trains that stop.
# arr = ['900', '940', '950', '1100', '1500', '1800']
# dep = ['910', '1200', '1120', '1130', '1900', '2000']
arr = []
dep = []
count = 1
n = int(input("Enter number of trains: "))
for i in range(n):
    a = input("Enter arrival time: ")
    arr.append(a.replace(":", ""))
    d = input("Enter departure time: ")
    dep.append(d.replace(":", ""))
zip(*sorted(zip(arr, dep)))
print(arr)
print(dep)    
for i in range(n-1):
    for j in range(i):
        if i != j and arr[i] < arr[j]:
            if arr[i] < dep[j]:
                count += 1
                break

print(count)
