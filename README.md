## Approach

My experience with Python is limited to writing [this script](https://github.com/ivanmaeder/vimv) a long long time ago, and spending a [couple of afternoons](https://github.com/ivanmaeder/NLP) once looking at the Natural Language Processing with Python book.

Nevertheless, I'm going with Python because I'm bound to learn a few things.

Please excuse the blunders.

I'm using:

- Python 3.7.2
- pytest 4.3.0
- Networkx 2.2

## Question 1

I assumed this could be achieved by converting the data into a node graph and using a shortest path algorithm with the search criteria modified—replacing the sum of the path weights with the largest weight on the paths.

So that's what I did, using Dijkstra's algorithm.

Calculating the complexity…

- v&sup2; when converting the input file to a node graph (each vertex is connected to all other vertices, so v &times; v)
- v to create the priority queue
- v(v + log v) when iterating through the unvisited nodes, and inside: checking for the next node to visit, and the neighbours of that node

So overall, O(v&sup2;).

### Further possible optimisations

- Use a proper priority queue data structure that indexes by weight so that that lookup is log v, instead of v. This would give O(v log v)
- Creating the priority queue at the same time as the node graph (removing one of the terms discarded during the simplification)
- In the main loop, when the next node to visit is gotten, some time can be saved if multiple nodes have the same weight and one of those nodes is the destination node—but likely a small, maybe a mostly imperceptible win
- Using a different search algorithm

## Question 2

I want to try to figure this without doing any research.

I cannot think of a simpler representation for the city data than a grid. A grid is easy to debug and provides instant lookup.

Calculating the complexity…

- n &times; (the sum of terms i=1 through to k &times; 4)&sup2; for loading the data and inside the same loop: calculating the area and applying the area information to the city grid

So overall O(nk&sup2;) or O(n).

### Further possible optimisations

- The first k can probably be reduced to a lookup in most cases if the area calculations for each value of k is cached. The circumference coordinates could be saved as values relative to any centre—i.e., for a pizzeria at (0, 0)
- Possibly changing the code that calculates delivery areas from list comprehension to a more manual solution