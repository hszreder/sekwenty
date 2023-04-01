# formula = "ANKpANpqq"
formula = "NANpANqrANANpqANpr"


def splitting (formula):
    counter = 1
    subformula = []
    if formula[0] == "A" or formula[0] == "K":
        subformula.append(formula[0])
        formula = formula[1:]
        while counter != 0:
            if formula[0] == "A" or formula[0] == "K":
                counter += 1
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)
            elif formula[0] == "p" or formula[0] == "q" or formula[0] == "r":
                counter -= 1
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)
            else:
                # counter += 0
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)
    elif (formula[0] == "N" and formula[1] == "A" or formula[1] == "K"):
        subformula.append(formula[0:2])
        formula = formula[2:]
        while counter != 0:
            if formula[0] == "A" or formula[0] == "K":
                counter += 1
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)
            elif formula[0] == "p" or formula[0] == "q" or formula[0] == "r":
                counter -= 1
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)
            else:
                counter += 0
                subformula.append(formula[0])
                formula = formula[1:]
                print(formula, subformula, counter)

    #subformula2 = ",".join(subformula)
    return formula, subformula, counter


def left_conj (formula):
    if formula[0] == "K":
        formula = formula[1:]

    return formula

#potem splitting

#print(left_conj(formula))


def right_conj (formula):



def left_alt (formula):



def right_alt (formula):



def double_neg (formula):
    if formula[0] == "N" and formula[1] == "N":
        formula = formula[2:]

    return formula





print(splitting(formula))
