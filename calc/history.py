def save(a, b, op, res):
    with open("history.txt", "at") as f:
        f.write("{}{}{}={}\n".format(a, op, b, res))


def save_error(s):
    with open("history.txt", "at") as f:
        f.write("{}\n".format(s))


def load():
    with open("history.txt", "rt") as f:
        return f.readlines()


def clear():
    with open("history.txt", "w") as f:
        pass


def print_calculations():
    print("History of calculations:")
    history_lines = load()
    for st in history_lines:
        print(st.replace("\n", ""))