from operations.operations import operations_dict
from adapters import csv_adapter


def get_input_data_sources(input_file_paths, separated=False):
    """
    :return: list of input data
    """
    if separated:
        return [csv_adapter.get_rows(input_file_path) for input_file_path in input_file_paths]
    return [csv_adapter.get_rows_from_multiple_files(input_file_paths)]


def write_rows_to_file(input_data_sources, output_file_paths):
    if len(input_data_sources) != len(output_file_paths):
        raise Exception("output file paths number is not equal to the number of input data sources")

    [csv_adapter.write_rows(output_file_path, input_data_sources)
     for output_file_path, input_data_sources
     in zip(output_file_paths, input_data_sources)]


def union_input_data_sources(input_data_sources):
    return [(output_row for input_data_source in input_data_sources for output_row in input_data_source)]


def execute_coc_input_data_sources(input_data_sources, chain_of_commands):
    return \
        [_execute_chain_of_commands(input_data_source, chain_of_commands) for input_data_source in input_data_sources]


def _execute_chain_of_commands(input_data_source, chain_of_commands):
    """
    :param input_data_source: iterable. containing row
    :param chain_of_commands:
    this chain:
    pluck(11) -> max -> filter(0, 100)
    should be:
    [['pluck', 11], ['max'], ['filter', 0, 100]]
    :return: iterable of rows
    """
    current_command = chain_of_commands[0]
    remaining_commands = chain_of_commands[1:]
    operation_func = operations_dict[current_command[0]]

    current_bulk = operation_func(input_data_source, *current_command[1:])

    if remaining_commands:
        data_to_unload = _execute_chain_of_commands(current_bulk, remaining_commands)
    else:
        data_to_unload = current_bulk

    for output_row in data_to_unload:
        yield output_row
