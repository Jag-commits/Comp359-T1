import time
import random
from implementations.registry import UF_REGISTRY


#Measure timings of each implementation
def timing_test(uf_class, n, num_ops):
    #Generate random pairs of nodes
    ops = [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(num_ops)]

    #Create a Union Find object using the current implementation
    uf = uf_class(n)

    #This tests how long it takes to connect many random pairs
    start_union = time.perf_counter()
    for p, q in ops:
        uf.union(p, q)
    end_union = time.perf_counter()

    #This tests how long it takes to locate roots after the unions have been made
    start_find = time.perf_counter()
    for p, q in ops:
        uf.find(p)
        uf.find(q)
    end_find = time.perf_counter()

    #Calculate the total times
    union_time = end_union - start_union
    find_time = end_find - start_find

    return union_time, find_time


#Using a chain stucture to test a worst case scenario for the implementations 
def worst_case_test(uf_class, n):
    #Create a Union Find object with n elements
    uf = uf_class(n)

    #Create a chain structure
    #This is a bad case for weaker Union Find implementations
    start_union = time.perf_counter()
    for i in range(n - 1):
        uf.union(i, i + 1)
    end_union = time.perf_counter()

    #Measure Find after the chain has been created
    #This shows how well each implementation handles deep structures
    start_find = time.perf_counter()
    for i in range(n):
        uf.find(i)
    end_find = time.perf_counter()

    return end_union - start_union, end_find - start_find


def main():
    #Display results of the tests

    print()
    print("TIMING TESTS:")

    #Run three input sizes to compare performance as the data grows
    test_sizes = [
        ("SMALL INPUT TEST", 200, 200),
        ("MEDIUM INPUT TEST", 1000, 1000),
        ("LARGE INPUT TEST", 10000, 10000)
    ]

    #Loop through each test size
    for test_name, n, num_ops in test_sizes:
        print()
        print(test_name)

        #Run the same timing test on each Union Find implementation
        for name, uf_class in UF_REGISTRY.items():
            union_t, find_t = timing_test(uf_class, n, num_ops)
            print(name)
            print("Union time:", union_t)
            print("Find time:", find_t)
            print()

    print()
    print("WORST CASE TEST:")
    n = 5000

    #Run the worst case test on each implementation (Chain Structur)
    for name, uf_class in UF_REGISTRY.items():
        union_t, find_t = worst_case_test(uf_class, n)
        print(name)
        print("Chain union time:", union_t)
        print("Find all time:", find_t)


if __name__ == "__main__":
    main()