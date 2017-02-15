
from package import *

class canu(MakePackage):


  def fetch(self):
    runCommand("wget https://github.com/marbl/canu/releases/download/v1.4/canu-1.4.Linux-amd64.tar.xz")
    runCommand("tar -xvf canu-1.4.Linux-amd64.tar.xz")

  workdir="canu-1.4/Linux-amd64"

  config=""

  build=""

  def install(self):
    c="""pwd
         rm -rf %(prefix)s/opt/canu
         mkdir -p %(prefix)s/opt/canu
         cp -r %(srcpath)s/canu-1.4/Linux-amd64/* %(prefix)s/opt/canu
         ln -sf %(prefix)s/opt/canu/bin/canu %(prefix)s/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
