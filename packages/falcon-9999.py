from package import *

class falcon(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/FALCON.git") 

    workdir="FALCON"

    unpack=""
