from view.view import Visualizer
from sortingalgorithms.all_algorithms import *
from exceptions.sorting_algorithm_missing import SortingAlgorithmNotFoundError, getErrorMessage

class ArraySort:

    def __init__(self, array):
        self.sortEvalDictionary = { "bubble" : bubble,
                                    "insertion" : insertion,
                                    "merge" : merge,
                                    "selection" : selection,
                                    "quick" : quick,
                                    "heap" : heap
        }
        self.array = array

    def sort(self, sortType):
        a = self.sortEvalDictionary.get(sortType)
        if not a :
            print()
            raise SortingAlgorithmNotFoundError(getErrorMessage(sortType))
        a.sort(self.array)
    
    def __repr__(self):
        return f"{self.array}"

if __name__ == '__main__':
    a = ArraySort([5, 4, 3, 2, 1])
    a.sort("bubbles") #replace this with a key from the dictionary to see sorted values
    print(a)
    app = Visualizer()
    app.main_loop()