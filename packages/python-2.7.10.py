from package import *

class python(MakePackage):
    dependencies=["bzip2","ncurses", "sqlite","readline", "zlib", "openssl"]
    fetch="https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz"

    config="./configure --enable-shared --prefix=%(prefix)s"

    install="""
            make install
            python setup.py install --prefix=%(prefix)s
            mv %(prefix)s/bin/python2.7 %(prefix)s/bin/python2.7exec
            echo -en "#!/bin/sh\\nexport PYTHONPATH=`eval $(cat $ENHANCEHOME/root/paths | grep PYTHONPATH | cut -d\( -f2 | cut -d\) -f1)`\\n%(prefix)s/bin/python2.7exec \"\$@\"" > %(prefix)s/bin/python2.7
            chmod +x %(prefix)s/bin/python2.7
            ln -f -s %(prefix)s/bin/easy_install-2.7 %(prefix)s/bin/easy_install2
            """

