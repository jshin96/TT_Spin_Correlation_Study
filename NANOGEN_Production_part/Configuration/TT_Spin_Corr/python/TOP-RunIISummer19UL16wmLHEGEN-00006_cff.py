import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('root://eosuser.cern.ch//eos/user/s/shin/Gridpacks/Powheg_vs_Madgraph_spinCorrelation/tt012j_5f_ckm_NLO_FXFX_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_local.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/blob/421fdb3d061157fb31029fee52d00676d36d893c/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/tt012j_5f_ckm_NLO_FXFX_NNLO3p1/tt012j_5f_ckm_NLO_FXFX_NNLO3p1_proc_card.dat


import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
generator = cms.EDFilter("Pythia8HadronizerFilter",
maxEventsToPrint = cms.untracked.int32(1),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.0),
pythiaHepMCVerbosity = cms.untracked.bool(False),
comEnergy = cms.double(13000.),
PythiaParameters = cms.PSet(
pythia8CommonSettingsBlock,
pythia8CP5SettingsBlock,
pythia8aMCatNLOSettingsBlock,
pythia8PSweightsSettingsBlock,
processParameters = cms.vstring(
  'JetMatching:setMad = off',
  'JetMatching:scheme = 1',
  'JetMatching:merge = on',
  'JetMatching:jetAlgorithm = 2',
  'JetMatching:etaJetMax = 999.',
  'JetMatching:coneRadius = 1.',
  'JetMatching:slowJetPower = 1',
  'JetMatching:qCut = 40.', #this is the actual merging scale
  'JetMatching:doFxFx = on',
  'JetMatching:qCutME = 20.',#this must match the ptj cut in the lhe generation step
  'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
  'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
  'TimeShower:mMaxGamma = 1.0',#cutting off lepton-pair production in the electromagnetic shower to not overlap with ttZ/gamma* samples
  'TimeShower:MEcorrections = on' # To avoid shifts in the peak position of the mass of correctly reconstructed top quarks
),
parameterSets = cms.vstring('pythia8CommonSettings',
'pythia8CP5Settings',
'pythia8aMCatNLOSettings',
'pythia8PSweightsSettings',
'processParameters'
)
)
)
ProductionFilterSequence = cms.Sequence(generator)
