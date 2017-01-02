from package import *;

class spades(MakePackage):

  fetch="http://cab.spbu.ru/files/release3.9.1/SPAdes-3.9.1.tar.gz"
  workdir="SPAdes-3.9.1"
  config=""
  build = ""
  install = "PREFIX=%(prefix)s ./spades_compile.sh"
