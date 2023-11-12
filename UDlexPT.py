
# class UDlexPT - the PortiLexicon-UD it reads dic files from the current directory
#               - it should contain WORDmaster.txt plus the 12 tags .tsv files
#
# member functions:
#    UDlexPT                    - the constructor
#    sget(self, word):          # get the entries for a word - returns a list with 3-tuples (empty if absent)
#    exists(self, word):        # returns True if the word exists
#    pget(self, word, tag):     # get the entries of a word for a specific tag - return similar to sget
#    pexists(self, word, tag):  # returns True if this word has at least one entry for tag
#    theTags(self, word):       # returns an array of all tags of a word - empty if absent of the lexicon

from os import path

class UDlexPT:
    def __init__(self):  # creates the lexicon
        self.tags = ["ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", \
            "NOUN", "NUM", "PRON", "SCONJ", "VERB"]
        self.master = {}
        self.words = 0
        self.entries = 0
        nEnt = [0]*len(self.tags)
        nNAE = [0]*len(self.tags)
        nEnD = [0]*len(self.tags)
        infile = open(path.dirname(__file__)+"/WORDmaster.txt")
        for line in infile:
            buf = line[:-1].split(",")
            tg = buf[1].split(" ")
            self.master.update({buf[0]:tg})
            self.words += 1
            ### compute totals
            if (len(tg) == 1):
                nNAE[self.tags.index(tg[0])] += 1
            for t in tg:
                nEnt[self.tags.index(t)] += 1
        infile.close()
        self.t = []
        i = 0
        for t in self.tags:
            self.t.append({})
            infile = open(path.dirname(__file__)+"/"+t+".tsv")
            for line in infile:
                buf = line[:-1].split("\t")
                entry = self.t[i].get(buf[0],"none")
                if (entry == "none"):
                    self.t[i].update({buf[0]:[[buf[1],buf[2]]]})
                else:
                    entry.append([buf[1],buf[2]])
                    self.t[i].update({buf[0]:entry})
                self.entries += 1
                nEnD[self.tags.index(t)] += 1
            infile.close()
            i += 1
        print("UDlexPT read with", self.words, "distinct words and", self.entries, "entries")
        print("{:5} & {:6} & {:6} & {:6} \\\\ \\hline".format("tag","total","amb","non-amb"))
        accW, accN, accE = 0, 0, 0
        for t in self.tags:
            print("{:5} & {:6} & {:6} & {:6} & {:6} \\\\ \\hline".format(t, \
                nEnt[self.tags.index(t)], \
                nEnt[self.tags.index(t)]-nNAE[self.tags.index(t)], \
                nNAE[self.tags.index(t)], \
                nEnD[self.tags.index(t)]))
            accW += nEnt[self.tags.index(t)]
            accN += nNAE[self.tags.index(t)]
            accE += nEnD[self.tags.index(t)]
        print("{:5} & {:6} & {:6} & {:6} & {:6} \\\\ \\hline".format("total", self.words, self.words-accN, accN, accE))
    def sget(self, word):   # get the entries for a word
        tags = self.master.get(word,"none")
        if (tags == "none"):
            return []
        else:
            ans = []
            for t in tags:
                a = self.t[self.tags.index(t)].get(word)
                #if (a == None):
                #    input("fix WORDmaster for: "+word)
                for n in a:
                    ans.append([n[0],t,n[1]])
            return ans
    def exists(self, word):   # returns True if the word exists
        tags = self.master.get(word,"none")
        if (tags == "none"):
            return False
        else:
            return True
    def pget(self, word, tag):   # get the entries of a word for a specific tag
        a = self.t[self.tags.index(tag)].get(word,"none")
        if (a == "none"):
            return []
        else:
            ans = []
            for n in a:
                ans.append([n[0],tag,n[1]])
            return ans
    def pexists(self, word, tag):    # returns True if this word has at least one entry for tag
        a = self.t[self.tags.index(tag)].get(word,"none")
        if (a == "none"):
            return False
        else:
            return True
    def theTags(self, word):   # returns an array of all tags of a word - empty if absent of the dictionary
        ts = self.master.get(word,"none")
        if (ts == "none"):
            return []
        else:
            return ts

