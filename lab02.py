# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Roll the dice to determine the weapon
weaponRoll = random.randint(1, 6)  # Roll a dice (1-6)

# Add weaponRoll to hero's combat strength
combatStrength = int(input("Enter your combat Strength: "))
combatStrength += weaponRoll

# Print the weapon name
weaponName = weapons[weaponRoll - 1]  # -1 because index starts from 0
print(f"You rolled a {weaponRoll}. Your weapon is: {weaponName}")

# Define weapon strength conditions
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# Check if the weapon is not a Fist
if weaponName != "Fist":
    print("Thank goodness you didn't roll the Fist...")
else:
    print("Oh no, you're stuck with the Fist!")

# Get the monster's combat strength
mCombatStrength = int(input("Enter the monster's combat Strength: "))

# Roll the dice for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.randint(1, 6)
print(f"You rolled {healthPoints} health points.")

# Roll the dice for the monster's health points
input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.randint(1, 6)
print(f"The monster rolled {mHealthPoints} health points.")

# Roll to see if you find a healing potion
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print(f"Have you found a healing potion?: {bool(healingPotion)}")

# Analyze the rolls
input("Analyze the roll (Press enter)")
# Equality operators
print(f"--- You are matched in strength: {combatStrength == mCombatStrength}")

# Relational operators
print(f"--- You have a strong player: {combatStrength + healthPoints >= 15}")

# and keyword
print(f"--- Remember to take a healing potion!: {healingPotion == 1 and healthPoints <= 6}")

# not keyword
print(f"--- Phew, you have a healing potion: {not (healthPoints < mCombatStrength and healingPotion == 1)}")

# or keyword
print(f"--- Things are getting dangerous: {healingPotion == 0 or healthPoints == 1}")

# in keyword
print(f"--- Is it possible to roll 0 in the dice?: {0 in range(1, 7)}")

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print(f"--- Using your healing potion... Your Health Points is now full at {healthPoints}")
else:
    print(f"--- Your health is low at {healthPoints} and you have no healing potions available!")

# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print(f"Your weapon ({combatStrength}) ---> Monster ({mHealthPoints})")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print(f"You've reduced the monster's health to: {mHealthPoints}")

    print("The monster strikes!!!")
    print(f"Monster's Claw ({mCombatStrength}) ---> You ({healthPoints})")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print(f"The monster has reduced your health to: {healthPoints}")