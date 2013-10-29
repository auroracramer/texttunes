import imp, sys

f, filename, desc = imp.find_module("collections", ["/home/j/jt/jtcramer/python26hack/"])

modle = imp.load_module("collections", f, filename, desc)

sys.modules['collections'] = modle
