# from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial                                                         
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TagAndProbeeraBv2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TagProbe_eraBv2.py'

config.Data.inputDataset = '/SingleMuon/Run2017B-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'eraB.txt'
config.Data.runRange = '297050-299329'
#config.Data.totalUnits = 1                                                                                                         
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'TagAndProbe_eraBv2'

config.Site.storageSite = 'T2_CH_CERN'

