family = {}

def name_li(family):
    while True:
        family_rel = input("What is the family association: ")
        name = input("What is your name: ")
        add_name = input("Would you like to continue? 'yes' \
                         or 'no': ")
        if add_name == 'no':
            break
        family[family_rel] = name
    return family
        
def main():
    #for index, name in enumerate(name_li(names), 1):
    #    print(f"{index}. {name}")
    print(name_li(family))

if __name__ == "__main__":
    main()