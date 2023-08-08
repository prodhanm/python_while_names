def name_li():
    names = []
    while True:
        print("What is your name: ")
        name = input()
        print("Do you have any names to add? (Yes or No)")
        add_names = input("Please enter 'Yes' or 'No': ")
        if add_names == 'Yes':
            names += name
        else:
            break
    return names
        
def main():
    print(name_li())
    for name in name_li():
        print(name)

if __name__ == "__main__":
    main()