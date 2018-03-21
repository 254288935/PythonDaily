# coding:utf-8
"""
python 线程练习
"""
import threading
import time

# # condition 生产者消费者模式
# product = None
# con = threading.Condition()
#
# def produce():
#     global product
#     if con.acquire():
#         while True:
#             if product is None:
#                 print 'produce...'
#                 product = 'spam'
#                 time.sleep(2)
#                 con.notify()
#             con.wait()
#             time.sleep(2)
#
# def consume():
#     global product
#     if con.acquire():
#         while True:
#             if product is not None:
#                 print 'consume'
#                 product = None
#                 time.sleep(1)
#                 con.notify()
#             con.wait()
#             time.sleep(2)
#
# t1 = threading.Thread(target=produce)
# t2 = threading.Thread(target=consume)
# t1.start()
# t2.start()













# # 计数器初值为2
# semaphore = threading.Semaphore(2)
#
# def func():
#
#     # 请求Semaphore，成功后计数器-1；计数器为0时阻塞
#     print '%s acquire semaphore...' % threading.currentThread().getName()
#     if semaphore.acquire():
#
#         print '%s get semaphore' % threading.currentThread().getName()
#         time.sleep(4)
#
#         # 释放Semaphore，计数器+1
#         print '%s release semaphore' % threading.currentThread().getName()
#         semaphore.release()
#
# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t3 = threading.Thread(target=func)
# t4 = threading.Thread(target=func)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#
# time.sleep(2)











# event = threading.Event()
#
# def func():
#     # 等待事件，进入等待阻塞状态
#     print '%s wait for event...' % threading.currentThread().getName()
#     event.wait()
#
#     # 收到事件后进入运行状态
#     print '%s recv event.' % threading.currentThread().getName()
#
# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t1.start()
# t2.start()
#
# time.sleep(2)
#
# # 发送事件通知
# print 'MainThread set event.'
# event.set()








local = threading.local()
local.tname = 'main'

def func():
    local.tname = 'notmain'
    print local.tname

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print local.tname