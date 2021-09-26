# Task 1: Breadth-First Search

## _The Simplest Uninformed/Blind Search Algorithm_

### What We Expect from algorithm to do:

Implement the Breadth-First Search (BrFS) algorithm inside the `solve()`
function provided in the file [`brfs_search.py`](../brfs_search.py).
Remember, BrFS expands the shallowest node on the frontier, i.e. newly
generated nodes are placed on the frontier using a FIFO policy.

Implementation of BrFS needs to have **all** of the following properties:

1. It implements graph search rather than tree search.
2. It returns a **valid** sequence of actions: All moves are legal and the
   sequence of moves leads from the initial state to the goal.
3. It visits states in the **right** order (see the description of BrFS in the
   lectures)
4. It produces an **optimal** solution. i.e. the number of steps is minimal.

To get an idea of how fast your implementation should run, here are the times
of our solution (in development phase) on the three maps, `anuSearch`, `aiSearch` and `mazeSearch`:

| Problem    | Expanded | Time (secs) |
| ---------- | -------- | ----------- |
| anuSearch  | 285      | 0.01        |
| aiSearch   | 150      | 0.005       |
| mazeSearch | 270      | 0.01        |

The times above have been averaged over several runs. The measurements were
taken using Anaconda Python 3.6.3 on a 2.8 GHz Intel Core i7. Depending on the
order in which you explore the nodes, your number of expanded nodes might differ
from the above. This is perfectly okay, as long as you implement BrFS correctly.

You can test your implementation with the commands:

```sh
python3 red_bird.py -l search_layouts/anuSearch.lay -p SearchAgent -a fn=bfs
python3 red_bird.py -l search_layouts/aiSearch.lay -p SearchAgent -a fn=bfs
python3 red_bird.py -l search_layouts/mazeSearch.lay -p SearchAgent -a fn=bfs
```

Alternatively, if you're using Mac or Linux, you can run these shortcuts:

```sh
./test.sh bfs anuSearch
./test.sh bfs aiSearch
./test.sh bfs mazeSearch
```

### Hints

1. Remember that BrFS _expands_ the _shallowest_ nodes on the frontier.
2. In [frontiers.py](../frontiers.py) you will find a number of data
   structures readily available, and which may be useful for you to implement
   the appropriate frontier.
3. Be sure to avoid generating a path to the same state more than once.
4. In the code, you might also see some type annotations. For example:
   ```python
   def solve(problem: SearchProblem) -> List[str]:
       """Implement breadth first search."""
       # *** YOUR CODE HERE ***
   ```
   This means that the function `solve()` takes one parameter called `problem`
   which is a subclass of `SearchProblem`. This function should return a list
   of strings (where each string corresponds to a direction). In Python, these
   type annotations (e.g. `SearchProblem`, `List[str]`) are optional and Python
   will not check the types (unless you use [mypy](http://mypy-lang.org/)), but
   they might improve readability and makes debugging easier. Have a look at
   this [blog post](https://blog.florimondmanca.com/why-i-started-using-python-type-annotations-and-why-you-should-too)
   for more information.

Finished!!, you can move to the
[next section](4_iterative_deepening_search.md) or go back to the
[index](README.md).
