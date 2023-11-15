# PortiLexicon-UD
PortiLexicon-UD a lexicon for Brazilian Portuguese according to Universal Dependencies

## Summary
This repository holds the data of the PortiLexicon-UD, as well as a Python 3 package, called UDlexPT, to access the lexicon data, plus a command line interface to the lexicon data.
PortiLexicon-UD is a lexicon for Portuguese that delivers the tagging information (PoS, lemma, and morphological features) for common words of Portuguese.

## Reference
To cite PortiLexicon-UD please refer to:
Lopes, L., Duran, M., Fernandes, P., and Pardo, T. (2022). PortiLexicon-UD: a Portuguese lexical resource according to Universal Dependencies model.
In Proceedings of the Thirteenth Language Resources and Evaluation Conference (LREC), pages 6635–6643, Marseille, France.
European Language Resources Association.

Available at: [http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.715.pdf](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.715.pdf)

# Contents
This repository contains the lexicon data, the Python 3 package to access the data, and a command line interface that uses the package in the simplest possible way.

## The Data
The data is composed by:
- `WORDmaster.txt`, one textual file with all lexicon entries (one per line) and the corresponding PoS tags that each entry has in the lexicon;
- 12 .tsv (tab separated values) files containing each the entries to each of the covered PoS tags, namely:
  - `ADJ.tsv` - the adjectives
  - `ADP.tsv` - the adpositions
  - `ADV.tsv` - the adverbs
  - `AUX.tsv` - the auxiliary verbs
  - `CCONJ.tsv` - the coordenative conjunctions
  - `DET.tsv` - the determiners
  - `INTJ.tsv` - the interjections
  - `NOUN.tsv` - the common nouns
  - `NUM.tsv` - the numbers (cardinals)
  - `PRON.tsv` - the pronouns
  - `SCONJ.tsv` - the subordinative conjunctions
  - `VERB.tsv` - the verbs

## Package UDlexPT
The Python 3 package UDlexPT is available in the file `UDlexPT.py` that read the data files and builds a data structure to access the lexicon.
Further information about the package usage and methods is available in the code remarks.

## Command Line Interface
The command line interface is written in Python 3 and it is available in file `lexUI.py`.
It provides a simple command line interface where the user types in a word and the information in the lexicon is fetched.

## Online Demo
A online demonstration of Portilexicon-UD is available at [https://portilexicon.icmc.usp.br](https://portilexicon.icmc.usp.br).

# Acknowledgements

This work was carried out at the Center for Artificial Intelligence of the University of São Paulo (C4AI - [http://c4ai.inova.usp.br/](http://c4ai.inova.usp.br/)), with support by the São Paulo Research Foundation (FAPESP grant #2019/07665-4) and by the IBM Corporation. The project was also supported by the Ministry of Science, Technology and Innovation, with resources of Law N. 8.248, of October 23, 1991, within the scope of PPI-SOFTEX, coordinated by Softex and published as Residence in TIC 13, DOU 01245.010222/2022-44.

