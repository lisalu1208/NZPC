"""
Problem C:

Most people use a recipe when cooking something for the first time. They also check
that they have all the ingredients they need before they start! This problem will require
you to help with that process.

Input:

The first line of input will contain the name of the item being made. It will be no more
than 20 characters which may include spaces.
The next line will contain a single positive integer, N, the number of ingredients
required (N <= 20).
The next N lines will each contain details of 1 ingredient. The format for this will be
<name>, <units>, <amount>
<name> will be the name of the ingredient with up to 20 lower case letters or spaces
<units> will be the units in which the ingredient is measured. Solid ingredients will
be g (grams) or kg (kilograms, 1000 grams), powders or liquids in ml
(millilitres) or l (litres, 1000 millilitres) while x will denote a simple count.
<amount> will be the number of the units required. The number will be positive and
may contain a decimal part.
The final N lines will contain the amount of each ingredient available. The format will
be the same as that described above for the ingredients, but they may not be listed in
the same order. The <amount> value may be zero. The units will not necessarily be
the same.

Output:

If an appropriate amount of each of the ingredients required is available, the output
should be
You may make your <name>.
where <name> is the name of the item from the input.
If there is not enough of one or more ingredients, the output should be
You may NOT make your <name>.
You need <ingredient list>.
where <name> is the name of the item from the input and
<ingredient list> contains the names of each ingredient for which not enough is
available. Ingredients are to be listed in alphabetical order with a comma and space
between each.
"""

nameItem = input()

numIngredient = int(input())
ingredientList = []
availableList = []
canMake = True
neededList = []

if len(nameItem) <= 20 and numIngredient <= 20:
    for i in range(numIngredient):
        line = input()
        name = line.split(',')[0]
        units = line.split(',')[1]
        amount = float(line.split(',')[2])
        if units.find("kg") != -1 or units.find("l") != -1:
            amount *= 1000
        ingredientList.append([name, units, amount])

    for j in range(numIngredient):
        line = input()
        n = line.split(',')[0]
        u = line.split(',')[1]
        a = float(line.split(',')[2])
        if u.find("kg") != -1 or u.find("l") != -1:
            a *= 1000
        index = [ind for ind in range(len(ingredientList)) if n in ingredientList[ind]][0]
        if a < ingredientList[index][2]:
            canMake = False
            neededList.append(n)

    if canMake:
        print("You may make your " + nameItem + ".")
    else:
        print("You may NOT make your " + nameItem + ".")
        needed = sorted(neededList)
        print("You need " + ', '.join(needed) + '.')
        # availableList.append([name, units, amount])
