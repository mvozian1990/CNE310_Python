def name(name, age, weight, height):
    p_name = "Name: " + name
    p_age = "Age: " + str(age)
    p_weight = "Weight: "+ str(weight)
    print(p_name)
    print(p_age)
    print(p_weight)
    print("Height:", str(height//12), "ft", str(height%12), "inches")
    print()

name("Joe", 22, 123, 69)
name("Josh", 32, 156, 74)
name("Mabel", 21, 106, 62)
