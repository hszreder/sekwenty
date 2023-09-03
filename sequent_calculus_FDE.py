import string

propositional_variables = list(string.ascii_lowercase)

def correctness (formula):
    '''Checks if entered formula is correct. If correct, returns counter = 0.'''
    counter = 1
    for i in range(len(formula)):
        if formula[i] == "A" or formula[i] == "K":
            counter += 1
        elif formula[i] in propositional_variables:
            counter -= 1
        else:
            counter += 0
    return counter


def splitting (formula):
    '''Splits complex formula for subformulas.'''
    counter = 1
    subformula = ""
    if formula[0] == "A" or formula[0] == "K":
        formula = formula[1:]
        while counter != 0:
            if formula[0] == "A" or formula[0] == "K":
                counter += 1
                subformula = subformula + formula[0]
                formula = formula[1:]
            elif formula[0] in propositional_variables:
                counter -= 1
                subformula = subformula + formula[0]
                formula = formula[1:]
            else:
                subformula = subformula + formula[0]
                formula = formula[1:]
    elif (formula[0] == "N" and (formula[1] == "A" or formula[1] == "K")):
        subformula = subformula + formula[0]
        formula = formula[2:]
        while counter != 0:
            if formula[0] == "A" or formula[0] == "K":
                counter += 1
                subformula = subformula + formula[0]
                formula = formula[1:]
            elif formula[0] in propositional_variables:
                counter -= 1
                subformula = subformula + formula[0]
                formula = formula[1:]
            else:
                subformula = subformula + formula[0]
                formula = formula[1:]
        formula = "N" + formula

    return subformula, formula



def left_separate(formula):
    '''Separates formula at left side.'''
    obj = ""
    while formula[0] != "," and formula[0] != "S":
        obj = obj + formula[0]
        formula = formula[1:]
    return obj, formula


def right_separate(formula):
  '''Separates formula at right side.'''
  obj = ""
  while len(formula) != 0 and formula[0] != ",":
      obj = obj + formula[0]
      formula = formula[1:]
  return obj, formula


def separate_sides(formula):
    '''Separates left and right side of a sequent.'''
    left = ""
    while formula[0] != "S":
        left = left + formula[0]
        formula = formula[1:]
    formula = formula[1:]
    left = left + "S"
    return left, formula


def left_alt(formula):
    '''Function for left alternative'''
    obj, rest = left_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent_1 = subformula_1 + rest
    sequent_2 = subformula_2 + rest
    return sequent_1, sequent_2


def left_nalt(formula):
    '''Function for left negation of alternative'''
    obj, rest = left_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent = subformula_1 + "," + subformula_2 + rest
    return sequent


def left_conj(formula):
    '''Function for left conjunction'''
    obj, rest = left_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent = subformula_1 + "," + subformula_2 + rest
    return sequent


def left_nconj(formula):
    '''Function for left negation of conjunction.'''
    obj, rest = left_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent_1 = subformula_1 + rest
    sequent_2 = subformula_2 + rest
    return sequent_1, sequent_2

def right_nalt(formula):
    beginning, formula = separate_sides(formula)
    obj, rest = right_separate(formula)
    '''Function for right negation of alternative.'''
    subformula_1, subformula_2 = splitting(obj)
    sequent_1 = beginning + subformula_1 + rest
    sequent_2 = beginning + subformula_2 + rest
    return sequent_1, sequent_2


def right_alt(formula):
    '''Function for right alternative.'''
    beginning, formula = separate_sides(formula)
    obj, rest = right_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent = beginning + subformula_1 + "," + subformula_2 + rest
    return sequent


def right_conj(formula):
    '''Function for right conjunction'''
    beginning, formula = separate_sides(formula)
    obj, rest = right_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent_1 = beginning + subformula_1 + rest
    sequent_2 = beginning + subformula_2 + rest
    return sequent_1, sequent_2


def right_nconj(formula):
    '''Function for right negation of conjunction'''
    beginning, formula = separate_sides(formula)
    obj, rest = right_separate(formula)
    subformula_1, subformula_2 = splitting(obj)
    sequent = beginning + subformula_1 + "," + subformula_2 + rest
    return sequent


def double_negation_left(formula):
   beginning, formula = separate_sides(formula)
   while "NN" in beginning:
        beginning = beginning.replace("NN", "")
   formula = beginning + formula
   return formula


def double_negation_right(formula):
    beginning, formula = separate_sides(formula)
    while "NN" in formula:
        formula = formula.replace("NN", "")
    formula = beginning + formula
    return formula


how_many_p = input("How many premises do you want to add? ")

premises = ""

for i in range(int(how_many_p)):
    while True:
        premise = input("Write down the premise: ")
        if correctness(premise) == 0:
            print("Premise is correct.")
            premises = premises + "," + premise
            break
        else:
            print("Premise is not correct. Please write a correct premise.")


while True:
    conclusion = input("Write down the conclusion:")
    if correctness(conclusion) == 0:
        print("Conclusion is correct.")
        break
    else:
        print("Conclusion is not correct. Please write a correct conclusion.")

formula = premises[1:] + "S" + conclusion

print("Entered formula: ", formula)

sequents = [formula]
beginning = ""
to_do = [formula]

while to_do != []:
    if formula[0] == "K":
        sequent = left_conj(formula)
        sequents.append(beginning + sequent)
        sequents.remove(beginning + formula)
        to_do.append(beginning + sequent)
        to_do.remove(beginning + formula)
        formula = to_do[0]
        beginning = ""
        print("Left con", sequents)
    elif formula[0] == "A":
        sequent_1, sequent_2 = left_alt(formula)
        sequents.append(beginning + sequent_1)
        sequents.append(beginning + sequent_2)
        sequents.remove(beginning + formula)
        to_do.append(beginning + sequent_1)
        to_do.append(beginning + sequent_2)
        to_do.remove(beginning + formula)
        formula = to_do[0]
        beginning = ""
        print("Left alt", sequents)
    elif formula[0] == "N":
        if formula[1] == "A":
            sequent = left_nalt(formula)
            sequents.append(beginning + sequent)
            sequents.remove(beginning + formula)
            to_do.append(beginning + sequent)
            to_do.remove(beginning + formula)
            formula = to_do[0]
            beginning = ""
            print("Left nalt", sequents)
        elif formula[1] == "K":
            sequent_1, sequent_2 = left_nconj(formula)
            sequents.append(beginning + sequent_1)
            sequents.append(beginning + sequent_2)
            sequents.remove(beginning + formula)
            to_do.append(beginning + sequent_1)
            to_do.append(beginning + sequent_2)
            to_do.remove(beginning + formula)
            formula = to_do[0]
            beginning = ""
            print("Left ncon", sequents)
        elif formula[1] in propositional_variables:
            left, right = separate_sides(formula)
            if "A" not in left and "K" not in left and "NN" not in left:
                to_do.remove(beginning + formula)
                if len(to_do) != 0:
                    formula = to_do[0]
            else:
                beginning = beginning + formula[:2]
                formula = formula[2:]
        elif formula[1] == "N":
            '''Double negation'''
            sequent = double_negation_left(formula)
            sequents.append(beginning + sequent)
            sequents.remove(beginning + formula)
            to_do.append(beginning + sequent)
            to_do.remove(beginning + formula)
            formula = to_do[0]
            beginning = ""
            print("Double negations", sequents)
    elif formula[0] in propositional_variables or formula[0] == ",":
        '''Formulas starting with propositional variable or ",".'''
        left, right = separate_sides(formula)
        if "A" not in left and "K" not in left and "NN" not in left:
            to_do.remove(beginning + formula)
            if len(to_do) != 0:
                formula = to_do[0]
        else:
            beginning = beginning + formula[0]
            formula = formula[1:]

to_do = []
if sequents != []:
    to_do.extend(sequents)
else:
    to_do = [formula]

beginning = ""
formula = to_do[0]


while to_do != []:
    if all("A" not in formula and "K" not in formula and "NN" not in formula for formula in to_do):
        break
    left, right = separate_sides(formula)
    if right[0] == "K":
        sequent_1, sequent_2 = right_conj(formula)
        sequents.append(sequent_1)
        sequents.append(sequent_2)
        sequents.remove(formula)
        to_do.append(sequent_1)
        to_do.append(sequent_2)
        to_do.remove(formula)
        formula = to_do[0]
        beginning = ""
        print("Right con", sequents)
    elif right[0] == "A":
        sequent = right_alt(formula)
        sequents.append(sequent)
        sequents.remove(formula)
        to_do.append(sequent)
        to_do.remove(formula)
        formula = to_do[0]
        beginning = ""
        print("Right alt", sequents)
    elif right[0] == "N":
        if right[1] == "A":
            sequent_1, sequent_2 = right_nalt(formula)
            sequents.append(sequent_1)
            sequents.append(sequent_2)
            sequents.remove(formula)
            to_do.append(sequent_1)
            to_do.append(sequent_2)
            to_do.remove(formula)
            formula = to_do[0]
            beginning = ""
            print("Right nalt", sequents)
        elif right[1] == "K":
            sequent = right_nconj(formula)
            sequents.append(sequent)
            sequents.remove(formula)
            to_do.append(sequent)
            to_do.remove(formula)
            formula = to_do[0]
            beginning = ""
            print("Right nconj", sequents)
        elif right[1] in propositional_variables:
            left, right = separate_sides(formula)
            if "A" not in right and "K" not in right and "NN" not in right:
                to_do.remove(formula)
                if len(to_do) != 0:
                    formula = to_do[0]
            else:
                beginning = beginning + right[:2]
                if beginning[-1] == ",":
                    sequents.remove(formula)
                    to_do.remove(formula)
                    formula = left + right[3:] + "," + beginning[:-1]
                    to_do.append(formula)
                    sequents.append(formula)
                    formula = to_do[0]
                else:
                    sequents.remove(formula)
                    to_do.remove(formula)
                    formula = left + right[3:] + "," + beginning
                    to_do.append(formula)
                    sequents.append(formula)
                    formula = to_do[0]
            beginning = ""
        elif right[1] == "N":
            '''Double negation'''
            sequent = double_negation_right(formula)
            sequents.append(sequent)
            sequents.remove(formula)
            to_do.append(sequent)
            to_do.remove(formula)
            formula = to_do[0]
            beginning = ""
            print("Double negations", sequents)
    elif right[0] in propositional_variables or right[0] == ",":
        '''Formulas starting with propositional variable or ",".'''
        left, right = separate_sides(formula)
        if "A" not in right and "K" not in right and "NN" not in right:
            to_do.remove(formula)
            if len(to_do) != 0:
                formula = to_do[0]
        else:
            beginning = beginning + right[0]
            if beginning[-1] == ",":
                sequents.remove(formula)
                to_do.remove(formula)
                formula = left + right[2:] + "," + beginning[:-1]
                to_do.append(formula)
                sequents.append(formula)
                formula = to_do[0]
            else:
                sequents.remove(formula)
                to_do.remove(formula)
                formula = left + right[2:] + "," + beginning
                to_do.append(formula)
                sequents.append(formula)
                formula = to_do[0]
        beginning = ""

'''Checking if sequents are open or closed'''

def separate_left(sequent):
    left = ""
    current_sequent = sequent
    while current_sequent[0] != "S":
        left += current_sequent[0]
        current_sequent = current_sequent[1:]
    return left, current_sequent


def duplicates(list_1, list_2):
    return any(elem in list_2 for elem in list_1)

for sequent in sequents:
    left, right = separate_left(sequent)
    right = right[1:]
    left_list = left.split(",")
    right_list = right.split(",")
    closed = duplicates(left_list, right_list)
    if closed == False:
        print(sequent, "open")
    else:
        print(sequent, "closed")