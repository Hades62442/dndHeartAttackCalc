import random

def main():
    global reps
    amountDied = 0
    days = 40
    reps = 5000
    for i in range(reps):
        j = 0
        died = False
        while not died and j < days:
            roll = random.randint(1, 100)
            #print(roll)
            if roll == 79:
                amountDied += 1
                died = True
            j += 1
    
    #print(f"Amount of deaths: {amountDied}")
    #print(f"Percentage of dying: {amountDied/reps*100}%")

    return amountDied


vals = []
for i in range(1000):
    amountDied = main()
    print(f"{amountDied/reps*100}%")
    vals.append(amountDied/reps*100)

total = 0
for i in range(len(vals)):
    total += vals[i]

avg = total/len(vals)
print(f"Average percentage of getting a heart attack: {avg}%")
