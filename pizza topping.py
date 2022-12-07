## The list for pizza modification
pizza_base = {"thick":10, "thin":5}
pizza_size = {"small":30, "medium":40, "large":50}
basic_sauce = {"tomato":5, "barbeque":5}
topping = {"cheese":5, "mushrooms":3, "avokado":7, "pineapple":5, "bacon":7, "chicken":7, "fish":6}


##before ordering the pizza
print ("Hello, welcome to the best place to order pizza!")

sum = 0
## Choosing the type of crust you want
while True:
    #s1 will be used in the if statement from the user input to match the outcome
    s1 = input("Choose pizza base, thick or thin:")

    if s1 in pizza_base.keys():
        print("you have chosen:", (s1))

        sum+= pizza_base[s1]
        break
    else:
        print("we only have these two options!")
##The choice of the size of the pizza
while True:
    s2 = input("Which size would you like the pizza to have? We have: small,medium,large:")

    if s2 in pizza_size.keys():
        print("Size wanted:", (s2))

        sum+= pizza_size[s2]
        break
    else:
        print("You have to choose the right size!")
### The choice of sauce 
while True:
    s3 = input("which type of sauce would you like?: tomato or barbeque:")
    if s3 in basic_sauce.keys():
        print("You would like", (s3), "as the sauce.")
        sum+= basic_sauce[s3]
        break
    else:
        print("We only have tomato or barbeque!")


####The choice of toppings
while True:
    s4 = input("Which type of toppings would you like? cheese,mushrooms,avokado,pinapple,bacon,chicken,fish:")
    if s4 in topping.keys():
        print("You have chosen", (s4))
        sum+=topping[s4]
        break
    else:
        print("We dont have this topping!")


## printing the total sum in the end

print("The total price for this pizza would be",(sum),"kr","for a pizza that has a:",(s1),"crust",", that is:",(s2),", with:",(s3),"and",(s4),"on.",end="")