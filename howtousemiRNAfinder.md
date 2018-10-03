# miRNA finder – part of raceRNA package (Krzyzosiak lab)

The python script was written by Tomasz Witkos and can be found online [here](https://github.com/krzyzosiak-lab/raceRNA/blob/master/mirnafinder.py). The scripts were used to produce supplementary data and figures presented in: A Potential Role of Extended Simple Sequence Repeats in Competing Endogenous RNA Crosstalk. Witkos TM, Krzyzosiak WJ, Fiszer A and Koscianska E.

## How does it work?

*Mirna finder* identifies miRNAs that can be potentially sequestered by single sequence repeats (SSRs). The program checks for complementarity between the repeat sequence and the miRNA seed region (nucleotides at positions 2 to 7 from 5’ end). The program requires a list of mature miRNAs (name + sequence) and a sequence of examined repeat, as defined by the user. The chosen repeat size must be between 3 and 6 nt and these size restrictions are due to the length of the miRNA seed region. Only miRNAs with at least 6 continuous matches between the repeat sequence and the miRNA seed are considered to be potentially sequestered by SSRs and only those are listed in the output file.

## Input file requirements
The user needs to provide an input file containing mature miRNA sequences in FASTA format. There is no limit of how many sequences can be examined. Please see the example input file *mirnalist.txt* for guidance. Mature miRNA sequences can be obtained from [miRBase](http://www.mirbase.org/ftp.shtml).

## Output file
The user is required to provide a desired name for the output file. The output file lists identified miRNAs with a potential to bind SSR in FASTA format.

## Example
Please run the program using provided *mirnalist.txt* as input file and choosing trinucleotide CCC repeat. As an output (*output_mirnafinder.txt*), only mir-3 is identified as potentially binding to the CCC repeats. MiR-3 seed region (GGGGGGU) contains GGGGGG stretch that is complementary to the examined CCC repeat unlike the other 2 miRNAs.
