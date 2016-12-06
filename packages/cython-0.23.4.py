from package import *

class cython(PythonPackage):
    dependencies = ["python"]
    fetch = "http://cython.org/release/Cython-%(version)s.tar.gz"
