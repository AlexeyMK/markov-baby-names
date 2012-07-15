import random

from collections import defaultdict
from sys import argv

WORD_SEP = ' '

class MarkovName:
  def __init__(self, input_file):
    """ input file should have one name per line"""
    markov_file = open(input_file, 'r')
    # markov chain is a dictionary from {(letter) to list-of-letters-seen-after}
    # {c: 'aaoehhhhh   '}
    self.chain = defaultdict(list)
    names = (line for line in markov_file if not line[0] == '#')
    for name in names:
      # Alice
      proper_name = name.lower().strip()
      # alice
      pairs = zip(proper_name, proper_name[1:])
      #pairs = [(a,l), (l, i), (i, c), (c, e)]
      for first, second in pairs:
          self.chain[first].append(second)
      # +1 for e as last character
      self.chain[proper_name[-1]].append(WORD_SEP)
      # +1 for a as first character
      self.chain[WORD_SEP].append(proper_name[0])

  def generate_name(self):
    name = []
    current = WORD_SEP  # used to mark both first and last character
    while not (current == WORD_SEP and name):
      current = random.choice(self.chain[current])
      name.append(current)

    return ''.join(name).strip().capitalize()


if __name__ == '__main__':
    try:
      if len(argv) not in (2,3):
        raise Exception("Too many or too few arguments")
      names_file = argv[1]
      num_names = 1 if len(argv) == 2 else int(argv[2])
      chain = MarkovName(names_file)
      for number in xrange(1, num_names + 1):
        name = ''
        while len(name) < 3 or len(name) > 15:
          name = chain.generate_name()
          print "Name #%d: %s" % (number, name)
    except Exception as e:
      print "Usage: python markovbaby.py input_file.txt [num_names]"
      print "Exception: %s" % e
