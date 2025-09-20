import math
from fractions import Fraction
from idlelib.pyshell import restart_line


def function_entropy(p1, p2):
    result = -((float(p1) * math.log2(float(p1))) + (float(p2) * math.log2(float(p2))))
    print(f"Float p1 = {float(p1)} || result_log_p1 = {math.log2(float(p1))}")
    print(f"Float p2 = {float(p2)} || result_log_p2 = {math.log2(float(p2))}")
    print("result = ", result)
    print()


def function_weight_avg_entropy(n):
    number_element = []
    number_store_for_cal = []
    for i in range(n):
        number_element.append(i)

    for j in range(len(number_element)):
        number_for_cal = Fraction(input(f"{j+1} : "))
        number_store_for_cal.append(float(number_for_cal))


    result = []
    term = []
    for k in range(0, n, 2):
        pair_result = number_store_for_cal[k] * number_store_for_cal[k+1]
        result.append(pair_result)
        term.append(f"{number_store_for_cal[k]} × {number_store_for_cal[k + 1]}")


    eq = " + ".join(term)
    print(f"({eq})")

    text_decide = str(input(f"Are you sure with number 'y' or 'n ' : "))
    if text_decide == "y":
        total = sum(result)
        print(f"Weight_avg_entropy = {total}")
    if text_decide == "n":
        return None

while True :
        text_input = str(input("Enter a func '1' (entropy) || '2' (weight avg entropy) || : "))
        if text_input == "1" :
            p1 = Fraction(input("Enter a p1 : "))
            p2 = Fraction(input("Enter a p2 : "))
            function_entropy(p1, p2)
        if text_input == "2" :
            num_input = int(input("Enter how many numbers you want : "))
            function_weight_avg_entropy(num_input)



