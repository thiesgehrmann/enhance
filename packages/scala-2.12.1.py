from package import *

class scala(MakePackage):

  #dependencies = [ "java" ]

  fetch="http://downloads.lightbend.com/scala/2.12.1/scala-2.12.1.tgz"

  workdir="scala-2.12.1"

  config=""
  build=""

  def install(self):
    c="""
      mkdir -p %(prefix)s/opt/scala
      cp -r ./* %(prefix)s/opt/scala
      ln -s %(prefix)s/opt/scala/bin/scala %(prefix)s/bin/scala
      ln -s %(prefix)s/opt/scala/bin/scalac %(prefix)s/bin/scalac
      ln -s %(prefix)s/opt/scala/bin/scalap %(prefix)s/bin/scalap
    """
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
