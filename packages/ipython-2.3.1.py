from package import *

class ipython(MakePackage):

    fetch = "https://pypi.python.org/packages/7b/90/9f795400c4780f6a3bbeaf8c2eaeb745319b922e3ae76492af244332af24/ipython-2.3.1.tar.gz"
    dependencies = ["readline","nose", "pexpect", "pyzmq", "pygments"]

    workdir="ipython-2.3.1"
    config=""
    build=""
    install="python setup.py install --prefix=%(prefix)s"


