## Approach

My experience with Python is limited to writing one [script](https://github.com/ivanmaeder/vimv) a long long time ago, and spending a [couple of afternoons](https://github.com/ivanmaeder/NLP) looking at the Natural Language Processing with Python book.

Still, I'm going with Python because I'm bound to learn a few things.

Please excuse the blunders.

I'm using:

- Python 3.7.2
- pytest-4.3.0

I have more experience with shortest path algorithms so I'm going to try the second problem first.

## Question 1

I think this is just a case of converting the data into a node graph and running one or more shortest path algorithms to find an optimal solution.



## Question 2

I want to try to figure this without doing any research.

I cannot think of a simpler representation for the city data than a grid. A grid is easy to debug and provides instant lookup.

Assuming that's correct, the optimisations must be in:

- Loading the data and processing it at the same time (not in separate steps)
- Keeping track of the value of the densest coordinate's value, instead of looking for it after processing all the data
- Improving the data processing efficiency through memoization or hardcoding

### Memoization or hardcoding

I think a gain might be had in not having to calculate the delivery area of every city, and so I could run those calculations once for every different value of K, and/or hardcode the circumference coordinates for a set of K.

The circumference coordinates could be saved as values relative to any centre—i.e., for a pizzeria at (0, 0).

This way, this calculation is reduced either completely (assuming **all** the circumference coordinates are hardcoded), or at least reduced.

In all cases some arithmetic will still be needed.

Performance tests would help figure out whether this is worth it, but that doesn't really change the fact that the solution will be O(n) at best.

### Further possible optimisations

- Caching the area of "duplicate" pizzerias—unlikely worth it, plus still O(n)
- Sorting pizzerias prior to processing—no longer O(n), additional complexity, dubious benefits
- Resizing the city grid to reduce memory usage—significantly more complex, more processing… may reduce performance and even then the memory usage may not be reduced at all

I don't think we do better than O(n).