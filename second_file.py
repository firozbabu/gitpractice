arr = [6,3,6,0,1,5,5,6,2,23,64,12,434]
for i in range(len(arr)):
	for j in range(len(arr)-1):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)


arr = [6,3,6,0,1,5,5,6,2,23,64,12,434]
for i in range(len(arr)):
	for j in range(len(arr)-1):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)