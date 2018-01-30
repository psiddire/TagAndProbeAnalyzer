from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TagAndProbeeraF'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TagProbe_eraF.py'

config.Data.inputDataset = '/SingleMuon/Run2017F-PromptReco-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'eraF.txt'
config.Data.runRange = '305044-306126'
#config.Data.totalUnits = 1                                                                                                             
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'TagAndProbe_eraF'

config.Site.storageSite = 'T2_CH_CERN'
