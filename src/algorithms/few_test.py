import unittest
import few
import os



class TestFew(unittest.TestCase):
    #All input files
    input_files = os.listdir("../data") 


    # TESTS
    # - run()

    def test_run_all(self):
        #print(self.input_files)
        with open("../data/solutions.txt", "r") as sol:

            #Gather all the known solutions from data/solutions.txt
            list_of_solutions = sol.readlines()
            solution_check = dict()
            for s in list_of_solutions:
                file, typ, res = s.split()
                solution_check[file] = dict()
                solution_check[file][typ] = int(res)


            for i in range(len(self.input_files)):
                if self.input_files[i] != "README.md" and self.input_files[i] != "solutions.txt":
                    print("### Running test for file:",self.input_files[i],"###")
                    with open("../data/"+str(self.input_files[i]), "r") as f:
                        result = few.few(f)
                        if self.input_files[i] in solution_check and "few" in solution_check[self.input_files[i]]:
                            self.assertEqual(result,solution_check[self.input_files[i]]["few"])
                            print("Found a solution with result",result)
                        else:
                            print(result)

