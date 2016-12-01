from package import *

class minimap(Package):
    dependencies = ["git"]

    def fetch(self):
      runCommand("git clone https://github.com/lh3/minimap.git")

    unpack=""
    workdir="minimap"


    def install(self):
      c = """make
             cp minimap %(prefix)s/bin"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))

