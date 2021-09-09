<h1 align="center">PyRival</h1>
<div align="center">
  <strong>A Python Library for Competitive Programming</strong>
</div>

<h3 align="center">Developers</h3>
<div align="center">
  <strong>
    <a href="https://github.com/Mukundan314">Mukundan314</a> &emsp;
    <a href="https://github.com/bjorn-martinsson">pajenegod</a> &emsp;
    <a href="https://github.com/eduard-netsajev">drd93</a> &emsp;
    <a href="https://github.com/algmyr">algmyr</a> &emsp;
    <a href="https://github.com/meooow25">meooow</a> &emsp;
    <a href="https://github.com/tfg50">tfg</a> &emsp;
    <a href="https://github.com/sgtlaugh">sgtlaugh</a> &emsp;
    <a href="https://github.com/abertell">abertell</a> &emsp;
  </strong>
</div>

---

### Templates
- The [Master Template](templates/template.py) works with all versions of Python and has Python 3 behaviour.
- Version Specific Templates: [PyPy 2](templates/template_pypy2.py), [Python 3](templates/template_py3.py)

##

### Tools
- [Interactive Runner](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/tools/interactive_runner.py)
- [Stress Tester](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/tools/stress_tester.py)

##

### Snippets
<details>
  <summary>Algebra</summary>

  - [(Multivariable) Chinese Remainder Theorem](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/chinese_remainder.py)
  - [Discrete Logarithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/discrete_log.py)
  - [LCM and GCD](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/gcd.py)
  - [Integer Factorization](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/factors.py)
  - [Fast Fourier Transform](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/fft.py)
  - [Fast Subset Transform](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/fst.py)
  - [Number Theoretic Transform](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/ntt.py)
  - [Deterministic Miller-Rabin Primality Test](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/is_prime.py)
  - [Tonelli–Shanks Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/mod_sqrt.py)
  - [Generalized Modular Inverse](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/modinv.py)
  - [Euler's Phi Function](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/phi.py)
  - [Primitive Root](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/primitive_root.py)
  - [Sieve of Eratosthenes](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/sieve.py)
</details>

<details>
  <summary>Data Structures</summary>

  - [Bit Array](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/BitArray.py)
  - [Binary Indexed (Fenwick) Tree](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/FenwickTree.py)
  - [Fractions](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Fraction.py)
  - [Continued Fractions](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/CFraction.py)
  - [Disjoint-Set (Union Find) Data Structure](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/DisjointSetUnion.py)
  - [Generic Nodes](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Node.py)
  - [Linked List](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LinkedList.py)
  - [Range Query Data Structure](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py)
  - [(Lazy) Segment Tree](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LazySegmentTree.py)
  - [Persistent Segment Tree](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/PersistentSegTree.py)
  - [Sorted List](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SortedList.py)
  - [Treap](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Treap.py)
  - [Trie Tree](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py)
  - [2-satisfiability Template](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/TwoSat.py)
</details>

<details>
  <summary>Geometry</summary>

  - [Convex Hull](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/convex_hull.py)
  - [Line Functions](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/lines.py)
  - [Polygon Functions](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/polygons.py)
  - [Vector Functions](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/vectors.py)
</details>

<details>
  <summary>Graphs</summary>

  - [Bellman-Ford Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/bellman_ford.py)
  - [Breadth First Search](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/bfs.py)
  - [Connected Components Search](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/components.py)
  - [Brent's Algorithm for Cycle Detection](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/cycle_finding.py)
  - [Depth First Search](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dfs.py)
  - [Dijkstra's Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dijkstra.py)
  - [Eulerian Path](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/euler_walk.py)
  - [Path Constructor](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/find_path.py)
  - [Floyd-Warshall Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/floyd_warshall.py)
  - [Bipartite Graph Check](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/is_bipartite.py)
  - [Kruskal's Algorithm with Disjoin Set Union](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/kruskal.py)
  - [Prim's Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/prim.py)
  - [Tarjan's Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/scc.py)
  - [Topological Sorting](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/toposort.py)
</details>

<details>
  <summary>Combinatorics</summary>

  - [General Purpose Numbers](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/combinatorics/combinatorics.py)
  - [Lucas's Theorem](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/combinatorics/nCr_mod.py)
  - [Partition Function](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/combinatorics/partitions.py)
</details>

<details>
  <summary>Linear Algebra</summary>

  - [Matrix Arithmetic, Exponentiation, Determinant, and Inverse](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/linear_algebra/matrix.py)
  - [Gaussian Elimination](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/linear_algebra/max_xor.py)
  - [Multivariable Chinese Remainder Theorem](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/linear_algebra/multivariable_crt.py)
</details>

<details>
  <summary>Numerical</summary>

  - [Linear Recurrence Template](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/berlekamp_massey.py)
  - [Hill Climbing Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/hill_climbing.py)
  - [Approximate Integration](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/integrate.py)
  - [Polynomial Interpolation](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/interpolate.py)
  - [Integer Roots](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/iroot.py)
  - [Binary Search](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/numerical/search.py)
</details>

<details>
  <summary>Strings</summary>

  - [Knuth–Morris–Pratt Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/kmp.py)
  - [Longest Common/Palindromic Subsequences](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/lcs.py)
  - [Longest Common Substring](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/LCSubstr.py)
  - [Longest Palindromic Substring](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/LPSubstr.py)
  - [Manacher's Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/suffix_array.py)
  - [Lydon Factorization](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/min_rotation.py)
  - [Z Algorithm](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py)
</details>


<details>
  <summary>Misc</summary>

  - [bootstrap for recursion](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py)
  - [FastIO](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/FastIO.py)
  - [heapq](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Heap.py)
  - [sorted](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/ordersort.py)
  - [py3k compatibility tools](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/py3k.py)
  - [random](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/Random.py)
  - [str.split for whitespace](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/split.py)
  - [Bit Hacks](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bit_hacks.py)
  - [32-bit Modular Arithmetic](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/mod.py)
  - [Memoize Decorators](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/memoize.py)
  - [C++ syle cout](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/ostream.py)
  - [Interactive Runner](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/tools/interactive_runner.py)
  - [Stress Tester](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/tools/stress_tester.py)
  - [Alpha–Beta Pruning](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/alphabeta.py)
  - [Longest Increasing Subsequence](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/lis.py)
  - [K-th Order Statistic](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/order_statistic.py)
</details>
