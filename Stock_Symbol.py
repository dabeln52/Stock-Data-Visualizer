#Ask user for chart
def chartSelect():
    print("\nPlease enter the number that corresponds to the chart you would like to view: \n")

    print("Chart Types \n--------------\n 1. Bar\n 2. Line\n 3. Exit Program")

    while True:
        #Define Chart
        try:
            chart = int(input("\nI choose chart: "))
        except:
            print("This field only accepts numbers. \n Please choose again.\n ")
        #Confirm Selection
        if chart == 1: 
            print("You have chosen Bar Graph!")
            #Display Corresponding Graph
            break
        elif chart == 2:
            print("You have chosen Line Graph!")
            #Display Corresponding Graph
            break
        elif chart == 3:
            print("Now Exiting the Program! Goodbye!\n")
            break
        
chartSelect()




