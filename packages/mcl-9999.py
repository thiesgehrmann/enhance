from package import *

class mcl(MakePackage):

  fetch = "http://micans.org/mcl/src/mcl-latest.tar.gz"

  def unpack(self, tar, wd):
    c="""pwd
      mkdir -p mcl_latest
      tar -xvf %(tar)s -C mcl_latest --strip-components 1"""
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd, tar=tar))

  workdir = "mcl_latest"

  config = "cd '" + workdir + "' && pwd && ./configure --prefix=%(prefix)s" 

  build="cd '" + workdir + "' && pwd && make"

  install="cd '" + workdir + "' && pwd && make install"


