from frontier import PQueue
import state
 # Tehila Gaon 315136952

def search(n):
    trys = 0
    f = PQueue(state.create(n))
    # f = frontier1.create(state.create(n))
    while not (f.is_empty()):
        s = f.remove()
        # print (s)
        if state.is_target(s):
            return [s, f.returnTotalStates(), f.returnMaxStates()]
        else:
            trys += 1
        ns = state.get_next(s)
        for i in range(0, len(ns)):
            f.insert(ns[i])
    return None


def main():
    ans = search(2)
    print(ans)
    print("Number of trys:", ans[1])
    print("Max size of pqueue:", ans[2])
    ans = search(3)
    print(ans)
    print("Number of trys:", ans[1])
    print("Max size of pqueue:", ans[2])
    ans = search(4)
    print(ans)
    print("Number of trys:", ans[1])
    print("Max size of pqueue:", ans[2])


if __name__ == "__main__":
    main()
