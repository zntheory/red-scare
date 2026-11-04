import sys
import os

DATAPATH = os.path.dirname(os.path.realpath("data/*.txt"))

from algorithms.alternate import alternate
from algorithms.few import few
from algorithms.many import many
from algorithms.none import none
from algorithms.some import some

def main():
  print("### Starting program! ###")

  if len(sys.argv) != 3:
     print(f"Program expects 2 arguments but was given {len(sys.argv) - 1}")
     print(f"Usage: python3 <problem> <data>")
     return

  problem = sys.argv[1]
  data = sys.argv[2]

  # file traversal, who?
  f = open(data, "r")

  match problem:
    case "alternate":
      alternate(f)
    case "few":
      few(f)
    case "many":
      many(f)
    case "none":
      none(f)
    case "some":
      some(f)
    case "*":
      alternate(f)
      f.seek(0)
      few(f)
      f.seek(0)
      many(f)
      f.seek(0)
      none(f)
      f.seek(0)
      some(f)
      f.seek(0)
    case _:
      print(f"Problem {problem} is not recognized!\nRecognized problems are \"alternate\", \"few\", \"many\", \"none\", \"some\", and \"*\" (all problems)")
      return

  f.close()

if __name__ == '__main__':
    main()