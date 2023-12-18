# class A():

#     def __init__(self, name):
#         self.fist_name = name
    
#     @property
#     def name(self):
#         return self.fist_name
    

#     @name.setter
#     def name(self, val):
#         self.fist_name = val
    
#     @name.deleter
#     def name(self):
#         self.fist_name = None

# b = A("Bhushan")

# b.name = "Ram"

# print(b.name)

# class A():
#     leave_remaining = 30

#     @classmethod
#     def change_leave(cls, val):
#         cls.leave_remaining = val

# b = A()

# print(b.leave_remaining)
# b.change_leave(10)
# print(b.leave_remaining)


# try:
#     a = open(r"E:\django-task\Ecommerce_web_shopping\file.txt",'+w')

#     a.write("Bhushan")

# finally:
#     a.close()

# li = [1,2,4,5,6,7]
# for i in li:
#     if i%2 != 0:
#         raise Exception("i is divided by 2",i)
#     else:   
#         print("excecution is normal")


# class Agevalidation(BaseException):

#     def __init__(self, msg):
#         self.msg = msg



# Age = int(input("Enter your age!!"))

# if Age < 18:
#     raise Agevalidation("Your are Not Eligible to Vote")

# print('You are Eligible to vote')

# def outer(fun):

#     def inner(a,b):
#         if b == 0:
#             raise Exception("a is not divisible by ", b)
        
#         else:
#             fun(a,b)

#     return inner

# @outer
# def division(a,b):
#     print(a/b)

# division(10,1)

# class A():
#     def __init__(self, fun):
#         self.fun = fun

#     def __call__(self, *args, **kwargs ):

#         if kwargs.get("b") == 0:
#             raise Exception("zero is not divisible by ")
        
#         return self.fun(*args, **kwargs)

# @A
# def m1(a,b):
#     return a/b

# print(m1(10,0))



# class B:
    
#     @A
#     def m1(self,a, b):
#         return a/b

# b = B()

# print(b.m1(10,0))

# class Deco():

#     def __init__(self, fun):
#         self.fun = fun

#     def __call__(self,*args, **kwargs):
#         if kwargs.get("b") == 0:
#             raise Exception("Zero devision is not possible")
#         return self.fun(*args, **kwargs)

# class A:

#     @Deco()
#     def m1(self, a, b):
#         return a/b
    

# c = A()
# print(c.m1(10,0))

# class Deco:

#     def __init__(self, fun):
#         self.fun = fun

#     def __call__(self, *args, **kwargs):
#         if kwargs.get("b") == 0:
#             raise Exception("Zero division is not possible")
#         return self.fun(*args, **kwargs)

# class A:

#     @Deco()
#     def m1(self, a, b):
#         return a / b

# c = A()
# print(c.m1(10, 0))  # This will raise an exception due to division by zero



# class A:

#     def __init__(self, fun):
#         self.fun = fun

    
#     def __call__(self, a, b):
        
#         if (b == 0):
#             raise Exception("Zero is not divisible")
        
#         return self.fun(a,b)


# class B():

#     @A()
#     def m1(self, a, b):
#         return a/b
    
# c = B()
# print(c.m1(10,1))



# Evaluation = lambda marks: "A+" if marks>=90 else( "A" if marks >=75 else ( "B" if marks >= 60 else( "c" if marks >= 50 else ("Pass" if marks >=40 else "fail"))))

# print(Evaluation(95))


# li = [1,2,3,4,5]
# fun = list(map( lambda a : a*2, li))
# print(fun)

# li = (1,2,3,4,5,6)
# fun = tuple(filter(lambda a: a>=3,li))
# print(fun)


# from functools import reduce
# li = (1,2,3,4,5,6)
# def add(x,y):
#     print(x,"****",y)
#     return x+y
# sum1 = reduce(add, li)
# print(sum1)

# class Num:
#     def __init__(self, start, stop, step):
#         self.start = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         value = self.start

#         if self.start >= self.stop:
#             raise StopIteration("sequence Exhausted")
        
#         self.start += self.step

#         return value
    
# obj = Num(0,11,2)

# print(next(obj))
# print(next(obj))
# print(next(obj))


# def num():

#     for i in range(0,11,2):

#         yield i

# a = num()
# print(a.__next__())
# print(a.__next__())

# from threading import Thread, current_thread

# print("program **** start", current_thread().name)

# def m1():

#     print("function start", current_thread().name)

#     print("function ends", current_thread().name)


# print("end program", current_thread().name)

# t1 = Thread(target=m1, name='thread_1')
# t1.start()

# from threading import current_thread, Thread, Lock

# l = Lock()

# class Num(Thread):

#     def even(self, start, stop, stepp):

#         l.acquire

#         for i in range(start, stop, stepp):
#             print(i, current_thread().name)
#         l.release()
    
#     def odd(self, start, stop, stepp):

#         for i in range(start, stop, stepp):
#             print(i, current_thread().name)

# B = Num()

# t1 = Thread(target=B.even, args=(0,10,2), name='even_thread')

# t2 = Thread(target=B.odd, args=(1,10,2), name="odd")

# t1.start()
# # t1.join()
# t2.start()