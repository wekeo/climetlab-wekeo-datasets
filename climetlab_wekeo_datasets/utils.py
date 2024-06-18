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


PREFIXES = {
    "eo:cgls": "clms",
    "eo:clms": "clms",
    "eo:ecmwf": "ecmwf",
    "eo:eum": "eum",
    "eo:mo": "mercator",
    "eo:eea": "clms",
}

PATTERN_SHORT = re.compile(r"^-[\d]{3}-[\d]{3}$")
PATTERN_LONG = re.compile(r"^-[\d]{3}-[\d]{3}-[\w]$")


@cache
def valid_entry_points() -> List[str]:
    eps = entry_points()
    return [e.name for e in eps["climetlab.datasets"]]


def payload_to_args(payload) -> Dict:
    # Change back reserved words keys by appending an underscore
    reserved_words = ["format"]
    for key in reserved_words:
        if key in payload:
            payload[f"{key}_"] = payload.pop(key)

    if "bbox" in payload:
        # HDA v2 order is WSEN, cml expects NWSE
        bbox = payload["bbox"]
        payload["bbox"] = [
            bbox[3],
            bbox[0],
            bbox[1],
            bbox[2],
        ]

    del payload["dataset_id"]
    return payload

    # arguments["area"] = [
    #                 bbox[3],  # N
    #                 bbox[0],  # W
    #                 bbox[1],  # S
    #                 bbox[2],  # E
    #


def payload_to_entry(payload) -> str:
    if "dataset_id" not in payload:
        raise MissingDatasetError("No dataset found in the payload.")

    dataset_id: str = payload["dataset_id"].lower()

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
    from a valid WEkEO v2 API request. Those can be directly
    injected into a load_dataset call.

    E.g:

    import climetlab as cml
    from climetlab_wekeo_datasets import hda2cml

    query = {
        "dataset_id": "EO:CLMS:DAT:CLMS_GLOBAL_ALBH_1KM_V1_10DAILY_NETCDF",
        "start": "2019-12-26T00:00:00.000Z",
        "end": "2020-01-25T00:00:00.000Z"
    }

    entry_point, arguments = hda2cml(query)
    dataset = cml.load_dataset(entry_point, **arguments)
    """
    return payload_to_entry(payload), payload_to_args(payload)
