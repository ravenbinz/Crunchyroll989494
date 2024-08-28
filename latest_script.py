import os
import time

def clear_terminal():
    os.system('clear')

def display_loading_bar(duration, color, message=""):
    steps = 10
    for i in range(steps + 1):
        time.sleep(duration / steps)
        completed = "■" * i
        remaining = "□" * (steps - i)
        percent = i * 10
        loading_bar = f"[{completed}{remaining}] {percent}%"
        print(f"\033[{color}m{loading_bar} {message}\033[0m", end="\r")
    print("")

def main():
    # Clear the terminal and show the welcome message
    clear_terminal()
    print("\033[1mWelcome To Akatsuki\033[0m")
    
    # Initial loading bar (15 seconds)
    display_loading_bar(15, "31")
    
    # Prompt for password
    password = input("Enter password: ")
    
    # Check the password
    if password == "fuad":
        # Clear the terminal and show another loading bar (7 seconds)
        clear_terminal()
        display_loading_bar(7, "32")
        
        # Show the final message
        print("\n\033[1mofuad3136@gmail.com:fuad123@#king\033[0m")
    else:
        print("\033[31mIncorrect password. Exiting...\033[0m")

if __name__ == "__main__":
    main()
  
