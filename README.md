# [GoogleCodeJam Farewell Rounds](https://codingcompetitions.withgoogle.com/codejam/archive/2023)

![Language](https://img.shields.io/badge/language-Python3-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
![Progress](https://img.shields.io/badge/progress-20%20%2F%2020-ff69b4.svg)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.googlecodejam.farewell.rounds)

* Python solutions of Google Code Jam Farewell Rounds. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8` is not friendly for Python to solve in 5 ~ 15 seconds.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

## Rounds

* [Kick Start 2022](https://github.com/kamyu104/GoogleKickStart-2022)
* [Code Jam 2022](https://github.com/kamyu104/GoogleCodeJam-2022)
* [Round A](https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds#round-a)
* [Round B](https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds#round-b)
* [Round C](https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds#round-c)
* [Round D](https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds#round-d)

## Round A

- Round A is appropriate for beginners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Colliding Encoding](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf)| [Python3](./Round%20A/colliding_encoding.py3)| _O(N)_ | _O(N)_ | Easy | | Hash Table |
|B| [Illumination Optimization](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086)| [Python3](./Round%20A/illumination_optimization.py3) | _O(N)_ | _O(1)_ | Medium | | Greedy |
|C| [Rainbow Sort](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cada38)| [Python3](./Round%20A/rainbow_sort.py3)| _O(N)_ | _O(N)_ | Easy | | Hash Table |
|D| [ASCII Art](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c2)| [Python3](./Round%20A/ascii_art.py3) | _O(1)_ | _O(1)_ | Easy | | Math |
|E| [Untie](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad9c1)| [Python3](./Round%20A/untie.py3) | _O(N)_ | _O(1)_ | Medium | | Greedy |

## Round B

- Round B is about the level of a Kick Start round or a Code Jam Round 1.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Collecting Pancakes](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad7d1)| [Python3](./Round%20B/collecting_pancakes.py3)| _O(N)_ | _O(1)_ | Medium | | Greedy, Prefix Sum |
|B| [Intruder Outsmarting](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d)| [Python3](./Round%20B/intruder_outsmarting.py3) | _O(W * log(min(D, N)))_ | _O(1)_ | Medium | | Extended Euclidean Algorithm  |
|C| [Spacious Sets](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad2ce)| [Python3](./Round%20B/spacious_sets.py3) | _O(NlogN)_ | _O(N)_ | Easy | | Binary Search, DP|
|D| [Railroad Maintenance](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad77d)| [PyPy3](./Round%20B/railroad_maintenance.py3) | _O(N + L)_ | _O(N + L)_ | Hard | | DFS, Biconnected Components, Articulation Points |
|E| [Railroad Management](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000caccfb)| [Python3](./Round%20B/railroad_management.py3) | _O(N)_ | _O(N)_ | Hard | | Graph, Cycle |

## Round C

- Round C is harder than a Code Jam Round 2 but easier than a Code Jam Round 3.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Game Sort: Part 1](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cacb87)| [Python3](./Round%20C/game_sort_part_1.py3)  | _O(P * L)_ | _O(1)_ | Easy | | Greedy, Counting Sort, Freq Table |
|B| [Immunization Operation](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cacb88)| [Python3](./Round%20C/immunization_operation.py3)  |  _O(M + VlogV)_ | _O(V)_  | Easy | | Simulation, Heap |
|C| [Evolutionary Algorithms](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad08b)| [PyPy3](./Round%20C/evolutionary_algorithms.py3) | _O(NlogN)_  |  _O(N)_ | Medium | | DFS, BIT, Fenwick Tree, Coordinate Compression, Combinatorics |
|D| [The Decades of Coding Competitions](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad9c6)| [PyPy3](./Round%20C/the_decades_of_coding_competitions.py3) | _O(K * (N + M + Q))_  |  _O(K * N)_ |  Medium | | Graph, Union Find, DSU |
|E| [Game Sort: Part 2](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad339)| [Python3](./Round%20C/game_sort_part_2.py3) | _O(N)_ | _O(1)_ | Hard | ❤️ | Constructive Algorithms, Prefix Sum, Freq Table, Greedy |

## Round D

- Round D is meant for experienced competitors. It is between a Code Jam Round 3 and Finals difficulty.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Indispensable Overpass](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cadc76)| [Python3](./Round%20D/indispensable_overpass.py3) | _O(W + E + C)_ | _O(W + E)_  | Easy | | Tree DP, Combinatorics |
|B| [Genetic Sequences](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cadc77)| [PyPy3](./Round%20D/genetic_sequences.py3) [PyPy3](./Round%20D/genetic_sequences2.py3) | _O((N + M) * log(N + M) + Q * log(min(N, M)) * logN)_ | _O((N + M) * log(N + M))_ | Medium | | Suffix Array, LCP Array, Binary Search, RMQ, Sparse Table, Persistent BST, Persistent Treap |
|C| [Hey Google, Drive!](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000caccfa)| [PyPy3](./Round%20D/hey_google_drive.py3) | _O((R * C)^2 * F)_ | _O(R * C)_  | Hard | ❤️ | Graph, BFS |
|D| [Old Gold](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cada3b)| [PyPy3](./Round%20D/old_gold.py3) | _O(NlogN)_ | _O(N)_ | Hard | ❤️ | Combinatorics, DP, Prefix Sum |
|E| [Ring-Preserving Networks](https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b95/0000000000cad08a)| [Python3](./Round%20D/ring_preserving_networks.py3) | _O(L)_ | _O(L)_ | Medium | | Graph, Constructive Algorithms, Clique |
