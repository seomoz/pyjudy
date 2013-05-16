
Python bindings to libJudy
==========================

[libJudy](TODO LINK HERE) is an efficient trie implementation in C.
Unfortunately of the existing three Python bindings, two do not work
on 64 bit systems, and the third only implements integer arrays and sets.

Our use case needs the JudySL implementation (string -> long), so
we provide Cython bindings for it.  If the need arises we will add
bindings to the other array types in the future based on the template
for JudySL.  If you implement other bindings please let us know
and we will add them to this repository.

This code is tested in Python 2.6/7 with Cython >0.17.

Getting Started
===============

Install libJudy and Cython, then compile the bindings:

    python setup.py install

After installation, make sure the unit tests pass:

    python test/test_judysl.py

The class `JudySL` implements a dictionary like interface.

    from pyjudy import JudySL

    j = JudySL()

    # set an item
    j['key'] = 5
    j['another key'] = 22
    j['third'] = 3

    # get an item 
    val = j['key']

    # delete one
    del j['another key']

    # iteration
    for k, v in j.iteritems():
        # do something with k, v


The current implementation includes `__getitem__`, `__setitem__`,
`__delitem__` and `iteritems`, `iterkeys`, `itervalues`.


Unicode support
===============

Uncode is not supported directly; instead it is necessary to convert
to byte string.

    j = JudySL()

    # this works
    s = u"A unicode string \xae"
    j[s.encode('utf-8')] = 5

    # this does not, if s contains non-ascii characters
    # raises UnicodeEncodeError
    j[s] = 5


