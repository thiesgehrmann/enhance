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
             echo -en '#!/bin/sh\njava_args="$1";\nshift;\nif [ "$java_args" == "-" ]; then\n  java_args="";\nfi\njava $java_args -jar %(prefix)s/opt/pilon-9999.jar "$@"' > %(prefix)s/bin/pilon
             chmod +x %(prefix)s/bin/pilon
             echo 'BE AWARE OF SPECIAL INPUT FORMAT. FIRST PARAMETER TO pilon ARE JVM ARGUMENTS. SEE %(prefix)s/bin/pilon'"""
      for cmd in c.split('\n'):
        runCommand(self.fillVars(c))


