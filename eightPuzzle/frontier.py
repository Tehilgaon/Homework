'''
implements a priority queue using a minimum heap
the heap is represented by a list
the parent of index i is in index (i-1)//2
the left child of index i is in index 2i+1
the right side of index i is in index 2i+2
'''
import state


class PQueue:
    f = []
    counterStates = 0
    maxStates = 0

    def __init__(self, s):
        self.create(s)

    def returnTotalStates(self):
        return self.counterStates

    def returnMaxStates(self):
        return self.maxStates

    def create(self, s):
        self.f = [s]
        return self.f  # returns a priority queue that contains s

    def getPQ(self):
        return self.f

    def is_empty(self):
        return self.f == []  # returns true iff f is empty list

    def insert(self, s):
        # inserts state s to the frontier
        self.counterStates += 1
        self.f.append(s)  # inserts the new state as the last item
        num = len(self.f)
        if num > self.maxStates:
            self.maxStates = num

        i = len(self.f) - 1  # i gets its value

        # move the item with smallest value to the root
        while i > 0 and self.val(self.f[i]) < self.val(
                self.f[(i - 1) // 2]):  # while item i's value is smaller than the value of his father, swap!
            # the next three lines swap i and his father
            t = self.f[i]
            self.f[i] = self.f[(i - 1) // 2]
            self.f[(i - 1) // 2] = t
            i = (i - 1) // 2  # i moves upwards

    def remove(self):  # remove and return the root of f
        if self.is_empty():  # underflow
            return 0
        s = self.f[0]  # store the root that should be returned
        self.f[0] = self.f[len(self.f) - 1]  # the last leaf becomes the root
        del self.f[-1]  # delete the last leaf
        self.heapify(self.f, 0)  # fixing the heap
        return s

    def lenOfPriorityQueue(self):
        return len(self.f)

    def val(self, s):  # returns path len + heuristic distance from target
        return state.hdistance(s) + state.path_len(s)

    def heapify(self, f, i):  # fix the heap by rolling down from index i
        minSon = i  # define i as minSon
        if 2 * i + 1 < len(f) and self.val(f[2 * i + 1]) < self.val(f[minSon]):  # if f[i] has a left son
            # and its left son is smaller than f[i]
            minSon = 2 * i + 1  # define the left son as minSon
        if 2 * i + 2 < len(f) and self.val(f[2 * i + 2]) < self.val(f[minSon]):  # if f[i] has a right son
            # and its right son is smaller than f[minSon]
            minSon = 2 * i + 2  # define the right son as minSon
        if minSon != i:  # if f[i] is bigger than one of its sons
            t = f[minSon]  # swap f[i] with the smaller son
            f[minSon] = f[i]
            f[i] = t
            self.heapify(f, minSon)  # repeat recursively



