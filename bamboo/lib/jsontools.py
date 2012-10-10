import numpy as np
from pandas import Series

from bamboo.lib.utils import is_float_nan


# JSON encoding string
JSON_NULL = 'null'


class JSONError(Exception):
    """
    For errors while parsing JSON.
    """
    pass


def get_json_value(value):
    if is_float_nan(value):
        value = JSON_NULL
    elif isinstance(value, np.int64):
        value = int(value)
    elif isinstance(value, np.bool_):
        value = bool(value)
    return value


def series_to_jsondict(series):
    return series if series is None else dict([
        (unicode(key), get_json_value(value))
        for key, value in series.iteritems()
    ])


def df_to_jsondict(dframe):
    return [series_to_jsondict(series) for idx, series in dframe.iterrows()]
