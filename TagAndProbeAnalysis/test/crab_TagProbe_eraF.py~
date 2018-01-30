from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TagAndProbeeraE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TagProbe_eraE.py'

config.Data.inputDataset = '/SingleMuon/Run2017E-PromptReco-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'eraE.txt'
config.Data.runRange = '303825-304797'
#config.Data.totalUnits = 1                                                                                                             
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'TagAndProbe_eraE'

config.Site.storageSite = 'T2_CH_CERN'
