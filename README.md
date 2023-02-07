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
$ cp ../../NANOGEN_Production_part/Configuration .
$ cp ../../NANOGEN_Production_part/run_generic_tarball_local.sh GeneratorInterface/LHEInterface
$ cp ../../NANOGEN_Production_part/runCmsDriverNanoGen.sh .
$ sed -i "s/local/xroots/g" Configuration/TT_Spin_Corr/python/<cff_file_name_in_Configuration>
$ ./runCmsFriverNanoGen.sh <cff_file_name_in_Configuration> <output_root_file_name>
$ sed -i "s/xrootd/local/g" Configuration/TT_Spin_Corr/python/<cff_file_name_in_Configuration>
$ cd configs
$ cmsRun <cfg_file_in_configs_directory>
```
 * This will give NANOGEN root files, then move onto the NANOAOD-Tools Part
## NANOAOD-Tools Part
 * exampleModule.py is the file that determines the analysis.
 * keep_and_drop_input.txt and keep_and_drop_output.txt determines the branch that goes into the analyzer and what branch remains in the output file.

```
$ cd ..
$ git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
$ cp ../../NANOAODTool_part/exampleModule.py PhysicsTools/NanoAODTools/python/postprocessing/examples
$ cp ../../NANOAODTool_part/keep_and_drop* PhysicsTools/NanoAODTools/scripts
$ scram b 
$ python scripts/nano_postproc.py outDir <absolute path of NANOGEN file> -I PhysicsTools.NanoAODTools.postprocessing.examples.exampleModule exampleModuleConstr -s _exaModu_keepdrop --bi scripts/keep_and_drop_input.txt --bo scripts/keep_and_drop_output.txt
```
* In outDir directory, you should have output root file that you can have a look or run plotting code. 

