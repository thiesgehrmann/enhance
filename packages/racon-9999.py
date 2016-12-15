from package import *

class racon(Package):
    dependencies = ["git", "zlib", "mummer"]

    def fetch(self):
      runCommand("git clone https://github.com/isovic/racon.git")

    unpack=""
    workdir="racon"

    def build(self):
      c = """make modules
             make tools
             make -j"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))

    def install(self):
      c = """cp ./bin/racon %(prefix)s/bin"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))
