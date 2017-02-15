from package import *

class gffread(MakePackage):

  def fetch(self):
    c = """  git clone https://github.com/gpertea/gclib
             git clone https://github.com/gpertea/gffread
             cd gffread
             make"""

    for cmd in c.split("\n"):
      runCommand(c)

  unpack = ""
  
  workdir = "gffread"

  config = ""
  build = "make"


  def install(self):
    runCommand(self.fillVars("cp gffread %(prefix)s/bin"))
  
