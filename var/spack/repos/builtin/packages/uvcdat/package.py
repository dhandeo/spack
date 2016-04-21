# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install uvcdat
#
# You can always get back here to change things with:
#
#     spack edit uvcdat
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Uvcdat(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://uvcdat.llnl.gov/index.html"
    url      = "https://github.com/UV-CDAT/uvcdat/archive/v2.4.1.tar.gz"

    version('2.5.0', '53d46658e34355b95caeb089cc4ed471')
    version('2.4.1', 'e54851295952891dabd0fe3840f59f3b')
    version('2.4.0', 'd4e51d6040a820920c75eebfa9ba256d')

    # FIXME: Add dependencies if this package requires them.
    depends_on("qt@4") # works with 4.8.6
    depends_on('zlib')
    depends_on('jpeg')
    depends_on('libpng')
    depends_on('libtiff')
    depends_on('libxml2')
    #depends_on('netcdf')
    #depends_on('netcdf-cxx')
    #depends_on('protobuf') # version mismatches?
    depends_on('sqlite') # external version not supported
    depends_on("jpeg") # works with 4.8.6
    depends_on("qt@4") # works with 4.8.6
    depends_on("qt@4") # works with 4.8.6
    depends_on("qt@4") # works with 4.8.6


    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        cmake('.', *std_cmake_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
