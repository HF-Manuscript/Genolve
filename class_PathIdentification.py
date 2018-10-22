from class_DefineRearrangementOperations import DefineRearrangementOperations
from class_RearrangementOperationExecution import RearrangementOperationExecution
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification


class PathIdentification:

    def __init__(self):
        pass

    def __del__(self):
        pass

    def identify_paths(self, sequence_blocks, path, Paths, level):

        # Generate edge_series
        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)

        # Define rearrangement operations
        find_rearrangement_operations = DefineRearrangementOperations()
        Inversions = find_rearrangement_operations.inversion_identification(edge_series)
        Transpositions = find_rearrangement_operations.transposition_identification(edge_series, sequence_blocks)
        Inverted_transpositions = find_rearrangement_operations.inverted_transposition_identification(edge_series, sequence_blocks)

        Operations = []
        Operations.extend(Inversions)
        Operations.extend(Transpositions)
        Operations.extend(Inverted_transpositions)

        if len(Operations) != 0:
          Operations.append('Catch_all')

        find_paths = PathIdentification()

        if len(edge_series) == 0:
            Paths.append(path[:])
            path.pop()
            level -= 1
            pass

        elif len(Operations) == 0:
           print('This algorithm was unable to resolve all paths of transformation for the current input.')
           print('Further development of the algorithm is currently underway and will adress instances such as these.')
           print('Please try a different input or use one of the sample input files provided.')
           print()
           path.pop()
           level -= 1
           pass

        else:
            level += 1
            for i in range(len(Operations)):
                current_opperation = Operations[i]

                if current_opperation == 'Catch_all':
                    if level == 1:
                        break

                    else:
                        path.pop()
                        level -= 1
                        pass

                else:
                    execute_operation = RearrangementOperationExecution()
                    execute = execute_operation.execute_operations(current_opperation, Inversions, Transpositions, Inverted_transpositions, sequence_blocks)
                    new_sequence_blocks = execute[0]
                    path.append(execute[1])

                    find_paths.identify_paths(new_sequence_blocks, path, Paths, level)

        return Paths
