import logic


def part_i():
    """
     We want to be able to process an entire CSV file using a chain of operations as defined bellow:
    """
    input_file_paths = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\0.csv"
    ]

    chain_of_commands = [['filter', 6, 'Johnson Heights'], ['pluck', 10], ['sum']]

    output_file_path = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_0.csv"
    ]

    input_data_sources = logic.get_input_data_sources(input_file_paths)

    output_rows = logic.execute_coc_input_data_sources(input_data_sources, chain_of_commands)

    logic.write_rows_to_file(output_rows, output_file_path)


def part_ii_option_one():
    """
    For each input file there is an output file containing the result of the chain in a CSV format
    """
    input_file_paths = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\0.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\1.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\2.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\3.csv",

    ]

    chain_of_commands = [['filter', 4, 'Bodefort'], ['pluck', 10], ['sum']]

    output_file_path = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_0.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_1.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_2.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_3.csv",
    ]

    input_data_sources = logic.get_input_data_sources(input_file_paths, separated=True)

    output_rows = logic.execute_coc_input_data_sources(input_data_sources, chain_of_commands)

    logic.write_rows_to_file(output_rows, output_file_path)


def part_ii_option_two():
    """
    Flatten - there is only one output file containing the result of the chain for all the input files together
    """
    input_file_paths = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\0.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\1.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\2.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\3.csv"
    ]

    chain_of_commands = [['filter', 4, 'Bodefort'], ['pluck', 10], ['sum']]

    output_file_path = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_0.csv"
    ]

    input_data_sources = logic.get_input_data_sources(input_file_paths)

    output_rows = logic.execute_coc_input_data_sources(input_data_sources, chain_of_commands)

    logic.write_rows_to_file(output_rows, output_file_path)


def part_iii():
    """
    Each CSV file given represents marks of a certain class.

    In this part, we would like to find the highest average mark between all classes. For that, we will need to run the process you've created in Part II in a chain:

    pluck(11) -> avg
    max (flattened)
    Implement a program that runs a "chain of chains" (where every chain's output is the input for the next chain).
    """
    input_file_paths = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\0.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\1.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\2.csv",
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\3.csv"
    ]

    first_coc = [['pluck', 10], ['avg']]
    second_coc = [['filter', 0, 68], ['min']]

    output_file_path = [
        r"C:\Users\dror9\PycharmProjects\upsolver_exercise\data\ans_0.csv"
    ]

    input_data_sources = logic.get_input_data_sources(input_file_paths, separated=True)

    avg_per_class = logic.execute_coc_input_data_sources(input_data_sources, first_coc)

    avg_of_all_class = logic.union_input_data_sources(avg_per_class)

    highest_average = logic.execute_coc_input_data_sources(avg_of_all_class, second_coc)

    logic.write_rows_to_file(highest_average, output_file_path)


if __name__ == '__main__':
    part_iii()
