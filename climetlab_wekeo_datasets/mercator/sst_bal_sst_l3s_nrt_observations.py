#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_datasets.mercator.main import Main

LAYERS = [
    "DMI-BALTIC-SST-L3S-NRT-OBS_FULL_TIME_SERIE_201904",  # noqa: E501 DMI-BALTIC-SST-L3S-NRT-OBS_FULL_TIME_SERIE
]


class sst_bal_sst_l3s_nrt_observations(Main):
    name = "EO:MO:DAT:SST_BAL_SST_L3S_NRT_OBSERVATIONS_010_032"
    dataset = "EO:MO:DAT:SST_BAL_SST_L3S_NRT_OBSERVATIONS_010_032"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "lat",
            "lon",
            "mask",
            "or_number_of_sst_pixels",
            "quality_level",
            "sea_ice_fraction",
            "sea_surface_temperature",
            "source_of_sst",
            "sses_bias",
            "sses_standard_deviation",
            "sst_dtime",
            "sum_square_sst",
            "sum_sst",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="DMI-BALTIC-SST-L3S-NRT-OBS_FULL_TIME_SERIE_201904",
        max_date="2024-03-30T00:00:00Z",
        min_date="2019-03-11T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "DMI-BALTIC-SST-L3S-NRT-OBS_FULL_TIME_SERIE_201904":
            if min_date is None:
                min_date = "2019-03-11T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-30T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
