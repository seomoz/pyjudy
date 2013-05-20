
import unittest
from pyjudy import JudySL


class TestJudySL(unittest.TestCase):
    def test_judysl(self):
        j = JudySL()
        j['key here'] = 55
        j['another key'] = 123
        j['2q342)@(*)( #!'] = 0

        self.assertEqual(j['key here'], 55)
        self.assertEqual(j['another key'], 123)
        self.assertEqual(j['2q342)@(*)( #!'], 0)

        # set an existing key to another value
        j['key here'] = 987654321
        self.assertEqual(j['key here'], 987654321)

        # test some unicode
        # need to encode as byte string
        s = u"the registered trademark \xae"
        j[s.encode('utf-8')] = 88
        self.assertEqual(j[s.encode('utf-8')], 88)

    def test_contains(self):
        j = JudySL()
        j['a'] = 5
        self.assertTrue('a' in j)
        self.assertFalse('b' in j)

    def test_errors(self):
        j = JudySL()
        self.assertRaises(KeyError, j.__getitem__, 'missing key')
        self.assertRaises(OverflowError, j.__setitem__, 'a', -1)
        self.assertRaises(OverflowError, j.__setitem__, 'b', 2**70)
        self.assertRaises(TypeError, j.__getitem__, 5)

    def test_delitem(self):
        j = JudySL()

        j['a'] = 5
        del j['a']

        # now it isn't there, should raise keyerror
        self.assertRaises(KeyError, j.__delitem__, 'a')

    def test_iteritems(self):
        j = JudySL()

        # first test empty iteration
        keys = []
        values = []
        for k, v in j.iteritems():
            keys.append(k)
            values.append(k)
        self.assertEqual(keys, [])
        self.assertEqual(values, [])

        # now add some items and test
        j['a'] = 0
        j['bb'] = 5555
        d = {}
        for k, v in j.iteritems():
            d[k] = v
        self.assertEqual(d, {'a': 0, 'bb': 5555})

        # finally delete the items and iterate again
        del j['a']
        del j['bb']
        for k, v in j.iteritems():
            keys.append(k)
            values.append(k)
        self.assertEqual(keys, [])
        self.assertEqual(values, [])

    def test_iterkeys(self):
        j = JudySL()

        # empty iteration
        keys = []
        for k in j.iterkeys():
            keys.append(k)
        self.assertEqual(keys, [])

        # add items
        j['some words'] = 99
        j['cc'] = 3121
        for k in j.iterkeys():
            keys.append(k)
        keys.sort()
        self.assertEqual(keys, ['cc', 'some words'])

    def test_itervalues(self):
        j = JudySL()

        values = []
        for v in j.itervalues():
            values.append(v)
        self.assertEqual(values, [])

        j['asfsa'] = 12
        j['09182310'] = 3

        for v in j.itervalues():
            values.append(v)
        values.sort()
        self.assertEqual(values, [3, 12])

    def test_scope(self):
        # test that nothing strange happens when the judy array goes out
        # of scope

        def get_data():
            j = JudySL()
            j['z'] = 10
            j['y'] = 7
            j['x'] = 15
            ret = []
            for k, v in j.iteritems():
                ret.append((k, v))
            del j
            return ret

        data = get_data()
        data.sort()
        self.assertEqual(data, [('x', 15), ('y', 7), ('z', 10)])


if __name__ == "__main__":
    unittest.main()

