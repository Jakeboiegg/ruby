towerDMG = int(input("What is the tower DMG: "))
towerRange = int(input("What is the tower range in radius: "))
mobHealth = int(input("What is the mob health: "))
mobSpeed = int(input("What is the mob speed: "))

effectiveRange = towerRange * 2
unitsLeft = effectiveRange
gameTick = 1

while mobHealth > 0 and unitsLeft > 0:
    mobHealth = mobHealth - towerDMG
    unitsLeft = unitsLeft - mobSpeed

    if mobHealth > 0 and unitsLeft > 0:
        print("Tick",gameTick,"|| " , mobHealth)
    else:
        break
         
    gameTick += 1

if mobHealth <= 0:
    print("Tick",gameTick,"|| DEAD")
elif unitsLeft <= 0:
    print("Tick",gameTick,"|| ESCAPED")