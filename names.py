names = []

def name_li(names):
    while True:
        name = input("What is your name: ")
        names.append(name)
        add_name = input("Would you like to continue. 'yes' \
                         or 'no': ")
        if add_name == 'no':
            break
    return names
        
def main():
    for index, name in enumerate(name_li(names), 1):
        print(f"{index}. {name}")

if __name__ == "__main__":
    main()