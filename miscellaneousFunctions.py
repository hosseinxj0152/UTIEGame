def subtractLists(first_list, second_list):
  if(len(first_list)!=len(second_list)):
    print("The lengths of your lists are not the same! Please try again!")
  else:
    return [x - y for (x, y) in (first_list, second_list)]
def multiplyLists(first_list, second_list):
  if(len(first_list)!=len(second_list)):
    print("The lengths of your lists are not the same! Please try again!")
  else:
    return [x * y for (x, y) in (first_list, second_list)]

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
