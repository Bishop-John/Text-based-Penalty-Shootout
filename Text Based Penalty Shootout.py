import random, time

print ("Welcome to the World Cup Penalty Shoot Out Game!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

goals = 0
shotLocations = ["BL", "TL", "M", "BR", "TR"]
team1 = input("Who is the player team... ")

for i in range(5):
    print ("You need to place your penalty either Bottom Left (BL), Top Left (TL), Middle (M), Bottom Right (BR), Top Right (TR)")
    playerShot = input("Where do you want to shoot? ").upper()
    while playerShot not in shotLocations:
        playerShot = input("Invalid option. Try again... ").upper()

    time.sleep(1)
    keeperSave = random.choice(shotLocations)
    print ("The keeper went", keeperSave)
    time.sleep(1)
    if playerShot == keeperSave:
        print ("PENALTY SAVED!!!!!")
    else:
        print ("PENALTY SCORED!!!")
        goals = goals + 1
    
print ("The shootout is over.", team1, "scored", goals, "of their penalties!")
