import time
import winsound

def alarm_at_fixed_time():
    """Mode 1: Alarm triggers at a specific clock time (HH:MM:SS)"""
    while True:
        alarm_time = input("Enter alarm time in HH:MM:SS format (e.g., 14:30:00): ")
        # Basic format validation
        try:
            time.strptime(alarm_time, "%H:%M:%S")
            break
        except ValueError:
            print("Invalid format. Please use HH:MM:SS with hours 00-23, minutes 00-59, seconds 00-59.")
    
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        now = time.strftime("%H:%M:%S")
        if now == alarm_time:
            print("\n🔔 ALARM! Time to wake up! 🔔")
            winsound.Beep(1000, 3000)   # Beep at 1000 Hz for 3 seconds
            break
        time.sleep(1)

def countdown_timer():
    """Mode 2: Alarm after a specified duration (hours/minutes/seconds)"""
    print("Enter the countdown duration:")
    try:
        h = int(input("Hours (0 if none): ") or "0")
        m = int(input("Minutes (0 if none): ") or "0")
        s = int(input("Seconds (0 if none): ") or "0")
    except ValueError:
        print("Invalid input. Using default 1 second.")
        h = m = 0
        s = 1

    total_seconds = h * 3600 + m * 60 + s
    if total_seconds <= 0:
        total_seconds = 1
        print("No valid duration entered. Setting alarm for 1 second.")

    print(f"⏰ Timer started: {h} hour(s), {m} minute(s), {s} second(s).")
    print(f"Waiting {total_seconds} seconds...")
    time.sleep(total_seconds)
    print("\n🔔 TIME'S UP! 🔔")
    winsound.Beep(1000, 3000)

def main():
    print("========== ALARM & REMINDER SYSTEM ==========")
    print("Choose an option:")
    print("1. Alarm at a fixed clock time ")
    print("2. Countdown timer")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        alarm_at_fixed_time()
    elif choice == '2':
        countdown_timer()
    else:
        print("Invalid choice. Please run the program again and enter 1 or 2.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user. Goodbye!")


