import FWCore.ParameterSet.Config as cms

process = cms.Process("TAGPROBE")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

#process.source = cms.Source("PoolSource", 
#                            fileNames = cms.untracked.vstring(
#                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm.root',
#                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm_1.root',
#                            )
#)

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())

#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))


process.muonexercise4tp = cms.EDAnalyzer("TagProbe",
                                         TagTriggerList = cms.vstring(
                                             "HLT_IsoMu30"#,"HLT_IsoMu24",
                                             #"HLT_IsoTkMu30"#"HLT_IsoTkMu24"
                                         ),
                                         TriggerList = cms.vstring(
                                             "HLT_IsoMu30"#,
                                             #"HLT_IsoTkMu30"
                                         )
)

process.thepath = cms.Path(process.muonexercise4tp)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("TagAndProbe_eraE.root"),
                                   closeFileFast = cms.untracked.bool(False)
)
