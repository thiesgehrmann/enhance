from package import *

class lapack(Package):
    fetch="http://www.netlib.org/lapack/lapack-%(version)s.tgz"

    config='sed -e "s:OPTS     =:OPTS = -fPIC:g" -e "s:NOOPT    =:NOOPT = -fPIC:g" make.inc.example > make.inc'

    workdir = "lapack-3.5.0"

    build="""
          ulimit -s 65000
          make blaslib
          make lapackelib
          make
          """

    install="""
            pwd
            cp liblapack.a %(prefix)s/lib/
            cp libtmglib.a %(prefix)s/lib/
            cp liblapacke.a %(prefix)s/lib/
            """

