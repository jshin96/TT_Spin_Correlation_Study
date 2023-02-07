from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import math

class exampleProducer(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
            self.out.branch("toplep_eta_%s" %mass, "F")
            self.out.branch("toplep_phi_%s" %mass, "F")
            self.out.branch("antitoplep_eta_%s" %mass, "F")
            self.out.branch("antitoplep_phi_%s" %mass, "F")
            self.out.branch("deta_%s" %mass, "F")
            self.out.branch("dphi_%s" %mass, "F")
            self.out.branch("top_pair_mass_%s" %mass, "F")
            self.out.branch("top_mass_%s" %mass, "F")
            self.out.branch("antitop_mass_%s" %mass, "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        nparts = getattr(event, "nLHEPart")
        n_lep = 0
        n_antilep = 0
        lead_lep_pt = 0.0
        lead_antilep_pt = 0.0
        leps = []
        antileps = []
        dphi=0.0
        deta=0.0
        antilep_eta = 0.0
        antilep_phi = 0.0
        lep_eta = 0.0
        lep_phi = 0.0
        top = ROOT.TLorentzVector()
        antitop = ROOT.TLorentzVector()
        ttpair = ROOT.TLorentzVector()
        for i in range(nparts):
#                if (getattr(event, "GenPart_statusFlags")[i] == 8):
            if (True):

                    lep_eta = getattr(event,"LHEPart_eta")[i]
                    lead_lep_pt = getattr(event,"LHEPart_pt")[i]
                    n_lep = 1
                    lep_phi = getattr(event,"LHEPart_phi")[i]

                if (getattr(event,"LHEPart_pdgId")[i] == 11 or getattr(event,"LHEPart_pdgId")[i] == 13 and getattr(event,"LHEPart_pt")[i] > lead_antilep_pt):
                    antilep_eta = getattr(event,"LHEPart_eta")[i]
                    lead_antilep_pt = getattr(event,"LHEPart_pt")[i]
                    antilep_phi = getattr(event,"LHEPart_phi")[i]
                    n_antilep = 1
            else: continue

        masses = ["450", "550", "800", "inf"]
        mparts = getattr(event, "nGenPart")
        for i in range(mparts):
            if (getattr(event,"GenPart_pdgId")[i] == 6 and getattr(event,"GenPart_genPartIdxMother")[i] < 5):
                top.SetPtEtaPhiM(getattr(event,"GenPart_pt")[i],getattr(event,"GenPart_eta")[i],getattr(event,"GenPart_phi")[i],getattr(event,"GenPart_mass")[i])
            if (getattr(event,"GenPart_pdgId")[i] == -6 and getattr(event,"GenPart_genPartIdxMother")[i] < 5):
                antitop.SetPtEtaPhiM(getattr(event,"GenPart_pt")[i],getattr(event,"GenPart_eta")[i],getattr(event,"GenPart_phi")[i],getattr(event,"GenPart_mass")[i])

        for k, mass in enumerate(masses):
            if k == 0:
                lower_bound = 0.0
            else:
                lower_bound = float(masses[k-1])
            upper_bound = float(masses[k])


            ttpair = top + antitop
            deta = lep_eta-antilep_eta
            dphi = lep_phi-antilep_phi
            PI = ROOT.TMath.Pi()
            if dphi > PI:
                dphi -= 2*PI
            if dphi < -PI:
                dphi += 2*PI
            if (n_lep != 1 or n_antilep != 1): return False
            deta = abs(deta)
            dphi = abs(dphi)
            if (ttpair.M() >= lower_bound and ttpair.M() < upper_bound):
                self.out.fillBranch("toplep_eta_%s" %mass,lep_eta)  # fill histogram
                self.out.fillBranch("toplep_phi_%s" %mass,lep_phi)  # fill histogram
                self.out.fillBranch("antitoplep_eta_%s" %mass,antilep_eta)  # fill histogram
                self.out.fillBranch("antitoplep_phi_%s" %mass,antilep_phi)  # fill histogram
                self.out.fillBranch("deta_%s" %mass,deta)  # fill histogram
                self.out.fillBranch("dphi_%s" %mass,dphi)  # fill histogram
                self.out.fillBranch("top_pair_mass_%s" %mass,ttpair.M())  # fill histogram
                self.out.fillBranch("top_mass_%s" %mass,antitop.M())  # fill histogram
                self.out.fillBranch("antitop_mass_%s" %mass,top.M())  # fill histogram
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

exampleModuleConstr = lambda: exampleProducer()
