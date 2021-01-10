import statistics
import random
from math import fsum
import time
import math


def test(f1, std, num_repetitions, len_input, range1, range2):
    r1 = list()
    r2 = list()
    past1 = 0
    past2 = 0
    avg1 = 0
    avg2 = 0
    abserror1 = list()
    absrelerror1 = list()
    avgabserror1 = 0
    avgabsrelerror1 = 0
    diff = 0
    input = list()

    for y in range(len_input):
        input.append(random.uniform(range1, range2))
    # toc = time.perf_counter()
    # print(toc - tic)
    past1 = f1(input)
    past2 = std(input)
    if past1 != past2:
        diff = diff + 1
    past3 = abs(past1 - past2)
    past4 = past3/past2
    for x in range(num_repetitions - 1):
        #tic = time.perf_counter()
        for y in range(len_input):
            input.append(random.uniform(range1, range2))
        #toc = time.perf_counter()
        #print(toc - tic)
        a = f1(input)
        b = std(input)
        if a != b:
            diff = diff + 1
        c = abs(b - a)
        d = c / b
        abserror1.append(abs(b - a))
        absrelerror1.append(abserror1[-1]/b)
        input.clear()
        avg1 = statistics.mean([past1, a])
        avg2 = statistics.mean([past2, b])
        avgabserror1 = statistics.mean([past3, c])
        avgabsrelerror1 = statistics.mean([past4, d])
        past1 = a
        past2 = b
        past3 = c
        past4 = d

    print("f1: ", f1.__name__)
    print("std: ", std.__name__)
    print("number of repetitions: ", num_repetitions)
    print("list length: ", len_input)
    print("range: ", range1, range2)

    print("average ", str(f1.__name__), avg1)
    print("average ", str(std.__name__), avg2)

    print(diff, "different results out of", num_repetitions)

    print(f"average absolute error for {str(f1.__name__)} is {str(avgabserror1)}")
    print("average absolute relative error for ", str(f1.__name__), str(avgabsrelerror1))


test(sum, fsum, 10000, 500, -20000000, 20000000)

