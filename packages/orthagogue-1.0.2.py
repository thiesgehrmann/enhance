from package import *

class orthagogue(MakePackage):
  dependencies = ["cmph", "tbb" ]
  fetch = "https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/orthagogue/orthAgogue-1.0.2.deb"

  def unpack(self, a, b):
    runCommand("pwd")
    runCommand("ar x orthAgogue-1.0.2.deb")
    runCommand("tar -xvf data.tar.gz")

  workdir=""
  config=""
  build=""

  def install(self):
    c="""pwd
         cp usr/bin/orthAgogue %(prefix)s/bin"""
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
      

