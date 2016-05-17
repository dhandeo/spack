import os
from spack import *


class Esmf(Package):
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

    # Direct versions require acceptance of a license
    #url      = "http://www.earthsystemmodeling.org/esmf_releases/non_public/ESMF_7_0_0/esmf_7_0_0_src.tar.gz"
    url      = "http://uvcdat.llnl.gov/cdat/resources/esmp.ESMF_6_3_0rp1_ESMP_01.tar.bz2"

    version('6.3.0', 'a9be4fb51da1bc1fab027137297c5030', url="http://uvcdat.llnl.gov/cdat/resources/esmp.ESMF_6_3_0rp1_ESMP_01.tar.bz2")

    # TODO: add optional packages
    extends("python")
    depends_on("py-numpy")

    def install(self, spec, prefix):
        # TODO: add optional packages
        os.environ["ESMF_DIR"] = os.path.join(self.stage.source_path, "esmf")
        os.environ["ESMF_INSTALL_PREFIX"] = prefix

        with working_dir('esmf'):
            make()
            make("install")