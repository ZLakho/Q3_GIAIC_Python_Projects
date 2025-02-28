import time

def countdown_timer(seconds):
    print("\n⏳ Countdown Timer Started! ⏳\n")
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = f"{hours:02}:{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print(" Time's up! ⏰")

print("Select time format:")
print("1. Seconds")
print("2. Minutes")
print("3. Hours")
choice = input("Enter your choice (1/2/3): ")

time_value = int(input("Enter the time value: "))

if choice == "2":
    time_value *= 60  
elif choice == "3":
    time_value *= 3600  

countdown_timer(time_value)