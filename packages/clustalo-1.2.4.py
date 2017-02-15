from package import *

class clustalo(MakePackage):

  dependencies = ["argtable"]

  fetch="http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz"
  workdir="clustal-omega-1.2.4"
