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
         mkdir -p %(prefix)s/opt/busco
         cp BUSCO.py BUSCO_plot.py %(prefix)s/opt/busco
         echo -en "#!/bin/sh\\nexport PYTHONPATH=$PYTHONPATH\\n%(prefix)s/opt/busco/BUSCO.py \"\$@\"" > %(prefix)s/bin/BUSCO
         chmod +x %(prefix)s/bin/BUSCO
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
