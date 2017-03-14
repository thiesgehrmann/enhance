from package import *

class fasttree(MakePackage):

  def fetch(self):
    c = """
      mkdir -p fasttree
      curl http://www.microbesonline.org/fasttree/FastTree.c > fasttree/FastTree.c
    """ 
    for cmd in c.split("\n"):
      runCommand(cmd)

  unpack = ""
  workdir = "fasttree"
  config = ""

  def build(self):
    runCommand("gcc -Wall -O3 -finline-functions -DOPENMP -fopenmp -funroll-loops -o FastTree -lm FastTree.c")

  def install(self):
    runCommand(self.fillVars("cp FastTree %(prefix)s/bin"))
