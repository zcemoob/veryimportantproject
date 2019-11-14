def average_of_squares(list_of_numbers, list_of_weights=None):

    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return (sum(squares))len(list_of_weights)


    if __name__ == "__main__":
    with open("data.txt", "r") as numbers_file:
        numbers_strings = numbers_file.readlines()

    with open("averages.txt", "w") as weights_file:
        file.write()

   # still in progress!!
    # weight_strings = weights_file.readlines()
    # numbers = convert_numbers(numbers_strings)
    # weights = convert_numbers(weight_strings)

    # result = average_of_squares(numbers, weights)

    # print(result)