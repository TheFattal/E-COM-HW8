import func_without_return
import inspect

scores = []

while True:
    user_input: int = int(input("Enter a score (or -99 to finish):"))
    try:
        score = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if score == -99:
        break

    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("Score out of range. Please enter a score between 0 and 100.")

func_without_return.my_statistics(scores)

# Printing all the function helps:
functions = inspect.getmembers(func_without_return, predicate=inspect.isfunction)
function_names = [name for name, func in functions]
for name in function_names:
    full_func_name = "func_without_return." + name
    print(f"{help(full_func_name)}:")
    print()  # Add a blank line between help outputs
help(func_without_return.my_statistics)
