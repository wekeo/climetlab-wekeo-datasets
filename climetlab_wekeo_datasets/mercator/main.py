#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

import climetlab as cml
import xarray as xr
from climetlab import Dataset

__version__ = "0.1.0"


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
        layer = kwargs["layer"]
        area = kwargs.get("area")
        start = kwargs["start"]
        end = kwargs["end"]
        variables = kwargs.get("variables")

        query = {
            "datasetId": f"{self.dataset}:{layer}",
            "dateRangeSelectValues": [
                {"name": "position", "start": f"{start}", "end": f"{end}"}
            ],
        }

        if area is not None:
            query["boundingBoxValues"] = [
                {
                    "name": "bbox",
                    "bbox": [
                        area[1],
                        area[2],
                        area[3],
                        area[0],
                    ],
                }
            ]

        if variables is not None:
            query["multiStringSelectValues"] = [
                {"name": "variables", "value": variables}
            ]
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
            array = xr.concat(datasets, dim="time")
            self._xarray = array
            return self._xarray
        except (AttributeError, ValueError):
            # Single file
            self._xarray = super().to_xarray(**options)
            return self._xarray
