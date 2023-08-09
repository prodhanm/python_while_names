name_loop = True
names = []

def name_li(name_loop, names):
    while name_loop != '-1':
        name = input("What is your name: ")
        names.append(name)
        add_name = input("Would you like to continue. 'yes' \
                         or 'no': ")
        if add_name == 'no':
            break
    return names
        
def main():
    for index, name in enumerate(name_li(name_loop,names)):
        print(f"{index}. {name}")

if __name__ == "__main__":
    main()