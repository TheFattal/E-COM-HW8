def zugi_print(numbers):
    """Function gets a list of integers and then prints EVEN or ODD for every element in the list."""
    func_list = []
    for number in numbers:
        if number % 2 == 0:
            func_list.append("even")
        else:
            func_list.append("odd")
    return func_list
