#!/usr/bin/python

num_genes = 30000 #protein coding genes
avg_length = 3000.0  # avg. base pairs
total_genomes = 3E9  # total base pairs

#Approximate total gene coding length
total_gene_length = num_genes * avg_length

#Proportion of coding genes in genome
proportion_gene = total_gene_length / total_genomes

#Print answers
print total_gene_length, proportion_gene

sequence = 'ASDFQWERTY'
first_aa = sequence[0]
second_aa = sequence[1]
last_aa = sequence[-1]  #read backwards with negative indices
sec2_last_aa = sequence[-2]
print sequence, first_aa, second_aa, last_aa, sec2_last_aa

#Indexing example with lists
positions = [1, 3, 7, 11, 22, 'one million', '42']
first_pos = positions[0]
sec_pos = positions[1]
last_pos = positions[-1]
sec2_last_pos = positions[-2]
print positions, first_pos, sec_pos, last_pos, sec2_last_pos

#Access multiple sequencial elements. This is called slicing.
mid_two_aa = sequence[4:6]  #This will give the 5th and 6th element
first_3_aa = sequence[0:3]
second_2_pos = positions[1:3]
last_two_pos = positions[-2:]
print mid_two_aa, first_3_aa, second_2_pos, last_two_pos

for aa in sequence:
    print aa

for pos in positions[:-2]:  #Loop through all but the last 2 pos
    pos_after = pos+1
    print pos, pos_after

if first_aa == 'R':
    print 'It is arginine'
else:
    print 'It is NOT arginie'

for aa in sequence:
    if aa == 'R':
        print aa, 'is R'
    else:
        print aa, 'is NOT R'
    if aa in ['K', 'Y']:
        print aa, 'is K or Y'


    