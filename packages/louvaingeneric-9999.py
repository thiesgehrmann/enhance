from package import *

class louvaingeneric(MakePackage):

  fetch = "https://downloads.sourceforge.net/project/louvain/GenericLouvain/louvain-generic.tar.gz"
  workdir = "gen-louvain"
  config = ""

  def install(self):
    c = """
      cp louvain %(prefix)s/bin
      cp convert %(prefix)s/bin/louvain-convert
      cp hierarchy %(prefix)s/bin/louvain-hierarchy"""
    for cmd in c.split("\n"):
      runCommand(self.fillVars(cmd))


