family = {}

def name_li(family):
    while True:
        family_rel = input("What is the family association: ")
        name = input("What is your name: ")
        family[family_rel] = name
        add_name = input("Would you like to continue? 'yes' \
                         or 'no': ")
        if add_name == 'no':
            break
    return family
        
def main():
    for family_rel, name in name_li(family).items():
        print(f"{family_rel}: {name}")

if __name__ == "__main__":
    main()