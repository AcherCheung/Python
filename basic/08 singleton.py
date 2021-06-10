import time
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance



class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name
        time.sleep(1)


def task(arg):
    obj = Foo(arg)
    print(obj, obj.name)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()


