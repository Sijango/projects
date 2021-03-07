import threading
import time

from multithreading.count_three_sum import read_ints

should_stop = False


def count_three_sum(ints, thread_name='t'):
    print(f'started count_three_sum in {thread_name}\n')

    n = len(ints)
    counter = 0
    # Специально медленный алгоритм)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if should_stop:
                    print('Task was Cancelled')
                    return counter

                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')

    print(f'ended count_three_sum in {thread_name}. Triplets counter={counter}')
    return counter


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')

    p = threading.Thread(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(5)

    should_stop = True

    time.sleep(2)

    print('ended main')