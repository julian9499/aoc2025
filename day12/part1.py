from typing import List, Dict, Tuple

SHAPE_SIZES = [5, 7, 6, 7, 7, 7]

if __name__ == '__main__':
    inputs: List[str] = []
    with open('./input', 'r') as file:
        inputs = [line.strip() for line in file.readlines()]
        count = 0
        for line in inputs:
            if ': ' in line and 'x' in line:
                size, present_counts = line.split(': ')
                width, height = map(int, size.split('x'))
                counts = list(map(int, present_counts.split()))

                region_area = width * height
                total_present_area = sum(n * size for n, size in zip(counts, SHAPE_SIZES))

                if total_present_area <= region_area:
                    count += 1

        print(count)
