from datetime import datetime
from multiprocessing import Pool, current_process, cpu_count

start = datetime.now()
def factor(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result
def factorize(*numbers):

    with Pool(cpu_count()) as pool:
        mapped = pool.map(factor,  [num for num in numbers])
    return mapped


if __name__ == '__main__':
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    finish = datetime.now()
    print(a, b, c, d)
    print(f'time  execute {finish - start}')
