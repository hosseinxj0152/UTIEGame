def subtractLists(first_list, second_list):
    result_values = {int(x) - int(y) for (x, y) in zip(list(first_list.values()), list(second_list.values()))}
    zip_iterator = zip(list(first_list.keys()), result_values)
    return dict(zip_iterator)


def multiplyLists(first_list, second_list):
    result_values = {int(x) * int(y) for (x, y) in zip(list(first_list.values()), list(second_list.values()))}
    zip_iterator = zip(list(first_list.keys()), result_values)
    return dict(zip_iterator)


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
