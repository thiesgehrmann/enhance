from package import *

class pandas(PythonPackage):
  dependencies = [ "python", "numpy", "scipy", "pip" ]

  def fetch(self):
    pass

  unpack = ""
  workdir = ""
  build = ""
  install = "pip install pandas"
