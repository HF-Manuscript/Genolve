from class_PathIdentification import PathIdentification
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification
from class_CorrectForInsertionsAndDeletions import CorrectForInsertionsAndDeletions

import sys

# Set the recursion limit
recursion_limit = 4000
sys.setrecursionlimit(recursion_limit)
rec_limit = sys.getrecursionlimit()

# Genolve driver code (This is the code that is run by the user at the current stage of development)
if __name__ == '__main__':

     # Input files
     filenameA = 'GenomeA.txt'
     filenameB = 'testerGB.txt'

     # Generate the lists of sequence blocks representing Genome A and B respectively
     generate_list_of_sequence_blocks = SequenceBlockAndEdgeSeriesIdentification()
     sequence_blocks_A = generate_list_of_sequence_blocks.list_sequence_blocks(filenameA)
     sequence_blocks_B = generate_list_of_sequence_blocks.list_sequence_blocks(filenameB)

     # Correct for the missing and additional sequence blocks in Genome B relative to Genome A
     find_large_indels = CorrectForInsertionsAndDeletions()
     correct_for_deletions = find_large_indels.find_missing_blocks(sequence_blocks_A, sequence_blocks_B)
     sequence_blocks_B = correct_for_deletions[0]
     deleted_sequence_blocks = correct_for_deletions[1]
     correct_for_insertions = find_large_indels.find_inserted_blocks(sequence_blocks_A, sequence_blocks_B)
     sequence_blocks_B = correct_for_insertions[0]
     inserted_sequnce_blocks = correct_for_insertions[1]

     # Use the recursive function to identify all paths of transformation
     execute = PathIdentification()
     path = []
     Paths = []
     level = 0
     Completely_transformed = []
     number_of_final_inversions = 0
     sequence_blocks = sequence_blocks_B
     Sets_of_operations = execute.identify_paths(sequence_blocks, path, Paths, level)


     # Print results to screen
     print('          PATHS')
     print()
     print('Number of paths:  ', len(Paths))
     print()

     for i in range(len(Sets_of_operations)):
          print('Path number: ', i+1)
          print(Sets_of_operations[i])
          print()
