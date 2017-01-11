from package import *

class xorg(MakePackage):
    dependencies = ['git','freetype','fontconfig','autoconf','automake','libtool','m4']

    packages = ['util/macros','font/util','xcb/proto','xcb/pthread-stubs',\
                'proto/bigreqsproto','proto/xextproto','proto/kbproto','proto/inputproto',\
                'proto/xf86bigfontproto','proto/xcmiscproto','proto/x11proto',\
                'proto/xextproto','proto/renderproto','proto/fixesproto',\
                'proto/xineramaproto','proto/randrproto','proto/fontsproto',\
                'lib/libXau','xcb/libxcb','lib/libxtrans',\
                'lib/libXdmcp','lib/libX11','lib/libICE','lib/libSM',\
                'lib/libXt','lib/libXext','lib/libXfixes','lib/libXrender','lib/libXi',\
                'lib/libXinerama','lib/libXrandr','lib/libXcursor','lib/libfontenc','lib/libXfont', 'app/mkfontscale','app/mkfontdir','app/bdftopcf',\
                'font/encodings','font/adobe-100dpi','font/adobe-75dpi','font/adobe-utopia-100dpi',\
                'font/adobe-utopia-75dpi','font/adobe-utopia-type1','font/arabic-misc','font/bh-100dpi',\
                'font/bh-75dpi','font/bh-lucidatypewriter-100dpi','font/bh-lucidatypewriter-75dpi','font/bh-ttf',\
                'font/bh-type1','font/bitstream-100dpi','font/bitstream-75dpi','font/bitstream-speedo',\
                'font/bitstream-type1','font/cronyx-cyrillic','font/cursor-misc','font/daewoo-misc',\
                'font/dec-misc','font/ibm-type1','font/isas-misc','font/jis-misc','font/micro-misc',\
                'font/misc-cyrillic','font/misc-ethiopic','font/misc-meltho','font/misc-misc','font/mutt-misc',\
                'font/schumacher-misc','font/screen-cyrillic','font/sony-misc','font/sun-misc',\
                'font/winitzki-cyrillic','font/xfree86-type1','font/alias']
    packages = ['app/bdftopcf']


    def fetch(self):
        runCommand("""
            mkdir xorg/
            cd xorg/
            git clone git://anongit.freedesktop.org/git/xorg/util/modular util/modular
            """)
    patch="""--- util/modular/build.sh       2017-01-11 14:28:45.711029584 +0100
+++ /home/thiesgehrmann/build.sh        2017-01-11 14:20:11.839005813 +0100
@@ -560,6 +560,11 @@
        return 1
     fi

+    # To remove the AC_GCC_BUILTIN thing that doesn't work...
+    if [ "$component" == "libXext" ]; then
+      sed -i.bak -e 's/AX_GCC_BUILTIN(\[__builtin_popcountl\])//' "$DIR/configure.ac"
+    fi
+
     return 0
 }
"""

    workdir = "xorg"

    def config(self):
        f = open('module_list','w')
        for package in self.packages:
            f.write(package + '\n')
        f.close()
        f = open('build.sh.patch', 'w')
        for line in self.patch.split('\n'): 
          f.write(line + '\n')
        f.close()

    modify_environ={'PREFIX':'%(prefix)s'}
    
    build = """
            patch util/modular/build.sh < build.sh.patch
            util/modular/build.sh --modfile module_list --clone %(prefix)s
            """
    
    install = ""
