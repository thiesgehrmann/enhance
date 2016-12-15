from package import *

class graphmap(Package):
    dependencies = ["git"]

    def fetch(self):
      runCommand("git clone https://github.com/isovic/graphmap.git")

    unpack=""
    workdir="graphmap"


    def install(self):
      c = """make modules
             make
             cp bin/Linux-x64/graphmap %(prefix)s/bin """
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))
