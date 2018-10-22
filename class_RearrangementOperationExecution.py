class RearrangementOperationExecution:
    def __init__(self):
        pass

    def __del__(self):
        pass

    ## Identifies the type of rearrangement operation and calls its function of execution
    def execute_operations(self, current_operation, Inversions, Transpositions, Inverted_transpositions, sequence_blocks ):

        excecute_operation = RearrangementOperationExecution()

        if current_operation in Inversions:
            classification = 'Inv'
            excecute_inversion = excecute_operation.excecute_inversion(current_operation, sequence_blocks)
            new_sequence_blocks = excecute_inversion[0]
            inversion_position = excecute_inversion[1] # (Variable to be used in VCF output in future development)
            operation = (classification, current_operation)

        elif current_operation in Transpositions:
            classification = 'Trn'
            excecute_transposition = excecute_operation.excecute_transposition(current_operation, sequence_blocks)
            new_sequence_blocks = excecute_transposition[0]
            transposition_position = excecute_transposition[1] # (Variable to be used in VCF output in future development)
            operation = (classification, current_operation)

        elif current_operation in Inverted_transpositions:
            classification = 'Inv_trn'
            excecute_inverted_transposition = excecute_operation.excecute_inverted_transposition(current_operation, sequence_blocks)
            new_sequence_blocks = excecute_inverted_transposition[0]
            inverted_transposition_position = excecute_inverted_transposition[1] # (Variable to be used in VCF output in future development)
            operation = (classification, current_operation)

        return (new_sequence_blocks, operation)

    ## Execution of an inversion rearrangement operation
    def excecute_inversion(self, inversion, sequence_blocks):

        inverted_sequence = []

        temp = sequence_blocks[sequence_blocks.index(inversion[0][1]):sequence_blocks.index(inversion[1][0])+1]
        # temp = the segment of sequence blocks to be inverted

        # Determination of the inversion position
        inversion_position = ((sequence_blocks.index(inversion[0][1]), sequence_blocks.index(inversion[1][0])+1))

        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)

        new_sequence_blocks = sequence_blocks[:sequence_blocks.index(inversion[0][0])+1] + inverted_sequence[::-1] + sequence_blocks[sequence_blocks.index(inversion[1][1]):]

        return new_sequence_blocks, inversion_position

    ## Execution of a transposition rearrangement operation
    def excecute_transposition(self, transposition, sequence_blocks):

        temp = sequence_blocks[sequence_blocks.index(transposition[1][0]):sequence_blocks.index(transposition[1][1])+1]
        # temp = the segment of sequence blocks to be transposed

        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(transposition[1][0])] + sequence_blocks[sequence_blocks.index(transposition[1][1])+1:]
        # temp_sequence_blocks = the list of sequence blocks with the segment to be transposed removed

        new_sequence_blocks = temp_sequence_blocks[:temp_sequence_blocks.index(transposition[0][0])+1] + temp[::] + temp_sequence_blocks[temp_sequence_blocks.index(transposition[0][1]):]

        # Determination of the transposition position
        transposition_position = ((sequence_blocks.index(transposition[1][0]),sequence_blocks.index(transposition[1][1])+1),sequence_blocks.index(transposition[0][0]))

        return new_sequence_blocks, transposition_position

    ## Execution of an inverted transposition rearrangement operation
    def excecute_inverted_transposition(self, inverted_transposition, sequence_blocks):

        inverted_sequence = []

        temp = sequence_blocks[sequence_blocks.index(inverted_transposition[1][0]):sequence_blocks.index(inverted_transposition[1][1])+1]
        # temp = segment of sequence blocks to be inverted and transposed

        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)

        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(inverted_transposition[1][0])] + sequence_blocks[sequence_blocks.index(inverted_transposition[1][1])+1:]
        # temp_sequence_blocks = the list of sequence blocks with the segment to be inverted and transposed removed

        new_sequence_blocks = temp_sequence_blocks[:temp_sequence_blocks.index(inverted_transposition[0][0])+1] +inverted_sequence[::-1] + temp_sequence_blocks[temp_sequence_blocks.index(inverted_transposition[0][1]):]

        # Determination of the inverted transposition position
        inverted_transposition_position = ((sequence_blocks.index(inverted_transposition[1][0]),sequence_blocks.index(inverted_transposition[1][1])+1),sequence_blocks.index(inverted_transposition[0][0] ))

        return new_sequence_blocks, inverted_transposition_position
