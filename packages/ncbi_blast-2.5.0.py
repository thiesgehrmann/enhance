from package import *;

class ncbi_blast(MakePackage):
    depenencies=['Archive']
    fetch='ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.5.0/ncbi-blast-2.5.0+-src.tar.gz'
    workdir="ncbi-blast-2.5.0+-src/c++/"
    config="./configure --with-mt --prefix=%(prefix)s --without-debug"

    def install(self):
      c = """sed -i.bak -e 's:$(INSTALL) -m 644 $(incdir)/[*] $(pincludedir):$(INSTALL) -m 644 $(incdir)/common/* $(incdir)/*.h $(pincludedir):' Makefile
             make install"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))
