from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.requestName = 'production-DYJetsToLL_M-50-madgraphMLM-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1_AODSIM-v3'
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.psetName = 'ntuplizer_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ntuple.root', 'ntuple.log', 'ntuple_stats.log']

config.section_('Data')

config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/AODSIM'

config.Data.inputDBS = 'global'
config.Data.outLFNDirBase = '/store/user/ppigard/eID/MC/Spring16/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-RunIISpring16DR80-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1_AODSIM/v3'

config.Data.totalUnits = -1
config.Data.unitsPerJob = 15
config.Data.splitting = 'FileBased'
config.Data.publication = False

config.section_('User')

config.section_('Site')
config.Site.blacklist = ['T2_US_Wisconsin']

config.Site.storageSite = 'T2_FR_GRIF_LLR'
