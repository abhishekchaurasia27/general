def reversed_args(f):
    def inner(*args, **kargs):
        l = []
        for i in args:
            l.append(i)
        for k,v in kargs.items():
            l.append((k,v))
        l.reverse()
        return f(*l)
