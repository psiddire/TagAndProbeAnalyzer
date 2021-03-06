import FWCore.ParameterSet.Config as cms

process = cms.Process("MCTRUTH")

#initialize MessageLogger and output report                                                                                            
#process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.MessageLogger.cerr.threshold = 'INFO'
#process.MessageLogger.cerr.INFO = cms.untracked.PSet(
#    limit = cms.untracked.int32(0)
#)

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring(
                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm.root',
                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm_1.root',
                            )
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.muonexercise4mc = cms.EDAnalyzer("McTruth",
                                         TriggerList = cms.vstring(
                                             "HLT_IsoMu24",
                                             "HLT_IsoTkMu24"
                                         )
)

process.thepath = cms.Path(process.muonexercise4mc)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("output.root"),
                                   closeFileFast = cms.untracked.bool(False)
)
