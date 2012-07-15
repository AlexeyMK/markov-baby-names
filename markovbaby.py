def create_chain(input_file):
    markov_file = open(input_file, 'r')
    from collections import defaultdict
    chain = defaultdict(list)
    # markov chain is a dictionary from {(letter) to list-of-letters-seen-after}
    # {c: 'aaoehhhhh   '}
    for line in markov_file:
        if line.startswith('#'):
            continue
        # Alice
        line = line.lower().strip()
        # alice
        pairs = zip(line, line[1:])
        #pairs = [(a,l), (l, i), (i, c), (c, e)]
        for first, second in pairs:
            chain[first].append(second)
        # +1 for e as last character
        chain[line[-1]].append(' ')
        # +1 for a as first character
        chain[' '].append(line[0])

    return chain


def generate_name(chain):
    from random import choice
    name = ''
    current = ' ' # pick first letter
    while True:
        current = choice(chain[current])
        if current != ' ':  # word isn't over yet
            name+= current
        else:
            break

    return name.capitalize()


if __name__ == '__main__':
    from sys import argv
    names_file = argv[1]
    num_names = 1 if len(argv) == 2 else int(argv[2])
    markov_chain = create_chain(names_file)
    for number in xrange(1, num_names + 1):
        name = ''
        while len(name) < 3 or len(name) > 15:
            name = generate_name(markov_chain)
        print "Name #%d: %s" % (number, name)
