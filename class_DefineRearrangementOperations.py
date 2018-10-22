class DefineRearrangementOperations:
    def __init__(self):
        pass

    def __del__(self):
        pass

    ## Identification of inversion rearrangement operations
    def inversion_identification(self, working_edge_series):

        edge_series = []
        Inversion_operations = []

        edge_series.extend(working_edge_series)

        # For each edge_pair in the edge_series:
        # 1. Calculate the possible edge pair partners for the current edge pair.
        # 2. Determine whether an inversion partner is present in the list of edge pairs.
        # 3. If present, append the current edge pair and its edge_pair partner to the list of Inversions

        for edge_pair in range(len(edge_series)):
            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)

            # 1. Calculation of edge pair partners
            if orientation_edge1 > 0:
                compatible_edge_partner_1 = (abs(edge1) + 1) * orientation_edge1 * (-1)

            else:
                compatible_edge_partner_1 = (abs(edge1) - 1) * orientation_edge1 * (-1)

            if orientation_edge2 > 0:
                compatible_edge_partner_2 = (abs(edge2) - 1) * orientation_edge2 * (-1)

            else:
                compatible_edge_partner_2 = (abs(edge2) + 1) * orientation_edge2 * (-1)

            inversion_partner = (int(compatible_edge_partner_1), int(compatible_edge_partner_2))

            # 2. Determination of whether an edge_pair partner is present in the edge_series
            if inversion_partner in edge_series:
                x = int(inversion_partner[0])
                y = int(inversion_partner[1])

                inversion_partner = (x, y)
                inversion_partner_position = edge_series.index(inversion_partner)
                edge_series[inversion_partner_position] = (1, 1)

            # 3. Append the edge_pair and the edge_pair partner to the list of inversions
                Inversion_operations.append((current_edge_pair, inversion_partner))

            else:
                pass

        return Inversion_operations

    ## Identification of transpositions rearrangement operations
    def transposition_identification(self, edge_series, sequence_blocks):

        Transposition_operations = []

        # For each edge pair in the edge_series:
        # 1. Calculate the sequence blocks bordering the compatible block of sequence blocks
        # 2. Determine whether the transposition of the sequence blocks to the edge pair is a valid operation
        # 3. If the operation is valid, append it to the list of Transpositions

        for edge_pair in range(len(edge_series)):
            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)

            # 1. Calculation of sequence blocks bordering the compatible block of sequence blocks
            if orientation_edge1 > 0:
                compatible_sequence_block_1 = (abs(edge1) + 1) * orientation_edge1

            else:
                compatible_sequence_block_1 = (abs(edge1) - 1) * orientation_edge1

            if orientation_edge2 > 0:
                compatible_sequence_block_2 = (abs(edge2) - 1) * orientation_edge2

            else:
                compatible_sequence_block_2 = (abs(edge2) + 1) * orientation_edge2

            compatible_sequence_block = (int(compatible_sequence_block_1), int(compatible_sequence_block_2))

            # 2. Determination of whether the transposition of the sequence blocks is a valid operation
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                # 3. Append the edge_pair and sequence blocks bordering the compatible block of sequence blocks to the list of transpositions
                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Transposition_operations.append((current_edge_pair, compatible_sequence_block))

                elif position_block1 == position_block2:
                    Transposition_operations.append((current_edge_pair, compatible_sequence_block))

                else:
                    pass

            else:
                pass

        #Removal of equvalent transposition operations from the list of transpositions
        remove_equivalent_operations = DefineRearrangementOperations()
        Final_transposition_operations = remove_equivalent_operations.removal_of_equivalent_transpositions(Transposition_operations,sequence_blocks)

        return Final_transposition_operations

    ## Identification of inverted transposition rearrangement operations
    def inverted_transposition_identification(self, edge_series, sequence_blocks):

        Inverted_Transposition_operations = []

        # For each edge_pair in the edge_series:
        # 1. Calculate the sequence blocks bordering the compatible block of sequence blocks
        # 2. Determine whether the inverted transposition of the sequence blocks to the edge pair is a valid operation
        # 3. If the operation is valid, append it to the list of Inverted_transpositions

        for edge_pair in range(len(edge_series)):
            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)

            # 1. Calculation of the compatible block of sequence blocks
            if orientation_edge1 > 0:
                compatible_sequence_block_1 = (abs(edge1) + 1) * orientation_edge1 * (-1)

            else:
                compatible_sequence_block_1 = (abs(edge1) - 1) * orientation_edge1 * (-1)

            if orientation_edge2 > 0:
                compatible_sequence_block_2 = (abs(edge2) - 1) * orientation_edge2 * (-1)

            else:
                compatible_sequence_block_2 = (abs(edge2) + 1) * orientation_edge2 * (-1)

            compatible_sequence_block = (int(compatible_sequence_block_2), int(compatible_sequence_block_1))

            # 2. Determination of whether the inverted transposition of the sequence blocks is a valid operation
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                # 3. Append the edge_pair and sequence blocks bordering the compatible block of sequence blocks to the list of inverted transpositions
                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Inverted_Transposition_operations.append((current_edge_pair, compatible_sequence_block))

                elif position_block1 == position_block2:
                    Inverted_Transposition_operations.append((current_edge_pair, compatible_sequence_block))

                else:
                    pass

            else:
                pass

        return Inverted_Transposition_operations

    ## Removal of equivalent transpositions from the list of transpositions
    #  (i.e. in [1,2,3,7,8,4,5,6,9,10] the movement of block [7,8] to edge_pair(6,9) is equivalent to that of
    #   block [4,5,6] to edge_pair(3,7)
    def removal_of_equivalent_transpositions(self, Transpositions, sequence_blocks):

        i = 0
        while i < len(Transpositions):
            current_translocation = Transpositions[i]

            j = 0
            while j < len(Transpositions):
                other_translocation = Transpositions[j]

                if sequence_blocks.index(current_translocation[1][1]) == sequence_blocks.index(
                        other_translocation[1][0]) - 1 and sequence_blocks.index(current_translocation[1][0]) == sequence_blocks.index(other_translocation[0][1]):

                    Transpositions.remove(other_translocation)

                else:
                    pass

                j += 1
            i += 1

        return Transpositions
