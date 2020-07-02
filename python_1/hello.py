first_name = input("What is your first name? ");
print("Hello,",first_name);
if first_name == "Bala":
    print(first_name," is learning python");
elif first_name == "vijay":
    print(first_name, "is learning with fellow students in the community! Me too!")    
else:
    # This is just in case younger user can't read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading...".format(age))
    print("You should totally learn python, {}!".format(first_name))    
print("have a great day {}!".format(first_name));