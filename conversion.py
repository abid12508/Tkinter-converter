def inchestofeet():
    print("Input the amount of inches converted to feet: ; press "'0'" to switch the measurements")
    itfinp = float(input())
    itfconv = itfinp/12
    print(itfconv)
    
    if(itfconv == 1):
        print("Foot")
        menu()
    elif(itfinp == 0):
        print("Input the amount of feet converted to inches: ")
        itfinpswitch = float(input())
        itfconvswitch = itfinpswitch * 12
        print(itfconvswitch)
        
        if(itfconvswitch == 1):
            print("Inch")
            menu()
        else:
            print("Inches")
            menu()
    else:
        print("Feet")
        menu()

def ouncestopounds():
    print("input the amount of ounces to pounds: ; press "'0'" to switch the measurements")
    otpinp = float(input())
    otpconv = otpinp/16
    print(otpconv)
    
    if(otpconv == 1):
        print("Pound")
        menu()
    elif(otpinp == 0):
        print("Input the amount of pounds to ounces: ")
        otpinpswitch = float(input())
        optconvswitch = otpinpswitch*16
        print(optconvswitch)
        if(optconvswitch == 1):
            print("Ounce")
            menu()
        else:
            print("Ounces")
            menu()

    else:
        print("Pounds")
def feettoyards():
    print("Input the amount of feet to yards: ; press "'0'" to switch the measurements")
    ftyinp = float(input())
    ftyconv = ftyinp/3
    print(ftyconv)
    if(ftyconv == 1):
        print("Yard")
        menu()
    elif(ftyinp == 0):
        print("Input the amount of yards to feet: ")
        ftyinpswitch = float(input())
        ftyconvswitch = ftyinpswitch*3
        print(ftyconvswitch)
        if(ftyconvswitch == 1):
            print("Foot")
            menu()
        else:
            print("Feet")
            menu()
        
    else:
        print("Yards")
def menu():
    print("1. inches to Feet; 2. Ounces to Pounds; 3. Feet to Yards;")
    inputvar = input()
    if inputvar == "1":
        inchestofeet()
    elif inputvar == "2":
        ouncestopounds()
    elif inputvar == "3":
        feettoyards()
    else:
        print("Error, Try again")
        menu()   
menu()
