from package import *

class miniasm(Package):
    dependencies = ["git","minimap"]

    def fetch(self):
      runCommand("git clone https://github.com/lh3/miniasm.git")

    unpack=""
    workdir="miniasm"


    def install(self):
      c = """make
             cp miniasm minidot %(prefix)s/bin"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))

