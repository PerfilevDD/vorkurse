#!/usr/bin/python
if __name__ == '__main__':
    file_name = input("Name: ")
    new_name = ""

    for i in file_name:
        if i == " " or i == "(" or i == ")" or i == "!" or i == "?":
            i = "_"
            new_name = new_name + i
        else:
            new_name = new_name + i
            
    new_name = new_name + ".py"

    new_name = new_name.lower()

    f = open(new_name, "x")
    print(f"{new_name} ist erstellt.")

