import threading

lock_obj = threading.RLock()

# DEADLOCK
#
# print('Acquire 1st time')
# lock_obj.acquire()
#
# print('Acquire 2st time')
# lock_obj.acquire()
#
# print('Releasing')
# lock_obj.release()

# Тоже DEADLOCK
# Лечится созданием не LOCK а RLock
# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('Acquired')
#     reentrance()
#
#
# reentrance()
