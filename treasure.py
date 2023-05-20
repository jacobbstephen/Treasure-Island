
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

dir = input("Enter left or right: ").lower()
if dir == "left":
    print("You have entered an island which is surrounded by water....... You need to reach the other shore to be safe from a beast which is gonna eat you")
    print("The beast is on it's way to eat you.....you've got 2 options..... either to swim across the sea to reach the shore or wait for the boat which is arriving...... which can be do or die becoz the beast is arriving...... choose wisely...... your life..... your choice")
    next_step = input("Enter swim or wait for the boat: ").lower()
    if next_step == "wait":
        print("You're safe buddy..... You've managed to reach the shore..... it's was a near miss from the beast!!")
        print("In the shore u got 3 doors..... Yellow, Blue & Red.... You've got to choose wisely to finish the game......It's a matter of luck")
        door = input("Enter the colour of the door:").lower()
        if door == "red" or door == "blue":
            print("Game Over")
        else:
            print("You won!!")
            print('''
 _                   _           
| |                 | |          
| |_ _ __ ___  _ __ | |__  _   _ 
| __| '__/ _ \| '_ \| '_ \| | | |
| |_| | | (_) | |_) | | | | |_| |
 \__|_|  \___/| .__/|_| |_|\__, |
              | |           __/ |
              |_|          |___/ 
''')
    else: 
        print("Buddy.....You are dead!!!.....")
else: 
        print("Buddy.....You are dead!!!.....")