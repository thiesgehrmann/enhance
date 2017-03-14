from package import *;

class usearch(MakePackage):

  def fetch(self):
    pass

  unpack=""
  config=""
  build=""
  def install(self):
    runCommand(self.fillVars("wget http://drive5.com/cgi-bin/upload3.py?license=2017031308012919925 -O %(prefix)s/bin/usearch"))
    runCommand(self.fillVars("chmod +x %(prefix)s/bin/usearch"))
