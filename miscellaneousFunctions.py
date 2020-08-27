def subtractLists(first_list, second_list):
    result = first_list.copy()
    result={int(x)-int(y) for (x,y) in zip(first_list,second_list)}
    return result
    # return {[*first_list]:(x-y) for (x, y) in zip(first_list, second_list)}


def multiplyLists(first_list, second_list):
    return {x * y for (x, y) in zip(first_list, second_list)}


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
