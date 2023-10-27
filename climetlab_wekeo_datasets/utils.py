import re

try:
    from functools import cache
except ImportError:
    # Python 3.8
    from functools import lru_cache

    cache = lru_cache(maxsize=None)

from importlib.metadata import entry_points
from typing import Dict, List, Tuple


class MissingDatasetError(Exception):
    pass


class UnsupportedDatasetError(Exception):
    pass


KEYS = {
    "boundingBoxValues",
    "stringInputValues",
    "datasetId",
    "dateRangeSelectValues",
    "multiStringSelectValues",
    "stringChoiceValues",
}

PREFIXES = {
    "eo:cgls": "clms",
    "eo:clms": "clms",
    "eo:ecmwf": "ecmwf",
    "eo:eum": "eum",
    "eo:mo": "mercator",
}

PATTERN_SHORT = re.compile(r"^-[\d]{3}-[\d]{3}$")
PATTERN_LONG = re.compile(r"^-[\d]{3}-[\d]{3}-[\w]$")


@cache
def valid_entry_points() -> List[str]:
    eps = entry_points()
    return [e.name for e in eps["climetlab.datasets"]]


def payload_to_args(payload) -> Dict:
    arguments = {}
    for key in KEYS:
        values = payload.get(key)
        if values is None:
            continue

        if key == "datasetId":
            if values.startswith("EO:MO:"):
                arguments["layer"] = values.split(":")[-1]

        elif key == "boundingBoxValues":
            try:
                area = values[0]
                bbox = area["bbox"]
                arguments["area"] = [
                    bbox[3],  # N
                    bbox[0],  # W
                    bbox[1],  # S
                    bbox[2],  # E
                ]
            except KeyError:
                pass

        elif key in (
            "stringInputValues",
            "stringChoiceValues",
            "multiStringSelectValues",
        ):
            for value in values:
                arguments[value["name"]] = value["value"]

        elif key == "dateRangeSelectValues":
            try:
                date_range = values[0]
                arguments["start"] = date_range["start"]
                arguments["end"] = date_range["end"]
            except KeyError:
                pass

    # Change back reserved words keys by appending an underscore
    reserved_words = ["format"]
    for key in reserved_words:
        if key in arguments:
            arguments[f"{key}_"] = arguments.pop(key)

    return arguments


def payload_to_entry(payload) -> str:
    if "datasetId" not in payload:
        raise MissingDatasetError("No dataset found in the payload.")

    dataset_id: str = payload["datasetId"].lower()

    if dataset_id.startswith("eo:mo"):
        dataset_id = ":".join(dataset_id.split(":")[:-1])

    try:
        prefix = PREFIXES[":".join(dataset_id.split(":")[:2])]
    except KeyError:
        raise UnsupportedDatasetError(f"Dataset {dataset_id} unsupported.")

    name = "-".join(dataset_id.split(":")[3:]).replace("_", "-")

    if PATTERN_SHORT.match(name[-8:]):
        name = name[:-8]

    elif PATTERN_LONG.match(name[-10:]):
        name = name[:-10]

    entry_point = f"wekeo-{prefix}-{name}"

    if entry_point not in valid_entry_points():
        raise UnsupportedDatasetError(f"Dataset {dataset_id} unsupported.")

    return entry_point


def hda2cml(payload) -> Tuple[str, Dict]:
    """
    Returns an entry point name and a dictionary of arguments
    from a valid WEkEO API request. Those can be directly
    injected into a load_dataset call.

    E.g:

    import climetlab as cml
    from climetlab_wekeo_datasets import hda2cml

    query = {
        "datasetId": "EO:MO:DAT:ARCTIC_ANALYSISFORECAST_BGC_002_004:cmems_mod_arc_bgc_anfc_ecosmo_P1D-m_202105",
        "dateRangeSelectValues": [
            {
            "name": "time",
            "start": "2019-01-01T00:00:00.000Z",
            "end": "2023-10-25T23:59:59.999Z"
            }
        ]
    }

    entry_point, arguments = hda2cml(query)
    dataset = cml.load_dataset(entry_point, **arguments)
    """
    return payload_to_entry(payload), payload_to_args(payload)
