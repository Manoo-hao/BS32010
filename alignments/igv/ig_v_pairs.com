output_file=ig_v_pairs.out
mode=pairwise
matrix_file=blosum62.mat
pairwise_random=0,0,1
gap_penalty=12.0
constant=0
seq_file=ig_v.pir
