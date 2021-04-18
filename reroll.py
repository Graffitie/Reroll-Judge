import random
import tkinter.messagebox
from tkinter import *

# Set up Variables
inputDice = 6
inputCount = 1
inputRoll = 4
iterations = 10000

# Set up tkinter GUI
root = Tk()  # sets up the main window
root.title("Reroll Judge")
root.geometry("700x400")
root.resizable(0, 0)

back = Frame(root, width=600, height=400)  # background frame for Layout

# Input Mask
labelDescription = Label(back, text="", font=("Cambria", 26))
labelDice = Label(back, text="How many-sided die?", font=("Cambria", 11))
entryDice = Entry(back)
entryDice.insert(10, "6")
labelDiceCount = Label(back, text="Number of dice?", font=("Cambria", 11))
entryDiceCount = Entry(back)
entryDiceCount.insert(10, "1")
labelRolled = Label(back, text="Total you rolled", font=("Cambria", 11))
entryRolled = Entry(back)
entryRolled.insert(10, "4")


def rollDice(event):
    global inputDice
    global inputCount
    global inputRoll
    global asked

    tallyYes = 0.0
    tallyNo = 0.0
    tallyDraw = 0.0

    inputDice = int(entryDice.get())
    inputCount = int(entryDiceCount.get())
    inputRoll = int(entryRolled.get())

    if inputDice == 0 or inputCount == 0 or inputRoll == 0:
        tkinter.messagebox.showinfo("ERROR", "Please enter valid Dice rolls")

    elif inputRoll > inputDice * inputCount:
        tkinter.messagebox.showinfo("ERROR", "You rolled higher than possible. I think you made a typo.")

    elif inputRoll < inputCount:
        tkinter.messagebox.showinfo("ERROR", "No one is that unlucky. I think you made a typo.")

    else:
        # runs a stochastic evaluation of dice rolls, i.e. rolls a shit ton of virtual dice
        for x in range(0, iterations):
            n = 0  # variable for adding multiple dice
            for v in range(0, inputCount):
                n += random.randint(1, inputDice)  # rolls the  dice the specified amount of times

            # splitting the roll results into categories: Is the roll better or is it a draw?
            if n > inputRoll:
                tallyYes += 1
            elif n == inputRoll:
                tallyDraw += 1
            else:
                tallyNo += 1

        # converts the roll results from 0-1 into percentage for human-readability
        # 'result' is percentage of higher or same rolls; 'strictly better' is strictly better rolls
        resultFloat = ((tallyYes + tallyDraw) / iterations) * 100
        resultRounded = float(int(((tallyYes + tallyDraw) / iterations) * 100))
        strictlyBetterFloat = (tallyYes / iterations) * 100
        strictlyBetterRounded = float(int((tallyYes / iterations) * 100))
        print(tallyYes)
        print(resultFloat)
        asked = 0

        # whole lot of outcomes with judgment calls and percentage results of rolling better / same-or-better
        if (resultFloat > 99.99):
            result = "Result for " + str(inputRoll) + ": \nCan't get much worse, can it?"
        elif (inputRoll == inputDice * inputCount):
            result = "Result for " + str(inputRoll) + ": \nUhm... No?"
        elif (resultFloat > 99.90):
            result = "Result for " + str(
                inputRoll) + ": \nLess than 1 in a 1000 bad luck. It can pretty much only get better!"
        elif (resultFloat > 95):
            result = "Result for " + str(inputRoll) + ": \nWhy are you even asking? Do it! There's a " + str(
                int(resultRounded)) + "% chance of rolling better or the same."
        elif (resultFloat > 87):
            result = "Result for " + str(inputRoll) + ": \nYes, of course!  " + str(
                int(resultRounded)) + "% chance of rolling better or the same."
        elif (resultFloat > 75):
            result = "Result for " + str(inputRoll) + ": \nAbsolutely! There's a " + str(
                int(resultRounded)) + "% chance of rolling better or the same."
        elif (resultFloat > 66):
            result = "Result for " + str(inputRoll) + ": \nYes! " + str(
                int(resultRounded)) + "% chance of rolling better or the same."
        elif (resultFloat > 52):
            result = "Result for " + str(inputRoll) + ": \nProbably. " + str(
                resultRounded) + "% chance of rolling better or the same."
        elif (strictlyBetterFloat > 40):
            result = "Result for " + str(inputRoll) + ": \nProbably not. Only " + str(
                int(strictlyBetterRounded)) + "% chance of rolling better."
        elif (strictlyBetterFloat > 20):
            result = "Result for " + str(inputRoll) + ": \nOnly if you have to. Just a " + str(
                int(strictlyBetterRounded)) + "% chance of rolling better."
        elif (strictlyBetterFloat > 5):
            result = "Result for " + str(inputRoll) + ": \nDefinitely not! Only a " + str(
                int(strictlyBetterRounded)) + "% chance of rolling better."
        elif (strictlyBetterFloat > 1):
            result = "Result for " + str(inputRoll) + ": \nReally bad idea. Only a " + str(
                int(strictlyBetterRounded)) + "% chance of rolling better."
        elif (strictlyBetterFloat > .3):
            result = "Result for " + str(inputRoll) + ": \nHow much more do you want? Don't do it!."
        elif (strictlyBetterFloat <= .3 and inputRoll > 20 and inputRoll > (inputDice * inputCount) - inputCount * 1.5):
            result = "Result for " + str(inputRoll) + ": \nYou know what? Do it. I dare you."
        else:
            result = "Result for " + str(inputRoll) + ": \nYou really, really shouldn't."

        # Output into an info popup window
        resultText = result
        tkinter.messagebox.showinfo("Result:", resultText)
        print(resultText)


# more GUI setup
buttonCalculate = Button(back, text="Calculate", font=("Cambria", 15))
buttonCalculate.bind("<Button-1>", rollDice)
labelResult = Label(back, text="Should you reroll?", font=("Cambria", 20))

# draw the GUI
back.pack()  # background frame

labelDescription.grid(row=0, columnspan=3, ipady=30)

labelDice.grid(row=1)
entryDice.grid(row=2)

labelDiceCount.grid(row=1, column=1)
entryDiceCount.grid(row=2, column=1, padx=50)

labelRolled.grid(row=1, column=2)
entryRolled.grid(row=2, column=2)

buttonCalculate.grid(row=4, column=1, pady=00)

labelResult.grid(row=3, columnspan=5, sticky=S, pady=30)

root.mainloop()  # Makes it that the GUI gets drawn every frame and doesn't close by itself
