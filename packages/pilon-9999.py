from package import *

class pilon(Package):
    dependencies = ["git"]

    def fetch(self):
      runCommand("git clone https://github.com/broadinstitute/pilon.git")

    unpack=""
    workdir="pilon"


    def install(self):
      c = """./build.sh
             mkdir -p %(prefix)s/opt/pilon/
             find | grep "pilon.*one-jar.jar" | xargs -i cp {} %(prefix)s/opt/pilon-9999.jar
             echo -en '#!/bin/sh\njava -jar %(prefix)s/opt/pilon-9999.jar "$@"' > %(prefix)s/bin/pilon
             chmod +x %(prefix)s/bin/pilon"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))


