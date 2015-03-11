import FWCore.ParameterSet.Config as cms

# -------------------------------------
# Options
# -------------------------------------
from Analyzer.Ntuplizer.Options import *

options = getAnalysisOptions()

options.maxEvents = -1
options.isMC = 1
options.ispythia6 = 1

options.parseArguments()

print "cmsRun with options: "
print "===================="
print options

# --------------------------------------
#  Options : Consequences
# --------------------------------------
if options.isMC == True :
    #GLOBALTAG = 'POSTLS162_V1::All'
    GLOBALTAG = 'PHYS14_25_V1::All'
else :
    GLOBALTAG = 'FT_R_70_V1::All'
    #to be checked...

print "Global Tag = ", GLOBALTAG

# -------------------------------------
process = cms.Process("Ntuplizer")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration/StandardSequences/MagneticField_38T_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')
#[16:55:02] Florian Beaudette: process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')

process.load("FWCore.MessageService.MessageLogger_cfi")


process.GlobalTag.globaltag = GLOBALTAG
#'POSTLS162_V1::All'
#START53_V15A::All'

process.load("Configuration.EventContent.EventContent_cff")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
#-1) )

# ----------------------------------------------------------------------
# Input File
# ----------------------------------------------------------------------
process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
    #'file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/TTJets_8TeV_53X.root'
    #'file:/data_CMS/cms/ochando/MC/CMSSW7XX/RelValZEE13GENSIMRECOPU50nsPOSTLS170V4v2/742B2DC4-C898-E311-B830-002590494D18.root'
    #'file:/data_CMS/cms/ochando/DATA/CMSSW7XX/981C8375-DED4-E311-86D0-0026189438BC.root'
    #'/store//mc/Spring14dr/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_POSTLS170_V5-v1/00000/F61AD943-37CE-E311-836D-003048D4DCD8.root'
    'file:/data_CMS/cms/ochando/1AD11194-BA6E-E411-A8A9-7845C4FC39E3.root'
    #'/store/mc/Spring14dr/TT_Tune4C_13TeV-pythia8-tauola/AODSIM/PU_S14_POSTLS170_V6-v1/00000/001C9565-FCD9-E311-96DE-002618FDA210.root'

                )
                            )

# ----------------------------------------------------------------------
# Output root file (monitoring histograms)
# ----------------------------------------------------------------------
process.TFileService=cms.Service('TFileService',
                                fileName=cms.string('electron_ntuple.root')
                                )


# ----------------------------------------------------------------------
# Electron ID
# ----------------------------------------------------------------------
process.load("EgammaAnalysis.ElectronTools.electronIdMVAProducer_CSA14_cfi")
process.load("RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cff")
#process.p = cms.Path(process.egmGsfElectronIDSequence + process.mvaNonTrigV025nsPHYS14)
#process.mvaTrigV050nsCSA14+process.mvaTrigV025nsCSA14+process.mvaNonTrigV050nsCSA14+process.mvaNonTrigV025nsCSA1+process.mvaNonTrigV025nsPHYS14 +process.exampleAnalyzer)

from FWCore.Modules.printContent_cfi import *
#process.dumpEv = FWCore.Modules.printContent_cfi.printContent.clone()
process.printDebug = cms.EDAnalyzer("EventContentAnalyzer")

# ----------------------------------------------------------------------
# Ntuplizer
# ----------------------------------------------------------------------
process.ntuplizer = cms.EDAnalyzer('Ntuplizer',
                                   EleTag      = cms.InputTag('gedGsfElectrons'),
                                   VerticesTag = cms.InputTag('offlinePrimaryVertices'),
                                   HLTTag          = cms.InputTag('TriggerResults','','HLT'),
                                   isMC = cms.bool(bool(options.isMC)),
                                   ispythia6 = cms.bool(bool(options.ispythia6)),
                                   MVAId  = cms.VInputTag("mvaNonTrigV025nsPHYS14", "mvaNonTrigV025nsPHYS14FIX")
#","","addMVAid"),
    #True)
                                   
                                   )

# ----------------------------------------------------------------------
# Path to execute
# ----------------------------------------------------------------------
process.p = cms.Path(
    process.egmGsfElectronIDSequence 
    + process.mvaNonTrigV025nsPHYS14 
    + process.mvaNonTrigV025nsPHYS14FIX
    #+ process.printDebug
    + process.ntuplizer
    )
