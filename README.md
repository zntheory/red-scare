# Red Scare [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/) [![licenseMIT](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/MIT)
> [!Note]
> This is a repository of a hand-in assignment called [Red Scare](https://github.com/thorehusfeldt/algdes-labs/tree/master/red-scare), with exercises designed by [Thore Husfeldt](https://github.com/thorehusfeldt), for the course Algorithm Design @ IT University of Copenhagen (2026).


### Installation

**Requirements**
- Python [3.14.4](https://www.python.org/downloads/release/python-3144/)

_**Note** that there are currently no releases._

```bash
git clone git@github.com:zntheory/red-scare.git
```

### Usage

Run the application:

```bash
cd src
python3 main.py all
```

The above command will output `results.txt` in the `src` directory.

### How to read results.txt

The `results.txt` file can be read similarly to a `csv` file, that is using a comma to seperate items, but without a header.

If we were to add a header and format it as a table, it would look like the following...

| Instance      | Problem       | n             | Result               |
| ------------- | ------------- | ------------- | -------------        |
|  graph i      | alternate     | int           | Bool                 |
|  graph i      | few           | int           | int                  |
|  graph i      | none          | int           | int                  |
|  graph i      | many          | int           | int \| string        |
|  graph i      | some          | int           | Bool \| string       |
|  graph i+1    | alternate     | int           | Bool                 |
...

#### Context

- `alternate` has the objective to return true if there is a path from source $s$ to sink $t$ that alternates between red and non-red vertices. Otherwise, return false.
  - Therefor, it will return a boolean, true or false.
- `few` has the objective to return the minimum number of red vertices on any path from source $s$ to sink $t$.
  - Therefor, it will return a positive integer, or $-1$ to denote no such path exists.
- `none` has the objective to return the length of a shortest $s,t$-path internally avoiding red vertices.
  - Therefor, it will return a positive integer, or $-1$ to denote no such path exists.
- `many` has the objective to return the maximum number of red vertices on any path from source $s$ to sink $t$.
  - Therefor, it will return a positive integer, or ...
  - string $??$ to denote that our solution was unable to solve the problem within 5 minutes, or ...
  - string $!!$ to denote that our solution detected a negative cycle in the graph, for which our implementation is unable to find a solution in polynomial time.
- `some` has the objective to return true if there is a path from source $s$ to sink $t$ that includes at least one red vertex. Otherwise, return false.
  - Therefor, it will return a boolean, true or false, or ...
  - string $??$ to denote that our solution was unable to solve the problem within 5 minutes, or ...
  - string $!!$ to denote that our solution detected a negative cycle in the graph, for which our implementation is unable to find a solution in polynomial time.
