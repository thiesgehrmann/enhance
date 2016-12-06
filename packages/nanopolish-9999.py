from package import *

class nanopolish(Package):
    dependencies = ["git","hdf5"]

    def fetch(self):
      runCommand("git clone --recursive https://github.com/jts/nanopolish.git")

    unpack=""
    workdir="nanopolish"


    def install(self):
      c = """sed -i.bak 's/^HDF5=install$/HDF5=noinstall/' Makefile
             make
             cp nanopolish %(prefix)s/bin """
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))

