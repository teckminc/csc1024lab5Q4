'''
Do not remove any text from these comments
4.	Write a Python program using the while loop to get an input of five numbers from the user, then store the input into a list called my_list in incremental order. Lastly, delete the content of my_list one by one in decremental order. Except for append()and del, do not use the built-in list functions to complete the task.

my_list = []
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
my_list = [1.0, 2.0, 3.0, 4.0, 5.0]
my_list = [1.0, 2.0, 3.0, 4.0]
my_list = [1.0, 2.0, 3.0]
my_list = [1.0, 2.0]
my_list = [1.0]
my_list = []

Function to use: float(), input(), print(), list.append(), list.sort()
Keyword: del
Operators: <=, +, -
Structure: while
'''
def main():
    my_list = []
    count = 1
    while count <= 5:
        num = float(input("Enter a number: "))
        my_list.append(num)
        count = count + 1

    my_list.sort()
    print("my_list =" , my_list)
    return 0


