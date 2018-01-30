import FWCore.ParameterSet.Config as cms

process = cms.Process("TAGPROBE")

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring(
#                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm.root',
#                                'root://cmseos.fnal.gov///store/user/cmsdas/2018/short_exercises/Muons/Samples/dymm_1.root',
                                 '/store/mc/RunIIFall17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/00000/005DC030-D3F4-E711-889A-02163E01A62D.root'      
                            )
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.muonexercise4tp = cms.EDAnalyzer("TagProbe",
                                         TagTriggerList = cms.vstring(
                                             "HLT_IsoMu24",
                                             "HLT_IsoTkMu24"
                                         ),
                                         TriggerList = cms.vstring(
                                             "HLT_IsoMu24",
                                             "HLT_IsoTkMu24"
                                         )
)

process.thepath = cms.Path(process.muonexercise4tp)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("TagProbe.root"),
                                   closeFileFast = cms.untracked.bool(False)
)
