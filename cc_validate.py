import re

def validate_credit_card(card_number):
    # Define the regex pattern
    pattern = r'^[7-9]\d{3}(-?\d{4}-?){3}$|^4\d{3}(-?\d{4}-?){3}$|^3[0,6,8]\d{3}(-?\d{4}-?){3}$|^(\d{4}-){3}\d{4}$'
    
    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        # Check for consecutive repeated digits
        if not re.search(r'(\d)\1{3,}', card_number.replace("-", "")):
            return True
    
    return False

def main():
    N = int(input("Enter the number of credit card numbers: "))
    
    if not 0 < N < 100:
        print("Invalid input for N. N should be between 0 and 100.")
        return
    
    for _ in range(N):
        card_number = input("Enter the credit card number: ")
        
        if validate_credit_card(card_number):
            print("This is a valid credit card number.")
        else:
            print("This is not a valid credit card number.")

if __name__ == "__main__":
    main()