import time

def countdown_timer():
    print("=== Python Countdown Timer ===")
    print("Please insert the countdown duration:")
    
    try:
        hour = int(input("Hours:   "))
        minute = int(input("Minutes: "))
        second = int(input("Seconds: "))
        
    except ValueError:
        return

    if hour < 0 or minute < 0 or second < 0:
        print("\n[Error]: Time components cannot be negative. Please try again.")
        return

    extra_minutes, second = divmod(second, 60)
    minute += extra_minutes
    
    extra_hours, minute = divmod(minute, 60)
    hour += extra_hours

    if hour == 0 and minute == 0 and second == 0:
        print("\n[Error]: The timer cannot be set to zero total time.")
        return

    print(f"\nCountdown activated for {hour:02d}:{minute:02d}:{second:02d}!")
    print("Press Ctrl+C to stop the timer early.\n")
    time.sleep(1)

    try:
        total_seconds = hour * 3600 + minute * 60 + second

        while total_seconds >= 0:
            hrs = total_seconds // 3600
            mins = (total_seconds % 3600) // 60
            secs = total_seconds % 60

            timer_display = f"{hrs:02d}:{mins:02d}:{secs:02d}"
            print(f"\rTime Remaining: {timer_display}", end="", flush=True)

            if total_seconds == 0:
                break

            time.sleep(1)
            total_seconds -= 1

        print("\n\nTime's up! ⏰")

    except KeyboardInterrupt:
        print("\n\n[Cancelled]: Countdown stopped manually by user.")

if __name__ == "__main__":
    countdown_timer()
