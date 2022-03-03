# Homework 2

**Due:** end of day, Friday, Mar 18th.

**How to submit?**
* Share your Google colab workbooks with sam77@psu.edu (make sure you are sharing access with me and not just sending me a link)
* If the questions ask for written descriptions or the conclusions you draw from the analyses, write them in text blocks within your colab notebook(s).


## Question 1 (2 points)
Beginning with the simple [Needleman-Wunsch implementation workbook](https://colab.research.google.com/github/shaunmahony/BMMB554-2022/blob/master/ipynb/PairwiseAlignment.ipynb) discussed in Lecture 11, make a Smith-Waterman alignment algorithm. Generate and compare global and local alignments of the following two sequences:
```
seq1 = "ACCGATGTACTGTAGGT"
seq2 = "GAGTCTACTGTTTAATC"
```
using the following scoring scheme:
- Gap penalty: -2
- Match score: +3
- Mismatch score: -1


## Question 2 (2 points)
From [GenBank](https://www.ncbi.nlm.nih.gov/protein/), export the amino acid sequences (in FASTA format) for the following proteins:
- Human KLF1 (Q13351)
- Human KLF6 (37655157)
- Mouse KLF1 (P46099)
- Mouse KLF6 (O08584)

The human KLF1 and mouse KLF1 proteins are orthologous. Human KLF1 and human KLF6 are paralogous, as are mouse KLF1 and KLF6.
Using the Galaxy EMBOSS tools, run the global aligner “needle” (Needleman-Wunsch) and the local aligner “water” (Smith-Waterman) for an orthologous comparison and at least one paralogous comparison. You should choose the same output options for each for ease of comparison (e.g. “simple” or “srspair”). Note that you can concatenate the sequences (by using “Concatenate queries” under “Text manipulation”) to get a combined sequence file. The EMBOSS tool “polydot” will give you a graphical picture of the positions of local alignments. Compare and contrast the outputs. 

Q2.1: How do the results of global and local alignment look for orthologous comparisons in terms of percent identity, similarity, gaps, etc.?
Q2.2: How do the results of global and local alignment look for paralogous comparisons in terms of percent identity, similarity, gaps, etc.?
Q2.3: What do the differences in similarities between orthologous and paralogous comparisons tell you about the conservation of different domains in the proteins?


## Question 3 (8 points)

Write a Python function to convert a genome sequence into a BWT, and write another function to reverse a BWT into a genome sequence. Use these functions to encode and decode the following genome sequence: GATCGATCAT

To make a BWT, you could start by generating all rotations of the original genome sequence (remembering to add the end-of-genome character). Here's how to make one rotation of a string in python:
```
def rotate(strg):
    return strg[-1:] + strg[:-1]
```
Then you need to sort the list of rotations and extract the last characters in each string.

To reverse a BWT, you need to first create your L-F mapping. Then iterate through the positions of the BWT as defined by the L-F mapping, starting from the end-of-genome character.
