from collections import Counter
from timeit import default_timer as timer
import multiprocessing as mp

def split_integer_parts(n, k):
    parts = n % (10 ** k)
    n //= 10 ** k
    while n > 0:
        if parts != n % (10 ** k):
            return False
        n //= 10 ** k
    return True


def get_sum_invalid(x, part_map):
    num = x.split('-')
    invalid_ids = []

    for n in range(int(num[0]), int(num[1]) + 1):
        n_len = len(str(n))
        for j in part_map[n_len]:
            if split_integer_parts(n, j):
                invalid_ids.append(n)
                break
    return sum(invalid_ids)

if __name__ == '__main__':
    part_map = {}
    for i in range(1,100):
        part_map[i] = []
        for j in range(1,i):
            if i % j == 0 and j < i:
                part_map[i].append(j)

    with (open("./input", "r") as file):
        inputs = [line.strip() for line in file.readlines()][0].split(',')
        location = 0
        total = len(inputs)
        args = [(x, part_map) for x in inputs]
        with mp.Pool() as pool:
            invalid_ids = pool.starmap(get_sum_invalid, args)

            # print(f"{location}/{total}")
            # location += 1


    print(sum(invalid_ids))
