import csv


def get_rows(file_path, skip_header_line=True):
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        if skip_header_line:
            next(csv_reader)

        for row in csv_reader:
            yield row


def get_rows_from_multiple_files(file_paths):
    for file_path in file_paths:
        for row in get_rows(file_path):
            yield row


def write_rows(file_path, rows):
    with open(file_path, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
