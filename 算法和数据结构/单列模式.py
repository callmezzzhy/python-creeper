from single import c

class single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=object.__new__(cls,*args,*kwargs)
        return cls._instance
class A(single):
    a=1

def sing(cls,*args,**kwargs):
    isinstances={}
    def _singel():
        if cls not in  isinstances:
            isinstances[cls]=cls(*args,**kwargs)
        return isinstances[cls]
    return _singel()

@sing
class B(object):
    b=3


