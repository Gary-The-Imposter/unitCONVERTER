def convert_Units(user_list):
    ## A series of if statements to find the correct Algorithm
    if user_list[1] == 'mm':
        ## Creates the calculation and formatted output
        golden_Egg = "{} Millimeters is equal to {:.2f} Inches".format(user_list[0],float(user_list[0]) * .03937)
    if user_list[1] == 'cm':
        golden_Egg = "{} Centimeters is equal to {:.2f} Inches".format(user_list[0],float(user_list[0]) * .3937)
    if user_list[1] == 'm':
        golden_Egg = "{} Meters is equal to {:.2f} Yards".format(user_list[0],float(user_list[0]) * 1.0936)
    if user_list[1] == 'km':
        golden_Egg = "{} Kilometers is equal to {:.2f} Miles".format(user_list[0],float(user_list[0]) * .6214)
    if user_list[1] == 'in':
        golden_Egg = "{} Inches is equal to {:.2f} Centimeters".format(user_list[0],float(user_list[0]) * 2.54)
    if user_list[1] == '\"':
        golden_Egg = "{} Inches is equal to {:.2f} Centimeters".format(user_list[0],float(user_list[0]) * 2.54)
    if user_list[1] == 'ft':
        golden_Egg = "{} Feet is equal to {:.2f} Meters".format(user_list[0],float(user_list[0]) * .3048)
    if user_list[1] == '\'':
        golden_Egg = "{} Feet is equal to {:.2f} Meters".format(user_list[0],float(user_list[0]) * .3048)
    if user_list[1] == 'yd':
        golden_Egg = "{} Yards is equal to {:.2f} Meters".format(user_list[0],float(user_list[0]) * .9144)
    if user_list[1] == 'mi':
        golden_Egg = "{} Miles is equal to {:.2f} Kilometers".format(user_list[0],float(user_list[0]) * 1.6093)
    if user_list[1] == 'nm':
        golden_Egg = "{} Nautical Miles is equal to {:.2f} Kilometers".format(user_list[0],float(user_list[0]) * 1.853)
    if user_list[1] == 'c':
        golden_Egg = "{} Celsius is equal to {:.2f} Degrees Fahrenheit".format(user_list[0],float(user_list[0]) * 9/5 + 32)
    if user_list[1] == 'f':
        golden_Egg = "{} Fahrenheit is equal to {:.2f} Degrees Celsius".format(user_list[0],float(user_list[0]) - 32 * 5/9)
    ## Returns the formatted answer as a string
    return golden_Egg

def unit_Converter():
    ## Explination of how to use the program
    ## This displays only once to the user
    print("Welcome to Gary's Unit Converter.")
    print("To convert a unit, input a number followed by a space and then a unit.")
    print("Example Input: 200 mi")
    print("You may input as many numbers as you'd like.")
    print("Here is the list of units:")
    print(" 'mm' 'cm' 'm' 'km' 'in' 'ft' 'yd' 'mi' 'nm' 'c' 'f' ")
    ## Program Start
    while True:
        user_Input = input("How much of what unit would you like to convert: ")
        #List Creation
        processed_Input = user_Input.split(" ")
        #Format Process
        processed_Input[1] = processed_Input[1].lower()
        #Acceptable Units List
        unit_List = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nm', 'c', 'f']
        #Input Check & Response
        ##Converted Units displayed to the user
        if len(processed_Input) == 2 and processed_Input[0].isnumeric() == True and processed_Input[1] in unit_List or processed_Input[1] == '\'' or processed_Input[1] == '\"':
            golden_Egg = convert_Units(processed_Input)
            ## Displays the Converted Units to the user
            print(golden_Egg)
            ## Cycle continues
            print("Would you like to convert another unit?")
        #### If user's input is invalid
        else:
            print("I'm sorry that's not a valid input.")

def main():
    unit_Converter()

if __name__=='__main__':
    main()

