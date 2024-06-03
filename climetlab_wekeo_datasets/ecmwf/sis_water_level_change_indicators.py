#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class sis_water_level_change_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_WATER_LEVEL_CHANGE_INDICATORS"

    @normalize(
        "experiment",
        [
            "era5_reanalysis",
            "historical",
            "rcp4_5",
            "rcp8_5",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "100_years",
            "10_years",
            "10th",
            "25_years",
            "25th",
            "2_years",
            "50_years",
            "50th",
            "5_years",
            "75th",
            "90th",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "annual_highest_high_water_level",
            "annual_lowest_low_water_level",
            "annual_mean_highest_high_water_level",
            "annual_mean_lowest_low_water_level",
            "epoch_mean_highest_high_water_level",
            "epoch_mean_lowest_low_water_level",
            "highest_astronomical_tide",
            "lowest_astronomical_tide",
            "mean_sea_level",
            "surge_level",
            "tidal_range",
            "total_water_level",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(self, experiment, statistic, variable, format_=None, limit=None):
        super().__init__(
            experiment=experiment,
            statistic=statistic,
            variable=variable,
            format_=format_,
            limit=limit,
        )
