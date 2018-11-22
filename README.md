# ChIP-seq_analysis
This script is takes advantage of the agrep tool provided by the TRE library in order to scan sequences for matches to a provided IUPAC DNA sequence. A certain number of mismatches can also be specified. The final result is a tab separated file including the sequence name, the matching sequence, and the number of mismatches. 

Example: alignToIUPAC.py NNNNNYTAWWWWTARNNNNN 2
 - Allows up to two mismatches, only best match will be shown