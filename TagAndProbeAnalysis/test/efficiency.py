import os
from sys import argv, stdout, stderr
import ROOT
import sys

ROOT.gROOT.SetStyle('Plain')
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

st = 'eraD'
filepath = 'plots/'+st+'/'
#file = 'crab_projects/crab_TagAndProbeMC/results/TagAndProbe_output.root'
file = 'crab_projects/crab_TagAndProbeeraD/results/TagAndProbe_eraD.root'

try:
    os.stat(filepath)
except:
    os.mkdir(filepath)

canvas = ROOT.TCanvas("canvas","canvas",800,800)

f = ROOT.TFile(file)

m1 = f.Get('muonexercise4tp/rec_tight_iso_hlt_pt')
m2 = f.Get('muonexercise4tp/rec_tight_iso_hlt_eta')
m3 = f.Get('muonexercise4tp/rec_tight_iso_hlt_nvtx')
m4 = f.Get('muonexercise4tp/rec_tight_iso_pt')
m5 = f.Get('muonexercise4tp/rec_tight_iso_eta')
m6 = f.Get('muonexercise4tp/rec_tight_iso_nvtx')
m7 = f.Get('muonexercise4tp/rec_tight_pt')
m8 = f.Get('muonexercise4tp/rec_tight_eta')
m9 = f.Get('muonexercise4tp/rec_tight_nvtx')
m10 = f.Get('muonexercise4tp/rec_pt')
m11 = f.Get('muonexercise4tp/rec_eta')
m12 = f.Get('muonexercise4tp/rec_nvtx')

m = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
n1 = m1.Clone('n1')
n2 = m2.Clone('n2')
n3 = m3.Clone('n3')
n4 = m4.Clone('n4')
n5 = m5.Clone('n5')
n6 = m6.Clone('n6')
n7 = m7.Clone('n7')
n8 = m8.Clone('n8')
n9 = m9.Clone('n9')
n = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

Titles = ["Trigger Efficiency vs Pt for "+st, "Trigger Efficiency vs Eta for "+st, "Trigger Efficiency vs NVtx for "+st, "Isolation Efficiency vs Pt for "+st, "Isolation Efficiency vs Eta for "+st, "Isolation Efficiency vs NVtx for "+st, "ID Efficiency vs Pt for "+st, "ID Efficiency vs Eta for "+st, "ID Efficiency vs NVtx for "+st]
YTitle = ["Trigger Efficiency", "Isolation Efficiency", "ID Efficiency"]
XTitle = ["Pt (GeV)", "Eta", "No. of Vertex"]
FileName = ["TriggerEfficiencyvsPt.png", "TriggerEfficiencyvsEta.png", "TriggerEfficiencyvsNVtx.png", "IsolationEfficiencyvsPt.png", "IsolationEfficiencyvsEta.png", "IsolationEfficiencyvsNVtx.png", "IDEfficiencyvsPt.png", "IDEfficiencyvsEta.png", "IDEfficiencyvsNVtx.png"]

for i in range(9):
    canvas.cd() 
    n[i].Divide(m[i+3])
    n[i].Draw()#"hist p")
    n[i].SetTitle(Titles[i])    
    n[i].SetMinimum(0.0)
    n[i].SetMaximum(1.0)
    n[i].GetYaxis().SetTitle(YTitle[int(i/3)])
    n[i].GetYaxis().SetNdivisions(505)
    n[i].GetYaxis().SetTitleSize(18)
    n[i].GetYaxis().SetTitleFont(43)
    n[i].GetYaxis().SetTitleOffset(1.7)
    n[i].GetYaxis().SetLabelFont(43) 
    n[i].GetYaxis().SetLabelSize(15)
    n[i].GetXaxis().SetTitle(XTitle[int(i%3)])
    n[i].GetXaxis().SetTitleSize(20)
    n[i].GetXaxis().SetTitleFont(43)
    n[i].GetXaxis().SetTitleOffset(1.0)
    n[i].GetXaxis().SetLabelFont(43) 
    n[i].GetXaxis().SetLabelSize(15)
    canvas.SaveAs(filepath+FileName[i])
    canvas.Clear()

