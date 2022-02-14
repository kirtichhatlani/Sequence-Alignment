# Sequence-Alignment
Needleman-Wunsch (NW) algorithm  is  a  classical  bioinformatics  algorithm  designed  to obtain optimal global alignment for a given pair of sequences.  The algorithm falls under the class of dynamic programming which in simple language is the class of algorithm that work by breaking a problem into subproblems, solving each subproblem and joining the solutions to reach the global solution.The algorithm can be divided into three steps:
1. Initialization: Construction of the matrix with the two sequences as each axis and selection of a suitable scoring system.  For simplicity, let’s have three types of scores:
a. Match = +1
b. Mismatch = -1
c. Gap = -1
2. Matrix filling: Filling the matrix based on the scoring system.  This occurs one row at a time, starting from the topmost row.  Each cell in the matrix derives the value from the adjacent cells located to the left, top-left or on top of the current cell.  The match score is added or gap/mismatch penalty is subtracted from these adjacent cells and the maximum value is carried over to the current cell.
3. Backtracking: Once the matrix has been filled up, backtracking is done to compute the optimal alignment(s).  The backtracking step starts from the very last cell filled in the matrix (the bottom-right cell) and proceeds to the first cell filled in matrix. This backtrack path is computed by moving through  the  adjacent  cells  (cells  to  the  left,  top-left  and  on  top  of  the current  cell)  with  the  maximum  score  such  that  the  path  has  the maximum total score.  If multiple paths exist, then all of them are  considered  to  be  the  optimal  paths.    This  path  is  converted  to  an alignment by the following rule: the path moves diagonally to the left if there is a match or if the maximum score of the adjacent cells is present in the diagonal left cell.  If either of these are true, the two corresponding characters from each sequence are aligned together. When the maximum  score  is  obtained  by  moving  horizontally,  then  a  gap  is introduced in the sequence on the vertical axis, and if the path moves vertically,  then  a  gap  is  introduced  in  the  sequence  on  the  horizontal axis.
4. Syntax: ./ kchhatlani6_nwAlign.py <input FASTA file 1> <input FASTA file 2>

The  Smith-Waterman  algorithm  is  a  variant  of  Needleman-Wunsch  that  is applicable for local alignments.  The differences between the algorithms are:
1. There are no negative values within the matrix.  If subtracting a gap penalty or mismatch score results in a negative value, the value for the cell becomes 0.
2. The traceback starts with the cell with the highest value and ends when a 0 valued cell is encountered during the traceback.
3. The next local alignment starts with second highest score and ends at the first encountered 0 valued in the path.
4. Syntax: ./ kchhatlani6_swAlign.py <input FASTA file 1> <input FASTA file 2>
