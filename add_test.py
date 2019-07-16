import unittest
import cffi
import importlib


def load(filename):
    # load source code
    source_file = open(filename + '.c')
    header_file = open(filename + '.h')
    source = source_file.read()
    includes = header_file.read()

    # pass source code to CFFI
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(filename + '_', source)
    ffibuilder.compile()

    # import and return resulting module
    module = importlib.import_module(filename + '_')

    source_file.close()
    header_file.close()

    return module.lib


class AddTest(unittest.TestCase):
    def test_addition(self):
        module = load('add')
        self.assertEqual(module.add(1, 2), 1 + 2)


if __name__ == '__main__':
    unittest.main()
