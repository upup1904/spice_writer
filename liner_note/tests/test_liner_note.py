from django.test import SimpleTestCase
from liner_note import add_note


class WrittenToTuplesTestCase(SimpleTestCase):
    def test_simple(self):
        linespecs, msgs = add_note.process_spec("4.8")
        self.assertEqual(linespecs, set([(4, 8)]))
        self.assertFalse(msgs)

    def test_multi(self):
        linespecs, msgs = add_note.process_spec("4.8 6.1001, 3.200")
        self.assertEqual(linespecs, set([(3, 200), (6, 1001), (4, 8)]))
        self.assertFalse(msgs)

    def test_range(self):
        linespecs,msgs = add_note.process_spec("6.8-12")
        self.assertEqual(linespecs, set([(6,8), (6,9), (6,10), (6,11), (6,12)]))
        self.assertFalse(msgs)

    def test_invalid_range_ignored(self):
        linespecs,msgs = add_note.process_spec("6.8-6")
        self.assertEqual(set( [(6, 8)] ), linespecs)
        self.assertEqual(msgs, ["range 6.8-6 is invalid, using first line only"])
    def test_multi_range(self):
        linespecs,msgs = add_note.process_spec("4.5-6 10.9-11 3.3")
        self.assertEqual(set( [(4, 5), (4,6), (10,9), (10,10), (10,11), (3,3)] ), linespecs)
        
    
        
