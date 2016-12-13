from package import *

class busco(MakePackage):

  dependencies = ["git", "augustus", "hmmer", "ncbi_blast"]

  def fetch(self):
    runCommand("git clone https://gitlab.com/ezlab/busco.git")

  unpack = ""
  workdir = "busco"
  config=""
  build = ""

  def install(self):
    c="""pwd
         cp BUSCO.py BUSCO_plot.py %(prefix)s/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
