import numpy as np


class SequenceBlockAndEdgeSeriesIdentification:
    def __init__(self):
        pass

    def __del__(self):
        pass

    ## Reads the tab-delimited text file into a list of sequence blocks
    def list_sequence_blocks(self, filename):

        sequence_blocks = []
        block_positions = []

        # Generation of the list of sequence blocks from the tab-delimited text file
        names_and_positions_of_sequence_blocks = np.loadtxt(filename, delimiter='\t', unpack=True, dtype=object)
        sequence_block_names = names_and_positions_of_sequence_blocks[0, :]
        sequence_block_positions = names_and_positions_of_sequence_blocks[1, :]

        for i in range(0, len(sequence_block_names)):
            sequence_blocks.append(int(sequence_block_names[i]))
            block_positions.append(tuple(sequence_block_positions[i]))
            # (The block_positions variable will be incorporated at a later stage of development)

        return sequence_blocks

    ## Generation of the edge series (a list of non-consecutive edge pairs)
    def generate_edge_series(self, sequence_blocks):

        edge_series = []

        for i in range(0, len(sequence_blocks) - 1):
            if int(sequence_blocks[i + 1]) - int(sequence_blocks[i]) == 1:
                pass

            elif int(sequence_blocks[i + 1]) - int(sequence_blocks[i]) == -1:
                pass

            else:
                edge = (int(sequence_blocks[i]), int(sequence_blocks[i + 1]))
                edge_series.append(edge)

        return edge_series
