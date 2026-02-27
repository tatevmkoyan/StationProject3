import time
print("Insert time to count down (h:m:s)")
hour = int(input())
minute = int(input())
second = int(input())

print("The countdown is activated")

while hour > 0 or minute > 0 or second > 0:
    print(f"{hour:02d}:{minute:02d}:{second:02d}")
    time.sleep(1)

    second -= 1

    if second < 0:
        second = 59
        minute -= 1

    if minute < 0:
        minute = 59
        hour -= 1

print("00:00:00")
print("Time's up!")