import threading

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('Stared main')

    ints = read_ints('..\\data\\1Kints.txt')

    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t1.start()

    t1.join()
    print('Ended main')
