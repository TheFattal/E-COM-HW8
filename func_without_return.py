# a:
def my_ascending(num1, num2):
    """The function gets 2 integers and prints them with ascending order."""
    if num1 >= num2:
        print(f"The numbers in ascending order are:{num2}, {num1}")
    else:
        print(f"The numbers in ascending order are:{num1}, {num2}")


my_ascending(-12, 7)


# b:
def my_details(string1):  # Works well only with odd
    """The function gets a string and prints the first, the middle and the last chars."""
    char_list = list(string1)
    middle_char_index = len(char_list) // 2
    print(f"The first char in the list is: {char_list[0]}")
    print(f"The middle char in the list is: {char_list[middle_char_index]}")
    print(f"The last char in the list is: {char_list[-1]}")


my_details("Al is the best")


# c:
def say_bool(bool1):
    """The functions gets a bool and prints YES if it's TRUE otherwise NO."""
    if bool1 is True:
        print(f"YES")
    else:
        print(f"NO")


say_bool(True)
say_bool(False)


# d:
def zugi_print(numbers):
    """Function gets a list of integers and then prints EVEN or ODD for every element in the list."""
    func_list = []
    for number in numbers:
        if number % 2 == 0:
            func_list.append("even")
        else:
            func_list.append("odd")
    print(*func_list, sep=', ')


# Define the list of numbers
numbers_list = [5, 3, 2, 10, 15, 14, 14]
# Call the function with the list
zugi_print(numbers_list)


def my_statistics(grades):
    """The function do various statistics to grades - then prints"""
    import math
    min_grade: int = grades[0]
    max_grade: int = grades[0]
    grades_amount: int = len(grades)
    grades_avg: float = sum(grades) / grades_amount
    variance: float = sum((x - grades_avg) ** 2 for x in grades) / len(grades)
    std_dev: float = math.sqrt(variance)
    count_over_90: int = 0
    count_under_55: int = 0
    for grade in grades:
        if grade > max_grade:
            max_grade = grade
        if grade < min_grade:
            min_grade = grade
        if grade > 90:
            count_over_90 += 1
        if grade < 55:
            count_under_55 += 1
    print(f"max grade is:{max_grade}\nmin grade is:{min_grade}\namount of grades:{grades_amount}\naverage: {grades_avg:.2f}")
    print(f"Grades standard deviation is: {std_dev}")


stat = [1, 4, 6, 9, 100, 3.2323452345]
my_statistics(stat)
