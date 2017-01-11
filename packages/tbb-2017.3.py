from package import *

class tbb(MakePackage):
  fetch = "https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/tbb2017_20161128oss_src.tgz"
  workdir = "tbb2017_20161128oss"

  config = ""
  def install(self):
    c="""pwd
         find | grep -e 'libtbb.*so' | grep release | xargs -i cp {} %(prefix)s/lib64"""
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
      
