from package import *

class orthofinder(MakePackage):

  dependencies = [ 'fastme', "dlcpar" ]

  fetch = "https://github.com/davidemms/OrthoFinder/releases/download/1.1.4/OrthoFinder-1.1.4_source.tar.gz"

  workdir="OrthoFinder-1.1.4_source"
  config=""
  build=""
  def install(self):
    c="""
      mv orthofinder %(prefix)s/opt/orthofinder
      ln -s %(prefix)s/opt/orthofinder/orthofinder.py %(prefix)s/bin
    """

    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))


  
