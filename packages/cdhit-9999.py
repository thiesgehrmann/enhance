from package import *;

class cdhit(MakePackage):

  dependencies = ["git", "ncbi_blast"]

  def fetch(self):
    runCommand("git clone https://github.com/weizhongli/cdhit.git")

  workdir = "cdhit"
  unpack = ""
  config = ""
  def install(self):
    c = """
      mkdir -p %(prefix)s/opt/cdhit
      cp -r * %(prefix)s/opt/cdhit
      ln -sf %(prefix)s/opt/cdhit/cd-hit %(prefix)s/bin
      ln -sf %(prefix)s/opt/cdhit/cd-hit-est %(prefix)s/bin
      ln -sf %(prefix)s/opt/cdhit/cd-hit-2d %(prefix)s/bin
      ln -sf %(prefix)s/opt/cdhit/cd-hit-est-2d %(prefix)s/bin
      ln -sf %(prefix)s/opt/cdhit/cd-hit-div %(prefix)s/bin
      ln -sf %(prefix)s/opt/cdhit/cd-hit-454 %(prefix)s/bin"""

    for cmd in c.split('\n'):
      runCommand(self.fillVars(c))
