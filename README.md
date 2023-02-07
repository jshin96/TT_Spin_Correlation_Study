# TT_Spin_Correlation_Study

## NANOGEN_Production_Part
  * these are the configuration codes to generate cmsRun cfg code.
  * Here I use run_generic_tarball_local.sh file which just uses local tarball that is in the directory of cfg. 
  * So when you run the first time, change this into run_generic_tarball_xrootd.sh, and then change to   run_generic_tarball_local.sh for future generations so you don't download tarball everytime. 
```
$ cmsrel CMSSW_12_4_8
$ cd CMSSW_12_4_8/src
$ cmsenv
$ git cms-addpkg GeneratorInterface/LHEInterface
$ cd -
$ mv Configuration CMSSW_12_4_8/src
$ mv run_generic_tarball_local.sh GeneratorInterface/LHEInterface
$ mv runCmsDriverNanoGen.sh CMSSW_12_4_8/src
$ sed -i "s/local/xroots/g" Configuration/TT_Spin_Corr/python/<cff_file_name_in_Configuration>
$ ./runCmsFriverNanoGen.sh <cff_file_name_in_Configuration> <output_root_file_name>
$ sed -i "s/xrootd/local/g" Configuration/TT_Spin_Corr/python/<cff_file_name_in_Configuration>
$ cd configs
$ cmsRun <cfg_file_in_configs_directory>
```
 * This will give NANOGEN root files, then move onto the NANOAOD-Tools Part
## NANOAOD-Tools Part

```
$ cd ..
$ git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
$ cd PhysicsTools/NanoAODTools
$ scram b 
$ 
