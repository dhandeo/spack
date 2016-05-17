import os
from spack import *


class PyEsmf(Package):
    """
    The Earth System Modeling Framework (ESMF) is a suite of software tools
    for developing high-performance, multi-component Earth science modeling
    applications. Such applications may include a few or dozens of components
    representing atmospheric, oceanic, terrestrial, or other physical domains,
    and their constituent processes (dynamical, chemical, biological, etc.).
    Often these components are developed by different groups independently, and
    must be ``coupled'' together using software that transfers and transforms
    data among the components in order to form functional simulations.
    """

    homepage = "https://www.earthsystemcog.org/projects/esmf://www.earthsystemcog.org/projects/esmf/"

    #url      = "http://www.earthsystemmodeling.org/esmf_releases/non_public/ESMF_7_0_0/esmf_7_0_0_src.tar.gz"
    url      = "http://uvcdat.llnl.gov/cdat/resources/esmp.ESMF_6_3_0rp1_ESMP_01.tar.bz2"

    version('6.3.0', 'a9be4fb51da1bc1fab027137297c5030', url="http://uvcdat.llnl.gov/cdat/resources/esmp.ESMF_6_3_0rp1_ESMP_01.tar.bz2")

    # TODO: add optional packages

    depends_on("esmf")
    depends_on("python")
    depends_on("py-numpy")
    extends("python")

    def install(self, spec, prefix):
        # TODO: add optional packages
        os.environ["ESMFMKFILE"] = os.path.join(spec["esmf"], "lib", "esmf.mk")
        os.environ["ESMF_INSTALL_PREFIX"] = prefix

        with working_dir('ESMP'):
            make()
            make("install")
