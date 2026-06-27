'''
Given a string of n words, help Alex to find out how many times his name
appears in the string.

Constraint: 1 <= n <= 200

Sample input: Hi Alex WelcomeAlex Bye Alex.
Sample output: 3
Explanation: Alex name appears 3 times in the string.
Hi Alex WelcomeAlex Bye Alex.
'''

def find(string):
    length = len('Alex')
    i = 0
    count = 0
    while i <= len(string) - len('Alex'):
        if string[i : i + length] == 'Alex':
            count += 1
            i += length
        else:
            i += 1

    return count

data = "Hi Alex WelcomeAlex Bye Alex."
print(find(data))