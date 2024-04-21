import itertools


def remove_wrong_possibilities(guess):
    global remaining_options

    for i in range(len(remaining_options)-1, -1, -1):
        if evaluate(remaining_options[i], guess[0]) != guess[1]:
            remaining_options.pop(i)
    return remaining_options


def evaluate(original, guess):
    original = list(original)
    guess = list(guess)
    black = 0
    white = 0
    for i in range(4):
        if original[i] == guess[i]:
            black += 1
    
    for i in range(4):
        if guess[i] in original:
            white += 1
            original.remove(guess[i])
    return black, white - black
    

stuff = ['pu', 'or', 'bl', 'ye', 're', 'br', 'gr', 'pi']
remaining_options = []
for subset in itertools.product(stuff, repeat=4):
    remaining_options.append(subset)


# remaining_options = remove_wrong_possibilities((('', '', '', ''), (0, 2)))
remaining_options = remove_wrong_possibilities((('pu', 'or', 'bl', 'ye'), (0, 1)))
remaining_options = remove_wrong_possibilities((('re', 'br', 'gr', 'pi'), (0, 3)))
remaining_options = remove_wrong_possibilities((('br', 'pi', 'pu', 'gr'), (2, 1)))
remaining_options = remove_wrong_possibilities((('br', 'pu', 're', 'gr'), (2, 1)))
# remaining_options = remove_wrong_possibilities((('br', 'ye', 'gr', 'ye'), (0, 1)))

print(remaining_options)
