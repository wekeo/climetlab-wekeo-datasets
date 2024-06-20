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

    def __init__(self, *args, **kwargs):
        query = {
            "dataset_id": f"{self.dataset}",
        }
        limit = kwargs.pop("limit", None)

        for key, value in kwargs.items():
            if key == "format_":
                key = "format"
            if value is not None:
                query[key] = value

        self.source = cml.load_source("wekeo", query, limit)
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
