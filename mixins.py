# http://sebulba.wikispaces.com/recipe+real+mixins
import inspect

def plugImport(name):
    '''Borrowed from python tutorial, does basic importing, I believe'''
    #name = "plugins/" + name
    mod = __import__("plugins/" + name)
    components = name.split('.')
    print components
    for comp in components[1:]:
      mod = getattr(mod, comp)
      print "module=", comp, mod
    return mod

def mixin(cls):
    """
    mixes-in a class (or a module) into another class. must be called from within
    a class definition. `cls` is the class/module to mix-in
    """
    locals = inspect.stack()[1][0].f_locals
    if "__module__" not in locals:
        raise TypeError("mixin() must be called from within a class definition")
    
    # copy the class's dict aside and perform some tweaking
    dict = cls.__dict__.copy()
    dict.pop("__doc__", None)
    dict.pop("__module__", None)
    
    # __slots__ hell
    slots = dict.pop("__slots__", [])
    if slots and "__slots__" not in locals:
        locals["__slots__"] = ["__dict__"]
    for name in slots:
        if name.startswith("__") and not name.endswith("__"):
            name = "_%s%s" % (cls.__name__, name)
        dict.pop(name)
        locals["__slots__"].append(name)
    
    # mix the namesapces
    locals.update(dict)
    
print plugImport("essai")
