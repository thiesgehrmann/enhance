from package import *

class louvaingeneric(MakePackage):
  # THE FLOAT VERSION OF LOUVAIN! THERE MAY BE LOSS OF PRECISENESS
  dependencies = [ "git" ]

  def fetch(self):
    runCommand("git clone git@github.com:thiesgehrmann/louvain.git")

  unpack=""

  workdir = "louvain"
  config = ""

  def buld(self):
    runCommand("pwd")
    runCommand("make")

  def install(self):
    c = """
      cp louvain %(prefix)s/bin/louvain
      cp convert %(prefix)s/bin/louvain-convert
      cp hierarchy %(prefix)s/bin/louvain-hierarchy"""
    for cmd in c.split("\n"):
      runCommand(self.fillVars(cmd))
