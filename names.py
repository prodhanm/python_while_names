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
    for family_rel, name in name_li(family).items():
        print(f"{family_rel}: {name}")
    #print(name_li(family))

if __name__ == "__main__":
    main()