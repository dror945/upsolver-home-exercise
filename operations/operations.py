import math
import numbers


def _should_not_ignore(val):
    return isinstance(val, numbers.Number)


def _create_row(*args):
    return args


def _get_val_from_row(row, index=0):
    val = row[index]
    try:
        return int(val)
    except ValueError as e:
        try:
            return float(val)
        except ValueError as e:
            return val


def operation_sum(rows):
    the_sum = sum(_get_val_from_row(row) for row in rows if _should_not_ignore(_get_val_from_row(row)))

    yield _create_row(the_sum)


def operation_avg(rows):
    num_of_rows = 0
    the_sum = 0
    average = 0

    for row in rows:
        curr_val = _get_val_from_row(row)

        if _should_not_ignore(curr_val):
            the_sum += curr_val
            num_of_rows += 1

    if num_of_rows > 0:
        average = the_sum / num_of_rows
        yield _create_row(average)


def operation_min(rows):
    try:
        the_min = min(_get_val_from_row(row) for row in rows if _should_not_ignore(_get_val_from_row(row)))
    except ValueError as e:
        return  # In case of no rows

    yield _create_row(the_min)


def operation_max(rows):
    try:
        the_max = max((_get_val_from_row(row) for row in rows if _should_not_ignore(_get_val_from_row(row))))
    except ValueError as e:
        return  # In case of no rows

    yield _create_row(the_max)


def operation_ceil(rows):
    for row in rows:
        curr_val = _get_val_from_row(row)

        if _should_not_ignore(curr_val):
            yield _create_row(math.ceil(curr_val))


def operation_pluck(rows, val_index):
    for row in rows:
        curr_val = _get_val_from_row(row, val_index)

        yield _create_row(curr_val)


def operation_filter(rows, val_index, wanted_val):
    for row in rows:
        curr_val = _get_val_from_row(row, val_index)

        if curr_val == wanted_val:
            yield row


operations_dict = {
    'sum': operation_sum,
    'avg': operation_avg,
    'min': operation_min,
    'max': operation_max,
    'pluck': operation_pluck,
    'filter': operation_filter,
    'ceil': operation_ceil
}
