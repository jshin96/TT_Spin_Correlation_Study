import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('root://eosuser.cern.ch//eos/user/s/shin/Gridpacks/Powheg_vs_Madgraph_spinCorrelation/tt_elmu_Powheg_spinlessmadspin_NLO_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_local.sh')
)

#Link to datacards:
#https://github.com/jfernan2/genproductions/blob/54a8155135fb7f0d9cef82dbbbbdcdbb59ea55f0/bin/Powheg/production/2017/13TeV/TT_hvq/TT_hdamp_NNPDF31_NNLO_ljets.input


import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *
generator = cms.EDFilter("Pythia8HadronizerFilter",
maxEventsToPrint = cms.untracked.int32(1),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.0),
pythiaHepMCVerbosity = cms.untracked.bool(False),
comEnergy = cms.double(13000.),
PythiaParameters = cms.PSet(
pythia8CommonSettingsBlock,
pythia8CP5SettingsBlock,
pythia8PowhegEmissionVetoSettingsBlock,
processParameters = cms.vstring(
        'POWHEG:nFinal = 2', ## Number of final state particles
        ## (BEFORE THE DECAYS) in the LHE
        ## other than emitted extra parton
        'TimeShower:mMaxGamma = 1.0',#cutting off lepton-pair production
        ##in the electromagnetic shower
        ##to not overlap with ttZ/gamma* samples
        '6:m0 = 172.5',    # top mass'
),
parameterSets = cms.vstring('pythia8CommonSettings',
'pythia8CP5Settings',
'pythia8PowhegEmissionVetoSettings',
'processParameters'
)
)
)
ProductionFilterSequence = cms.Sequence(generator)
