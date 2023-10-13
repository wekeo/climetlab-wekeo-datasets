#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from enum import Enum

import climetlab as cml
import xarray as xr
from climetlab import Dataset

__version__ = "0.1.0"


class CombineStrategy(Enum):
    MERGE = 1
    CONCAT = 2


class MergeError(Exception):
    pass


class Main(Dataset):
    name = None
    home_page = "https://www.wekeo.eu/"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "https://www.copernicus.eu/en/access-data/copyright-and-licences"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://www.copernicus.eu/en/access-data/copyright-and-licence"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    default_options = {
        "xarray_open_dataset_kwargs": {"chunks": "auto", "engine": "netcdf4"}
    }

    string_selects = []
    inputs = []

    def __init__(self, *args, **kwargs):
        query = {
            "datasetId": f"{self.dataset}",
        }

        start = kwargs.get("start")
        end = kwargs.get("end")

        if start is not None and end is not None:
            query["dateRangeSelectValues"] = [
                {"name": "date", "start": f"{start}", "end": f"{end}"}
            ]

        choices = dict(zip(self.choices, [kwargs[c] for c in self.choices]))
        if any(c is not None for c in choices.values()):
            query["stringChoiceValues"] = []

            for choice in choices:
                if choices.get(choice) is not None:
                    if choice == "format_":
                        label = "format"
                    else:
                        label = choice

                    query["stringChoiceValues"].append(
                        {"name": label, "value": choices[choice]}
                    )

        string_selects = dict(
            zip(self.string_selects, [kwargs[v] for v in self.string_selects])
        )
        if any(v is not None for v in string_selects.values()):
            query["multiStringSelectValues"] = []

            for variable in string_selects:
                if string_selects.get(variable) is not None:
                    if variable == "format_":
                        label = "format"
                    else:
                        label = variable

                    query["multiStringSelectValues"].append(
                        {"name": label, "value": string_selects[variable]}
                    )

        inputs = dict(zip(self.inputs, [kwargs[i] for i in self.inputs]))
        if any(c is not None for c in inputs.values()):
            query["stringInputValues"] = []

            for input in inputs:
                if inputs.get(input) is not None:
                    query["stringInputValues"].append(
                        {"name": input, "value": f"{inputs[input]}"}
                    )

        self.source = cml.load_source("wekeo", query)
        self._xarray = None

    def to_xarray(self, **kwargs):
        if self._xarray is not None:
            return self._xarray

        options = dict()
        options.update(self.default_options["xarray_open_dataset_kwargs"])
        options.update(kwargs.get("xarray_open_dataset_kwargs", {}))

        try:
            datasets = [xr.open_dataset(s, **options) for s in self.source.sources]

            strategy = CombineStrategy.MERGE
            if len(datasets) > 1:
                current = datasets[0]
                for dataset in datasets[1:]:
                    if not dataset.time.equals(current.time):
                        # If times are all different, try to concat
                        # along that dimension
                        strategy = CombineStrategy.CONCAT
                        break
                    else:
                        current = dataset

            if strategy == CombineStrategy.MERGE:
                try:
                    array = xr.merge(datasets)
                except xr.MergeError as exc:
                    err = (
                        f"Cannot safely merge your data.\n"
                        f"Try to download a single variable or loop over the files and call `to_xarray` on each one.\n"
                        f"Original exception: {exc}"
                    )
                    raise MergeError(err)
            else:
                array = xr.concat(datasets, dim="time")

            self._xarray = array
            return self._xarray
        except AttributeError:
            # Single file
            self._xarray = super().to_xarray(**options)
            return self._xarray
