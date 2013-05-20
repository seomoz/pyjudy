
ctypedef unsigned char uint8_t

cdef extern from "stdlib.h":
    ctypedef void const_void "const void"
    void strcpy(uint8_t*, uint8_t*)

# this is how we do #define in cython
DEF MAXLINELEN = 100000

cdef extern from "Judy.h":
    ctypedef void *   Pvoid_t
    ctypedef unsigned long    Word_t

    void JSLI( Word_t* PValue, Pvoid_t PJSLArray, uint8_t* Index)
    void JSLG( Word_t* PValue, Pvoid_t PJSLArray, uint8_t* Index)
    void JSLD( int Rc_int,     Pvoid_t PJSLArray, uint8_t* Index)
    void JSLFA(Word_t Rc_word, Pvoid_t PJSLArray)
    void JSLF( Word_t* PValue,  Pvoid_t PJSLArray, uint8_t* Index)
    void JSLN( Word_t* PValue,  Pvoid_t PJSLArray, uint8_t* Index)


cdef class JudySL(object):
    cdef Pvoid_t _ptr

    def __cinit__(self):
        self._ptr = NULL

    def __dealloc__(self):
        cdef Word_t v
        JSLFA(v, self._ptr)

    def __setitem__(self, uint8_t* key, Word_t value):
        # JSLI returns a pointer to the value.
        # we need to use it to set the desired value
        # Cython does not implement *v, instead need to use v[0]
        cdef Word_t* v
        JSLI(v, self._ptr, key)
        v[0] = value

    def __getitem__(self, uint8_t* key):
        cdef Word_t* v
        JSLG(v, self._ptr, key)
        if v == NULL:
            # not found
            raise KeyError
        else:
            return v[0]

    def __contains__(self, uint8_t* key):
        cdef Word_t* v
        JSLG(v, self._ptr, key)
        return v != NULL

    def __delitem__(self, uint8_t* key):
        cdef int Rc_int
        JSLD(Rc_int, self._ptr, key)
        if Rc_int == 0:
            # not in array
            raise KeyError

    def iteritems(self):
        # we need this construction to initialize key to null
        cdef uint8_t key[MAXLINELEN]
        strcpy(key, "")

        cdef Word_t* v

        # two parts
        # (1) start the iteration with JSLF to get the first key, value
        # (2) use JSLN to get the next value
        JSLF(v, self._ptr, key)

        while v != NULL:
            yield key, v[0]

            # (2)
            JSLN(v, self._ptr, key)

    def iterkeys(self):
        for k, v in self.iteritems():
            yield k

    def itervalues(self):
        for k, v in self.iteritems():
            yield v

