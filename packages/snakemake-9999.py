from package import *

class snakemake(EasyInstall3Package):
  def install(self):
    cmds = """easy_install3 -U %(name)s
              sed -i.bak -e 's!%(prefix)s/bin/python3.4exec!%(prefix)s/bin/python3.4!' %(prefix)s/bin/snakemake """
    for c in cmds.split("\n"):
      runCommand(self.fillVars(c))
