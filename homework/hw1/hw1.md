# Homework 1

**Due:** end of day, Friday, Feb 11th.

**How to submit?**
* Share your Google colab workbooks with sam77@psu.edu (make sure you are sharing access with me and not just sending me a link)
* If the questions ask for written descriptions or the conclusions you draw from the analyses, write them in text blocks within your colab notebook(s). 


## Question 1: Pandas DataFrames (2 points)
In [lecture 4](https://hackmd.io/@shaunmahony/rk-5fTgnF/%2F90ejemwPRSKws976s6Llww), we saw a table describing the numbers of SARS-CoV-2 sequencing experiments in the SRA, broken down by Library Strategy and Platform. That table was created in January 2021 from metadata describing ~190k relevant experiments that existed in the SRA at that time. 

This year, we have been using a table describing ~2.5 million SARS-CoV-2 experiments in the SRA. Build an equivalent experiment counts table (i.e., broken down by Library Strategy and Platform) from the 2022 SRA metadata that we have been using (https://github.com/shaunmahony/BMMB554-2022/raw/main/data/sra_ncov_bmmb554_2022.csv.gz).

*Hint*: review the [Pandas2 workbook](https://colab.research.google.com/github/shaunmahony/BMMB554-2022/blob/master/ipynb/Pandas2.ipynb) if you're stuck. 

**Do you notice any major differences in sequencing trends between this year and last year?
**

## Question 2: What's the best starting Wordle word? (4 points)

[Wordle](https://www.powerlanguage.co.uk/wordle/) has been taking the internet by storm over the past few weeks. For those (few) of you who have not heard of it yet, it's a simple word guessing game. The goal is to guess a random 5-letter word. You get 6 guesses. After each guess, the letters in your guess turn green if the guessed letter is in the correct position, orange if the letter is in the answer word but you have it in the wrong position, and grey if the letter you typed is not in the answer word. So, you can gain some information from each guess that will inform your next guess. If you haven't already, go play a game to get a sense of how it works: https://www.powerlanguage.co.uk/wordle. Note that only one game is made available per day.

After playing, you'll probably start to wonder whether there is some "best" or optimally informative word that you should use as your starting guess. This is an interesting question, and has connections to information theoretic problems that we come across in bioinformatics all the time. In this homework question, I want you to use Python to come up with some answers. 

Here's a list of all 5-letter words that Wordle accepts as legitimate guesses: https://raw.githubusercontent.com/shaunmahony/BMMB554-2022/main/homework/hw1/wordlewords.txt

Your job is to find the most informative word. You can define "informative" as you wish, as long as two conditions are met:
* You clearly describe your definition and rationale in the workbook.
* You perform a search over all words in the above file to find a word that maximizes your definition of "informative". 

If it were me, I would stick with a classic information content approach. You could first count how often each possible letter is used in the list of words. The word with the highest information content would then be a word that contains a combination of the most frequently occurring letters. Such a word would literally be the word that maximizes your chances to turn Wordle boxes green or orange. More specifically, the approach could be:
* Count the occurrences of each letter (a-z) in the file. These counts become the "score" associated with each letter. 
* Score each possible word by summing the per-letter scores. 
* Sort the words by score. 

**Provide me with a list of the 10 most informative words and the 10 least informative words.**


## Question 3: Do sequencing errors impact read mapping rates? (4 points)

In Lecture 5, we familiarized ourselves with the FASTQ file format in this notebook: (https://colab.research.google.com/github/shaunmahony/BMMB554-2022/blob/master/ipynb/FASTQ.ipynb). We learned how the quality string letters encode probability values, which in turn represent the probabilities that the corresponding sequenced base is incorrectly called by the sequencer. We also defined functions in the workbook that can help you to convert between FASTQ quality letters and the probability values. 

Here, I want you to use a collection of real Illumina FASTQ quality strings to simulate "sequencing errors" in a collection of sequences that have been sampled at random from the human genome (hg38 build). You will then map the "simulated" reads back to the genome (using your choice of aligner like BWA or Bowtie). Compare the uniquely mapping read rates between the perfectly sampled reads and the simulated sequencing error reads. Use your observations to answer the question: **Do typical sequencing error rates impact read alignment?**

Here's the data you'll need:
* 1M perfectly sampled 50bp sequences from hg38
    * FASTA format (gzipped): https://raw.githubusercontent.com/shaunmahony/BMMB554-2022/main/homework/hw1/rand1M.fa.gz 
    * FASTQ format (gzipped) with fake "perfect" quality scores: https://raw.githubusercontent.com/shaunmahony/BMMB554-2022/main/homework/hw1/rand1M.fq.gz
* 1M Illumina quality scores (50bp length)
    * TXT format (gzipped): https://raw.githubusercontent.com/shaunmahony/BMMB554-2022/main/homework/hw1/quals1M.txt.gz

How will you simulate sequencing errors? I would do something like the following:
* Read in the FASTA sequences and the quality score strings. Pair them up (there are 1M of each).
* Iterate through each sequence & quality string  pair:
    * Iterate through each character in the quality string
        * Convert the quality character to a p-value
        * Roll a dice with a random number generator.
        * If the random number is less than the p-value, "mutate" the base in the corresponding position in the sequence. If the sequence letter was an A, replace with a random choice from C,G,T, etc. 
        * Otherwise leave the base in the corresponding sequence position alone. 
* Print all sequence/quality string pairs out in FASTQ format (the name of the sequence can be random or related to the FASTA header - doesn't really matter).

After making your simulated sequences, map them and the "perfect" FASTQ format file above to hg38 (Galaxy or command line is fine). Check mapping rates. 

If you're interested, you can further check whether the reads are being mapped to the *correct* positions (there are contained in the names of the FASTA sequences), but this is not required for the homework assignment. 

