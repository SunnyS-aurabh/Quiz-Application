def get_valid_option(st):
    """Function to repeatedly prompt the user until a valid option is chosen."""
    while True:
        opt = input("Enter the option!").upper()
        if opt == "":  # If the user presses Enter without selecting an option
            print("\nYou must select an option! Please enter A, B, C, or D.")
        elif opt in st:  # Check if the option is valid
            return opt
        else:
            print("\nEnter from the given options only! Please select A, B, C, or D.")

def get_user_name():
    """Function to prompt the user for a name until it's valid (not empty)."""
    while True:
        name = input("\nPlease Enter Your Name: ").strip()
        if name == "":  # Ensure the name is not empty
            print("Name cannot be empty. Please enter a valid name.")
        else:
            return name

# Main code execution
print("Welcome to the Quiz Application!")
print("Rules:")
print("- Each question has 4 options.")
print("- Enter the option (A, B, C, D) as your answer.")
print("\nPress Enter to Start!")
_ = input()

# Ensure the user presses Enter to start
while _ != "":
    _ = input("\nWrong Key Pressed! Please Press Enter to Start.")

# Get a valid user name
name = get_user_name()

if _ == "":  # If Enter is pressed, start the quiz
    try:
        with open("questions.txt", "r") as f:
            qno = 1
            c = 0  # Correct answers counter
            for l in f:
                arr = l.strip().split(",")
                print(f"\nQuestion {qno}: {arr[0]}")
                qno += 1
                ono = 0
                st = ""  # To hold valid options (A, B, C, D)
                for j in range(1, len(arr)-1):
                    print(f"{chr(65 + ono)}. {arr[ono + 1]}")  # Print the options A, B, C, D
                    st += chr(65 + ono)  # Collect valid options (A, B, C, D)
                    ono += 1
                
                # Get a valid option from the user
                opt = get_valid_option(st)
                
                print("Your Answer:", opt)
                
                # Check if the answer is correct
                if opt == arr[-1]:
                    print("\nCorrect!")
                    c += 1
                else:
                    print("\nIncorrect!")
                
                nxt = input("Press any key to continue...")
    
        # After quiz completes, show the score
        print("\nQuiz Complete!")
        print(f"Your Score: {c}/5")
        
        # Save the score in the file
        with open("scores.txt", "a") as f:
            f.write(f"{name},{c}/5\n")
            
    
    except FileNotFoundError:
        print("Error: The questions.txt file is missing.")
    except IOError as e:
        print(f"Error while handling files: {e}")
