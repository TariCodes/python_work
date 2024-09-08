print ("------------")
print ("RIZZLE!!!!")
print ("------------\n")

print("INSTRUCTION \n\nRizzle is a fun game that helps solve sinical challenges in a rigorous way\n")


prompt = input(print ("Do you want to play? \t[Y/N]"))
while(prompt != "Y" | "N"):
    print("your answer must be Y or N")
    if (prompt == "Y"): 
        firstName = input ("Please enter your Firstname: ")
        lastName = input ("Please enter your Lastname: ") 
        greetings = firstName + " " + lastName
        print("welcome " + greetings.title())
    if (prompt == "N"):
        exit
# else:
#     print("your answer must be Y or N")

