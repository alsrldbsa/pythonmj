hour,min = map(int,input().split())

if hour > 0 and min >= 45:
	min = min - 45


elif hour == 0 and min < 45:
	hour = 23
	min = min + 15

elif hour > 0 and min<45: 
	hour = hour - 1
	min = min + 15

else :
	min = min - 45

print(hour, min)