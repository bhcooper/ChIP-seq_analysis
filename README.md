# ChIP-seq_analysis
This script takes advantage of the agrep tool provided by the TRE library in order to scan DNA sequences for matches to a provided IUPAC sequence. A specified number of mismatches can also be specified. The final result is a tab separated file including the name, matching sequence, and number of mismatches. 

Example: alignToIUPAC.py intersection.fa NNNNNYTAWWWWTARNNNNN 2
 - Allows up to two mismatches, only best match will be shown