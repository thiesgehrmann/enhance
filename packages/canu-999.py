from package import *

class canu(MakePackage):

  def fetch(self):
    runCommand("pwd")
    runCommand("git clone https://github.com/marbl/canu.git")

  unpack=""
  workdir = "canu/src"

  config=""

  def build(self):
    runCommand("pwd")
    build="make -j 32";
    runCommand(build)

  def install(self):
    c="""pwd
         mkdir -p %(prefix)s/opt/canu
         cp -r %(srcpath)s/canu/Linux-amd64/* %(prefix)s/opt/canu
         ln -sf %(prefix)s/opt/canu/bin/canu %(prefix)s/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
