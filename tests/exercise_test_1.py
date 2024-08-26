import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcs import filtrar_aprovados


class ExerciseTest1(unittest.TestCase):
    def testNormalSituation(self):
        self.assertEqual(filtrar_aprovados([
            {"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
	    	{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
		    {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}
        ]), [
            {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação", "media": 9.0},
		    {"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática", "media": 8.33}
        ])
    
    def testNoneIsApproved(self):
        self.assertEqual(filtrar_aprovados([
            {"nome": "Alice", "notas": [0, 0, 0], "curso": "Matemática"},
	    	{"nome": "Bob", "notas": [6.0, 5.5, 4.0], "curso": "Física"},
		    {"nome": "Charlie", "notas": [3.5, 2.0, 1.0], "curso": "Computação"}
        ]), [])

    def testNoArgumentsPassed(self):
        self.assertRaises(TypeError, filtrar_aprovados)
    
    def testNotAListPassed(self):
        with self.assertRaises(TypeError) as context1:
            filtrar_aprovados('olá')
        with self.assertRaises(TypeError) as context2:
            filtrar_aprovados(5)
        with self.assertRaises(TypeError) as context3:
            filtrar_aprovados(True)
        with self.assertRaises(TypeError) as context4:
            filtrar_aprovados({
                'a': 'a', 'b': 'b'
            })
        with self.assertRaises(TypeError) as context5:
            filtrar_aprovados((
                'a', 'b', 'c'
            ))
        with self.assertRaises(TypeError) as context6:
            filtrar_aprovados({
                'a', 'b', 'c'
            })

        self.assertTrue(isinstance(context1.exception, TypeError))
        self.assertTrue(isinstance(context2.exception, TypeError))
        self.assertTrue(isinstance(context3.exception, TypeError))
        self.assertTrue(isinstance(context4.exception, TypeError))
        self.assertTrue(isinstance(context5.exception, TypeError))
        self.assertTrue(isinstance(context6.exception, TypeError))

    
    def testAListOfNotDictionaries(self):
        self.assertRaises(TypeError, filtrar_aprovados([
            'a', 'b', (1, 2, 3, 4)
        ]))
        self.assertRaises(TypeError, filtrar_aprovados([
            {'a': 'b'}, 45, 3, 'a'
        ]))
    
    def testInsufficientArgumentsOnDicitionary(self):
        self.assertRaises(KeyError, filtrar_aprovados([
            {"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
	    	{"notas": [6.0, 5.5, 7.0], "curso": "Física"},
		    {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}
        ]))
        self.assertRaises(KeyError, filtrar_aprovados([
            {"nome": "Alice", "notas": [8.5, 9.0, 7.5]},
	    	{"notas": [6.0, 5.5, 7.0]},
		    {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}
        ])),
        self.assertRaises(KeyError, filtrar_aprovados([
            {"nome": "Alice", "curso": "Matemática"},
	    	{"notas": [6.0, 5.5, 7.0], "curso": "Física"},
		    {"nome": "Charlie", "curso": "Computação"}
        ]))
        self.assertRaises(KeyError, filtrar_aprovados([
            {"nome": "Alice"},
        ]))
