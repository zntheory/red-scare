import sys
import os
import signal

class TimeoutException(Exception): pass

def _on_timeout(signum, frame): raise TimeoutException()

signal.signal(signal.SIGALRM, _on_timeout)

TIMEOUT_SECONDS = 5 * 60

DATAPATH = os.listdir("data")

from algorithms.alternate import alternate
from algorithms.few import few
from algorithms.many import many, NegativeCycleException
from algorithms.none import none
from algorithms.some import some

def main():
  print("### Starting program! ###")

  if not (2 <= len(sys.argv) <= 3):
     print(f"Program expects 1 or 2 arguments but was given {len(sys.argv) - 1}")
     print(f"Usage: python3 main.py all OR python3 main.py <problem> <file>")
     sys.exit(1)

  problem = sys.argv[1]
  data = sys.argv[2] if len(sys.argv) == 3 else None

  # file traversal, who?
  # f = open(data, "r")

  if problem != "all" and data is None:
    print(f"Problem {problem} needs a data file")
    return

  if os.path.exists("results.txt"):
    os.remove("results.txt")

  match problem:
    case "alternate":
      with open(data, "r") as f:
        alternate(f)
    case "few":
      with open(data, "r") as f:
        few(f)
    case "many":
      with open(data, "r") as f:
        try:
          print(many(f))
        except NegativeCycleException as err: # found negative cycle - problem is NP-hard, so give up
          print(err)
    case "none":
      with open(data, "r") as f:
        none(f)
    case "some":
      with open(data, "r") as f:
        some(f)
    case "all":
      with open("results.txt", "a") as w:
        for file in DATAPATH:
          if file.endswith(".md"):
              continue
          with open("data/" + file, "r") as f:
            file_name = os.path.splitext(file)[0]
            n = int(f.readline().split()[0])
            f.seek(0)

            print("###",file,"###") # just to check where tf we are ;-;

            w.write(f"{file_name}, alternate, {n}, {alternate(f)}\n")
            f.seek(0)

            w.write(f"{file_name}, few, {n}, {few(f)}\n")
            f.seek(0)

            w.write(f"{file_name}, none, {n}, {none(f)}\n")
            f.seek(0)

            try:
              signal.alarm(TIMEOUT_SECONDS) # start timer
              many_res = many(f)
              signal.alarm(0) # stop timer cuz we didz it
              
              w.write(f"{file_name}, many, {n}, {many_res}\n")
              f.seek(0)
              
              w.write(f"{file_name}, some, {n}, {many_res > 0}\n")
              f.seek(0)
            except NegativeCycleException as err:
              w.write(f"{file_name}, many, {n}, !!\n")
              w.write(f"{file_name}, some, {n}, !!\n")
            except TimeoutException:
              w.write(f"{file_name}, many, {n}, ??\n")
              w.write(f"{file_name}, some, {n}, ??\n")
            finally:
              signal.alarm(0)

            #print("---")
    case _:
      print(f"Problem {problem} is not recognized!\nRecognized problems are \n-\"alternate\" \n-\"few\" \n-\"many\" \n-\"none\" \n-\"some\"\nTo (over)write the results.txt, use arg \"all\" (all problems, all data files).")
      return

if __name__ == '__main__':
    main()
