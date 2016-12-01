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
         mkdir -p %(prefix)/opt/canu
         cp -r %(srcpath)s/* %(prefix)/opt/canu
         ln -s %(prefix)s/opt/canu/Linux-amd64/bin/canu %(prefix)/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
