import random
from dfa import DFA

CHARS = ['+', '-']
MIN_SEQUENCE = 3
MAX_SEQUENCE = 300

print('''   WELCOME
        This is a DFA using L-System, see how it works:
        1 - You'll have to start with 'f' and finish with 'f'
        2 - After you'll type a '+' you cant type a '-' or vice-versa

        See some eamples:
        -> fff+++++ffff
        -> f----f
        -> f+f

        Choose an option:
        (1) -> Type a sequence to verify if its valid or not
        (2) -> Generate a sequence valid
        (3) -> Load a sequence to draw
''')
while True:
    choose = int(input("Choose: "))
    if choose == 1:
        sequence = input("You choose 1, so type a sequence to verify: ")
        dfa = DFA()
        print("Result: ", dfa.accepts(sequence))
    elif choose == 2:
        sequence = ""
        char = random.choice(CHARS)
        alfabet = [char, 'f']
        len_sequence = random.randint(MIN_SEQUENCE, MAX_SEQUENCE)
        for i in range(len_sequence):
            if i == 0:
                sequence += 'f'
            elif i == (len_sequence - 1):
                sequence += 'f'
            else:
                sequence += random.choice(alfabet)
        print("The sequence is: ", sequence)
    elif choose == 3:
        import draw_dfa
        draw_dfa.run()


