import os
import itertools


def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield True
            yield from scantree(entry.path)

        else:
            yield entry

listing = list(scantree('Konto Bankowe'))

for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)
  
listing = scantree('Konto Bankowe')
listing = sorted(listing, key=lambda e: e.is_dir())
 
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))