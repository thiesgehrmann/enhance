from package import *

class libxml(MakePackage):
    fetch="ftp://xmlsoft.org/libxml2/libxml2-2.9.4.tar.gz"


    def config(self):
      c="""
        ./configure --prefix=%(prefix)s
        for x in Makefile python/Makefile; do sed -i.bak -e 's:^PYTHON =.*$:PYTHON = %(prefix)s/bin/python:' -e 's:^PYTHON_INCLUDES = .*$:PYTHON_INCLUDES = %(prefix)s/include/python2.7/:' -e 's:^PYTHON_LIBS = .*$:PYTHONLIBS = -L%(prefix)s/lib64/ -lpython2.7 -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic:' -e 's:^PYTHON_SITE_PACKAGES =.*$:PYTHON_SITE_PACKAGES = %(prefix)s/lib64/python2.7/site-packages/:' $x; done
        sed -i.bak -e 's/$(LIBTOOL) $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=install//' python/Makefile
        make clean
        """
      for cmd in c.split('\n'):
        print cmd
        runCommand(self.fillVars(cmd))
        print self.fillVars(cmd)

