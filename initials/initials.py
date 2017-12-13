def get_initials(fullname):
    initials = ""
    name_list = fullname.split()
    for part in name_list:
        initials += part[0].upper()
    return initials
    # some code here

def main():
    fullname = input('Type your full name and press ENTER. ')
    print(get_initials(fullname))
    # some more code here (input and print statements)

if __name__ == '__main__':
    main()

