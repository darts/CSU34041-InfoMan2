#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <max words>', file=sys.stderr)
    sys.exit(1)

max_words = int(sys.argv[1])

tweaked = ''
material = sys.stdin.read()
for (i, word) in enumerate(material.split(' ')):
    tweaked += word
    if i < max_words:
        tweaked += ' '
    else:
        tweaked += '\n'

f1 = open('resFile.txt', 'w+')
f1.write(tweaked)
f1.close