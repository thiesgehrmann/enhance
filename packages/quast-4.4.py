from package import *

class quast(MakePackage):

  #dependencies = ["perl", "matplotlib"]

  fetch="http://downloads.sourceforge.net/project/quast/quast-4.4.tar.gz"

  workdir="quast-4.4"
  config=""
  build = ""

  def install(self):
    c="""pwd
         mkdir -p %(prefix)s/opt/quast
         cp -r ./* %(prefix)s/opt/quast
         %(prefix)s/opt/quast/quast.py --test
         echo -en "#!/bin/sh\\nexport PYTHONPATH=$PYTHONPATH\\n%(prefix)s/opt/quast/quast.py \"\$@\"" > %(prefix)s/bin/quast
         chmod +x %(prefix)s/bin/quast
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))

