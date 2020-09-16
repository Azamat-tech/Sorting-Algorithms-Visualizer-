from code.view import Visualizer
from sortingalgorithms.all_algorithms import *

if __name__ == '__main__':
    a = [5,4,3,2,1]
    bubble.sort(a)
    print(a)
    app = Visualizer()
    app.main_loop()