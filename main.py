# imports
import math
import sys

print("This program offers entropy calculations for three different types of input.")


def entropyCalc(val):
    entropy = 0
    entropy += -(val * math.log2(val))
    return entropy


def strToFloat(string):
    arr = string.split("/")
    flt = float(int(arr[0]) / int(arr[1]))
    return flt


# probability entropy
def probCalc():
    oddsArray = []

    i = 0

    print("Enter probabilities as decimals or fractions for any number of events")
    print("(Leave blank and hit 'enter' to finish and/or auto calculate remaining probability)")
    while True:
        try:
            inp = input("\nEnter probability of event " + str(i+1) + ": ")
            oddsArray.append(inp)
            if float(inp) <= 0:
                raise ValueError
            i += 1
        except ValueError:
            if oddsArray[i] == '':
                oddsArray.pop()
                break
            try:
                # if input is a fraction (ex. '1/2')
                if float(inp) <= 0:
                    raise ValueError
                inp = strToFloat(inp)
                print("string to float complete")
                i += 1
            except ValueError:
                oddsArray.pop()
                print("Error: Event probability must be a positive decimal or a fraction in the form 'a/b'")

    entropy = 0
    for i in range(len(oddsArray)):
        try:
            oddsArray[i] = float(oddsArray[i])
        except ValueError:
            oddsArray[i] = strToFloat(oddsArray[i])

        entropy += entropyCalc(float(oddsArray[i]))

    if sum(oddsArray) < 1.00:
        complement = 1.00 - sum(oddsArray)
        oddsArray.append(complement)
        entropy += entropyCalc(complement)

    print("Probabilities:")
    for i in range(len(oddsArray)):
        print("Probability of Event " + str(i+1) + ": " + str(float(oddsArray[i]) * 100) + " percent")
    print("Entropy of above probabilities (in bits): " + str(entropy))


def setCalc():
    itemList = []
    itemCount = int(input("Enter the number of unique items in your set: "))
    totalEntropy = 0

    print("Does every unique element have the same frequency?")

    # try-except to ensure valid input
    while True:
        try:
            sameOp = input("Enter 'y' or 'n': ")
            if sameOp not in ("y", "Y", "n", "N"):
                raise ValueError
        except ValueError:
            print("Error: choice must be 'y' or 'n'")
        else:
            break

    if sameOp in ("y", "Y"):
        while True:
            try:
                freq = int(input("Enter the frequency of each unique item: "))
                if freq <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Item frequency must be a positive integer")
            else:
                break
        setSize = freq * itemCount

        for i in range(itemCount):
            totalEntropy += entropyCalc(freq / setSize)

        print("Set:\n"
              "Number of unique items:          " + str(itemCount) + "\n"
              "Frequency of each item:          " + str(freq) + "\n"
              "Total number of items in set:    " + str(setSize) + "\n"
              "Entropy of set:                  " + str(totalEntropy))

    else:
        for i in range(itemCount):
            while True:
                try:
                    itemList.append(
                        int(input("Enter the number frequency of item " + str(i + 1) + " in your set: ")))
                except ValueError:
                    print("Error: Item frequency must be an integer")
                else:
                    break

        setSize = sum(itemList)

        for i in range(len(itemList)):
            totalEntropy += entropyCalc(itemList[i] / setSize)

        print("Set:")
        for i in range(len(itemList)):
            print("Item " + str(i+1) + ": " + str(itemList[i]))

        print("Entropy of set: " + str(totalEntropy))
    return


# calculate and return entropy of a string
def entropyOfString(string):
    # initialize entropy at 0
    entropy = 0

    # loop through all 256 possible ascii inputs
    for i in range(256):
        # p = probability = the frequency of any given ascii character divided by the total number of
        #   characters in the string
        p = string.count(chr(i)) / len(string)

        # if p = 0 then there were no occurrences of the character 'i' in this pass
        if p > 0:
            # if prob > 0, then calculate the shannon entropy for this character, and add it to total entropy
            #   (since the formula requires the summation of all the characters' entropies)
            entropy += -(p * math.log2(p))

    return entropy
# driving method from which other functions are chained


def start():
    # initial selection
    print("\nSelect an Entropy Calculator Type:\n"
          "1. Entropy based on probabilities\n"
          "2. Entropy based on item frequencies in a set\n"
          "3. Entropy based on symbol frequencies in a phrase\n")

    # try-except to ensure valid input
    while True:
        try:
            answer = input("Enter '1', '2', or '3': ")
            if answer not in ("1", "2", "3"):
                raise ValueError
        except ValueError:
            print("Error: choice must be '1', '2', or '3'")
        else:
            break

    # decision handling for probability or symbol frequency entropy
    if answer == '1':
        probCalc()
    elif answer == '2':
        setCalc()
    else:
        # symbol frequency entropy
        phrase = input("Enter characters for entropy calculation: ")
        print("Entropy of\n'" + phrase + "'\nin bits is: " + str(entropyOfString(phrase)))

    print("\nWould you like to do another entropy calculation?")

    # try-except to ensure valid input
    while True:
        try:
            restart = input("Enter 'y' or 'n': ")
            if restart not in ("y", "Y", "n", "N"):
                raise ValueError
        except ValueError:
            print("Error: choice must be 'y' or 'n'")
        else:
            break

    if restart in ("y", "Y"):
        start()
    else:
        print("Bye!")
        sys.exit()


start()


