from spack import *

class Cmor(Package):
    """Climate Model Output Rewriter"""

    homepage = "https://pcmdi.github.io/cmor-site/index.htm"
    url      = "https://github.com/PCMDI/cmor/archive/CMOR-2.9.3.zip"

    version('2.9.3', '3d5017abe46f0b3aaaf9fa92ca0d0733')

    depends_on("libuuid")

    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix,
                  "--with-uuid=%s" % spec["libuuid"].prefix)
        make()
        make("install")
