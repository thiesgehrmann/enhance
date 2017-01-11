from package import *

class diamond(MakePackage):

  dependencies = ["git"]

  def fetch(self):
    runCommand("git clone https://github.com/bbuchfink/diamond.git")

  unpack = ""
  workdir = "diamond"
  config=""
  build = ""

  def install(self):
    c="""pwd
         ./build_simple.sh
         mv diamond %(prefix)s/bin
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
