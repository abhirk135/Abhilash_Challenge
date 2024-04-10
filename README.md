# Abhilash_Challenge

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers

4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
Input Format

The first line of input contains an integer N .
The next N lines contain credit card numbers.

Constraints
0 < N < 100

Output Format

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.