lst=[1,5,9,19,27,30]
s=int(input("Enter: "))
first=0
last=len(lst)-1
mid = int((first+last)/2)
while first<=last:
	if lst[mid]==s:
		print("Pos=", mid)
		break
	elif lst[mid]<s:
		first=mid+1
	else:
		last=mid-1
	mid=int((first+last)/2)
else:
	print("not present")