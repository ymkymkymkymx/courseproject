## My results for the 4 five letter pairs
```
C:\Users\yumin\Desktop\cshw\lab7>python word.py
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 5757 nodes with 14135 edges
853 connected components
Shortest path between chaos and order is
chaos
choos
shoos
shoes
shoed
shred
sired
sided
aided
added
adder
odder
order
Shortest path between nodes and graph is
nodes
lodes
lores
lords
loads
goads
grads
grade
grape
graph
Shortest path between moron and smart is
moron
boron
baron
caron
capon
capos
capes
canes
banes
bands
bends
beads
bears
sears
stars
start
smart
Shortest path between files and swims is
files
fills
fells
sells
seals
seams
shams
shims
swims
Shortest path between mango and peach is
mango
mange
marge
merge
merse
terse
tease
pease
peace
peach
Shortest path between pound and marks is
None
```
## My code for the four letter solution
```
"""

=====

Words

=====



Words/Ladder Graph

------------------

Generate  an undirected graph over the 5757 5-letter words in the

datafile `words_dat.txt.gz`.  Two words are connected by an edge

if they differ in one letter, resulting in 14,135 edges. This example

is described in Section 1.1 in Knuth's book (see [1]_ and [2]_).



References

----------

.. [1] Donald E. Knuth,

   "The Stanford GraphBase: A Platform for Combinatorial Computing",

   ACM Press, New York, 1993.

.. [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html

"""

# Authors: Aric Hagberg (hagberg@lanl.gov),

#          Brendt Wohlberg,

#          hughdbrown@yahoo.com



#    Copyright (C) 2004-2019 by

#    Aric Hagberg <hagberg@lanl.gov>

#    Dan Schult <dschult@colgate.edu>

#    Pieter Swart <swart@lanl.gov>

#    All rights reserved.

#    BSD license.



import gzip

from string import ascii_lowercase as lowercase



import networkx as nx



#-------------------------------------------------------------------

#   The Words/Ladder graph of Section 1.1

#-------------------------------------------------------------------





def generate_graph(words):

    G = nx.Graph(name="words")

    lookup = dict((c, lowercase.index(c)) for c in lowercase)



    def edit_distance_one(word):

        for i in range(len(word)):

            left, c, right = word[0:i], word[i], word[i + 1:]

            j = lookup[c]  # lowercase.index(c)

            for cc in lowercase[j + 1:]:

                yield left + cc + right

    candgen = ((word, cand) for word in sorted(words)

               for cand in edit_distance_one(word) if cand in words)

    G.add_nodes_from(words)

    for word, cand in candgen:

        G.add_edge(word, cand)

    return G





def words_graph():

    """Return the words example graph from the Stanford GraphBase"""

    fh = gzip.open('words4_dat.txt.gz', 'r')

    words = set()

    for line in fh.readlines():

        line = line.decode()

        if line.startswith('*'):

            continue

        w = str(line[0:4])

        words.add(w)

    return generate_graph(words)





if __name__ == '__main__':

    G = words_graph()

    print("Loaded words_dat.txt containing 5757 five-letter English words.")

    print("Two words are connected if they differ in one letter.")

    print("Graph has %d nodes with %d edges"

          % (nx.number_of_nodes(G), nx.number_of_edges(G)))

    print("%d connected components" % nx.number_connected_components(G))



    for (source, target) in [('cold', 'warm'),

                             ('love', 'hate'),

                             ('good', 'evil'),
                             ('pear','beef'),
                             ('make','take')]:

        print("Shortest path between %s and %s is" % (source, target))

        try:

            sp = nx.shortest_path(G, source, target)

            for n in sp:

                print(n)

        except nx.NetworkXNoPath:

            print("None")
```
## My results for the four letter pairs
```
C:\Users\yumin\Desktop\cshw\lab7>python word4.py
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 2174 nodes with 8040 edges
129 connected components
Shortest path between cold and warm is
cold
wold
word
ward
warm
Shortest path between love and hate is
love
hove
have
hate
Shortest path between good and evil is
None
Shortest path between pear and beef is
pear
bear
beer
beef
Shortest path between make and take is
make
take
```
## My code for the unordered solution
```
"""

=====

Words

=====



Words/Ladder Graph

------------------

Generate  an undirected graph over the 5757 5-letter words in the

datafile `words_dat.txt.gz`.  Two words are connected by an edge

if they differ in one letter, resulting in 14,135 edges. This example

is described in Section 1.1 in Knuth's book (see [1]_ and [2]_).



References

----------

.. [1] Donald E. Knuth,

   "The Stanford GraphBase: A Platform for Combinatorial Computing",

   ACM Press, New York, 1993.

.. [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html

"""

# Authors: Aric Hagberg (hagberg@lanl.gov),

#          Brendt Wohlberg,

#          hughdbrown@yahoo.com



#    Copyright (C) 2004-2019 by

#    Aric Hagberg <hagberg@lanl.gov>

#    Dan Schult <dschult@colgate.edu>

#    Pieter Swart <swart@lanl.gov>

#    All rights reserved.

#    BSD license.



import gzip

from string import ascii_lowercase as lowercase
import itertools 


import networkx as nx



#-------------------------------------------------------------------

#   The Words/Ladder graph of Section 1.1

#-------------------------------------------------------------------





def generate_graph(words):

    G = nx.Graph(name="words")

    lookup = dict((c, lowercase.index(c)) for c in lowercase)



    def edit_distance_one(word):

        for i in range(len(word)):

            left, c, right = word[0:i], word[i], word[i + 1:]

            j = lookup[c]  # lowercase.index(c)

            for cc in lowercase[j + 1:]:
                a=left + cc + right
                for s in itertools.permutations(a, len(a)):
                    fullstring=""
                    for le in s:
                        fullstring=fullstring+le
                    yield  fullstring

    candgen = ((word, cand) for word in sorted(words)

               for cand in edit_distance_one(word) if cand in words)

    G.add_nodes_from(words)

    for word, cand in candgen:

        G.add_edge(word, cand)

    return G





def words_graph():

    """Return the words example graph from the Stanford GraphBase"""

    fh = gzip.open('words_dat.txt.gz', 'r')

    words = set()

    for line in fh.readlines():

        line = line.decode()

        if line.startswith('*'):

            continue

        w = str(line[0:5])

        words.add(w)

    return generate_graph(words)





if __name__ == '__main__':

    G = words_graph()

    print("Loaded words_dat.txt containing 5757 five-letter English words.")

    print("Two words are connected if they differ in one letter.")

    print("Graph has %d nodes with %d edges"

          % (nx.number_of_nodes(G), nx.number_of_edges(G)))

    print("%d connected components" % nx.number_connected_components(G))



    for (source, target) in [('chaos', 'order'),

                             ('nodes', 'graph'),

                             ('moron', 'smart'),
                             ('files','swims'),
                             ('mango','peach'),
                             ('pound','marks')]:

        print("Shortest path between %s and %s is" % (source, target))

        try:

            sp = nx.shortest_path(G, source, target)

            for n in sp:

                print(n)

        except nx.NetworkXNoPath:

            print("None")
```
## My results for the 4 five letter pairs using the unordered implementation
```
C:\Users\yumin\Desktop\cshw\lab7>python alter.py
Loaded words_dat.txt containing 5757 five-letter English words.
Two words are connected if they differ in one letter.
Graph has 5757 nodes with 112278 edges
16 connected components
Shortest path between chaos and order is
chaos
hoars
arose
adore
order
Shortest path between nodes and graph is
nodes
anode
agone
anger
gaper
graph
Shortest path between moron and smart is
moron
manor
roams
smart
Shortest path between files and swims is
files
isles
semis
swims
Shortest path between mango and peach is
mango
conga
nacho
poach
peach
Shortest path between pound and marks is
pound
mound
monad
damns
drams
marks
```