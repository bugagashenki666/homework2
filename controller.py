import re
from calc.operations import add
from calc.operations import dif
from calc.operations import div
from calc.operations import mul
from calc.operations import power
from calc.history import save
from calc.history import save_error
from calc.history import load
from calc.history import clear
from calc.history import print_calculations


def calculate(s):
    regex = r"(\d+\.?\d*)([+-/*]{1}|\*\*)(\d+\.?\d*)"
    matches = re.finditer(regex, s)
    results = []
    for matchNum, match in enumerate(matches, start=0):
        a = match.group(1)
        op = match.group(2)
        b = match.group(3)
        float_set = set(list("0123456789."))
        if not set(list(a)) <= float_set or not set(list(b)) <= float_set or not set(list(op)) <= set(list("+-/*")):
            results.append([-1, -1, -1, -1])
            continue
        res = 0
        if op == "+":
            res = add(float(a), float(b))
        elif op == "-":
            res = dif(float(a), float(b))
        elif op == "/":
            res = div(float(a), float(b))
        elif op == "*":
            res = mul(float(a), float(b))
        elif op == "**":
            res = power(float(a), float(b))
        results.append([a, b, op, res])
    return results


def execute():
    while True:
        s = input()
        if s in ("exit", "quit"):
            exit(0)
        elif s in ("load", "history"):
            print_calculations()
        elif s in ("clear", "clr"):
            clear()
        else:
            results_ = calculate(s)
            for st in results_:
                a = st[0]
                b = st[1]
                op = st[2]
                res = st[3]
                if a == -1 and b == - 1 and op == -1 and res == -1:
                    print("Not correct expression: {}".format(s))
                    save_error("Not correct expression: {}".format(s))
                else:
                    print("{}{}{}={}".format(a, op, b, res))
                    save(a, b, op, res)
