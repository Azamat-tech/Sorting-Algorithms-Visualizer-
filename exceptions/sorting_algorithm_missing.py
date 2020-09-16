
def getErrorMessage(sortType):
    return f"{sortType} sort has not been defined yet. "\
            "Add the algorithm to the sortingalgorithms/ directory, "\
            f"import it in the all_algorithms.py file and add the dictionary. \n"

class SortingAlgorithmNotFoundError(Exception):
    __module__ = Exception.__module__