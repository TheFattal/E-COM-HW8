import func_with_return
import inspect

avg1 = func_with_return.my_avg(90, 99)
print(f"The average of 90 and 99 is: {avg1}")

head1 = func_with_return.my_headline("python has concurred the world")
print(f"The new string is:\n{head1}\n{head1}")

list1 = [9, 8, 7]
list2 = [6, 5, 4, 3]
list3 = [2, 1]
con_res = func_with_return.concat_list(list1, list2, list3)
# Print the resulting list and its length
print(con_res)
print("length is:", len(con_res))

# Printing all the function helps:
functions = inspect.getmembers(func_with_return, predicate=inspect.isfunction)
function_names = [name for name, func in functions]
for name in function_names:
    full_func_name = "func_with_return." + name
    print(f"{help(full_func_name)}:")
    print()  # Add a blank line between help outputs

