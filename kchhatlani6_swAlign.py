#!/usr/bin/python
import sys
#Taking input of two sequnces
input1 = sys.argv[1]
input2 = sys.argv[2]
#Storing the input as string
seq1_fasta = ""                              
seq2_fasta = ""

with open(input1) as fh1:
    for line in fh1.readlines():
        if line.startswith(">"):
            continue
        else:
            seq1_fasta += line
seq1_fasta = seq1_fasta.rstrip("\n")                        

#Storing the sequence 2 in seq2:
with open(input2) as fh2:
    for line in fh2.readlines():
        if line.startswith(">"):
            continue
        else:
            seq2_fasta += line
seq2_fasta = seq2_fasta.rstrip("\n")                        

#Initializing the matrix
m = len(seq1_fasta)                                   
n = len(seq2_fasta)                                  
matrix = []                                   
for i in range(m+1):                            
    submatrix = []
    for j in range(n+1):                        
        submatrix.append(0)
    matrix.append(submatrix)                                 

#Scoring system:
match = +1
mismatch = -1
gap = -1

#Matrix filling:
for i in range(1,m+1):
    for j in range(1, n+1):
        if seq1_fasta[i-1] == seq2_fasta[j-1]:
            matrix[i][j] = max(matrix[i][j-1]+gap, matrix[i-1][j]+gap, matrix[i-1][j-1]+match, 0)
        else:
            matrix[i][j] = max(matrix[i][j-1]+gap, matrix[i-1][j]+gap, matrix[i-1][j-1]+mismatch,0)

seq1 = ""                                 
seq2 = ""                                  
maximum = 0                                     
for row in range(1, m+1):
    for column in range(1,n+1):
        if maximum < matrix[row][column]:
            maximum = matrix[row][column]     
            i = row                             
            j = column                    

#Traceback:
while matrix[i][j] != 0:
    if seq1_fasta[i-1] == seq2_fasta[j-1]:
        seq1 += seq1_fasta[i-1]
        seq2 += seq2_fasta[j-1]
        i -= 1
        j -= 1

    #If it is a mismatch:
    elif seq1_fasta[i-1] != seq2_fasta[j-1]:
        templist = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]        

        #If the maximum value is the the diagonal value:
        if max(templist) == templist[0]:
            seq1 += seq1_fasta[i-1]
            seq2 += seq2_fasta[j-1]
            i -= 1
            j -= 1

        #If the maximum value is the top value:
        elif max(templist) == templist[1]:
            seq1 += seq1_fasta[i-1]
            seq2 += "-"
            i -= 1

        #If the maximum value is the left vlaue:
        elif max(templist) == templist[-1]:
            seq1 += "-"
            seq2 += seq2_fasta[j-1]
            j-=1

seq1_rev = seq1[::-1]                   
seq2_rev = seq2[::-1]                   

#Output in process:
symbols = ""
for i in range(len(seq1_rev)):
    if seq1_rev[i] == seq2_rev[i]:
        symbols += "|"
    elif seq1_rev[i] != seq2_rev[i]:
        if (seq1_rev[i] == "-" or seq2_rev[i] == "-"):
            symbols += " "
        else:
            symbols += "*"

#Alignment score:
alignment_score = 0
for i in range(len(symbols)):
    if symbols[i] == "|":
        alignment_score += 1
    elif (symbols[i] == "*" or symbols[i] == " "):
        alignment_score += -1

sys.stdout.write(seq1_rev)
sys.stdout.write('\n')
sys.stdout.write(symbols)
sys.stdout.write('\n')
sys.stdout.write(seq2_rev)
sys.stdout.write('\n')
sys.stdout.write('Alignment score:' + str(alignment_score))
sys.stdout.write('\n')