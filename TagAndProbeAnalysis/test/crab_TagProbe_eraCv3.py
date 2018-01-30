# from https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial                                                         
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TagAndProbeeraCv3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TagProbe_eraCv3.py'

config.Data.inputDataset = '/SingleMuon/Run2017C-PromptReco-v3/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1000
config.Data.lumiMask = 'eraC.txt'
config.Data.runRange = '299368-302029'
#config.Data.totalUnits = 1                                                                                                         
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag =  'TagAndProbe_eraCv3'

config.Site.storageSite = 'T2_CH_CERN'

