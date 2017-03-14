from package import *

class dorthofinder(MakePackage):

  dependencies = [ 'fastme', "dlcpar", "git" ]

  def fetch(self):
    runCommand(self.fillVars("rm -rf %(prefix)s/bin/dorthofinder.py"))
    runCommand(self.fillVars("rm -rf %(prefix)s/src/OrthoFinder"))
    runCommand(self.fillVars("rm -rf %(prefix)s/opt/dorthofinder"))
    runCommand("git clone git@github.com:thiesgehrmann/OrthoFinder.git")

  workdir="OrthoFinder"
  unpack = ""
  config = ""
  build = ""

  def install(self):
    c="""
      rm -rf %(prefix)s/opt/dorthofinder
      rm -rf %(prefix)s/bin/dorthofinder.py

      mv orthofinder %(prefix)s/opt/dorthofinder
      ln -s %(prefix)s/opt/dorthofinder/orthofinder.py %(prefix)s/bin/dorthofinder.py
    """

    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))

