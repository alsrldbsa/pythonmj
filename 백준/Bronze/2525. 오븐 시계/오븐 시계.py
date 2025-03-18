hour,min = map(int,input().split())
cookt = int(input())
alltime = int(min + cookt)

if cookt < 60:
    min = min + cookt
    if min >= 60:
        hour = hour + 1
        min = min - 60
else:
    min = alltime % 60
    hour = hour + (alltime // 60)


if hour >= 24:
		hour = hour - 24


print(hour, min)