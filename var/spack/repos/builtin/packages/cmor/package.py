from spack import *

class Cmor(Package):
    """Climate Model Output Rewriter"""

    homepage = "https://pcmdi.github.io/cmor-site"
    url      = "https://github.com/UV-CDAT/uvcdat/archive/v2.4.1.tar.gz"

    version('2.4.1', 'e54851295952891dabd0fe3840f59f3b')

    depends_on('ossp-uuid')
    depends_on('udunits2')

    def install(self, spec, prefix):
        with working_dir('Packages/cmor'):
            configure("--prefix=%s" % prefix)
            make()
            make("install")
