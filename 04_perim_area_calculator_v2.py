# functions go here

# checks input is a number more than zero 
def num_check(question):
    valid = False 
    while not valid:

        error = "please enter a number that is more than zero"
    
        try:

            # ask user to enter a number 
            response = float(input(question))

            # cheaks number is more than zero
            if response > 0:
                return response 

            # outputs error if input is invalid 
            else: 
                print(error)  
                print()         

        except ValueError:
            print(error)



# Main Routine goes here 

# Introduction / Heading print statements 
print()
print("**** Area Preimeter Calcuator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # calculate area (width x height)
    area = width * height 

    # calculate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter to 2 dp
    print("perimeter: {:.2f} untits".format(perimeter))
    print("area: {:.2f} square units".format(area))


    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")



