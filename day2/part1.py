

if __name__ == '__main__':

    inputs = ""
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()][0].split(',')
        invalid_ids = []
        print(inputs)
        for x in inputs:
            num = x.split('-')
            for n in range(int(num[0]), int(num[1])+1):
                for i in range(len(str(n))):
                    if len(str(n)) % 2 == 1:
                        print(n)
                    elif int(str(n)[:int(len(str(n))/2)]) == int(str(n)[int(len(str(n))/2):]):
                        invalid_ids.append(int(n))

print(sum(invalid_ids))