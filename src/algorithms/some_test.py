import unittest
from algorithms.some import some
import os



class TestSome(unittest.TestCase):
    #All input files
    input_files = os.listdir("data") 


    # TESTS
    # to run use command from algorithms folder
    # python3 -m unittest few_test.py

    def test_run_all(self):
        #print(self.input_files)
        with open("test_solutions/solutions.txt", "r") as sol:

            #Gather all the known solutions from data/solutions.txt
            list_of_solutions = sol.readlines()
            solution_check = dict()
            for s in list_of_solutions:
                file, typ, res = s.split()
                solution_check[file] = dict()
                solution_check[file][typ] = int(res)

            possible = 0
            impossible = 0
            for i in range(len(self.input_files)):
                if self.input_files[i] != "README.md":
                    print("### Running test for file:",self.input_files[i],"###")
                    with open("data/"+str(self.input_files[i]), "r") as f:
                        try:
                            result = some.some(f)
                            print("Gave result:", result)
                            possible+=1
                        except:
                            print("Unsolvable")
                            impossible+=1

            print("Total amount of possible problems:", possible)
            print("Total amount of impossible problems:",impossible)
                           

