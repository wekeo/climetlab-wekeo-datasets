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


class sis_ocean_wave_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_OCEAN_WAVE_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_OCEAN_WAVE_INDICATORS"

    @normalize(
        "experiment",
        [
            "era5_reanalysis",
            "historical",
            "rcp4_5",
            "rcp8_5",
        ],
    )
    @normalize(
        "period",
        [
            "1976_2005",
            "2001_2017",
            "2041_2070",
            "2071_2100",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "100_year_return_period",
            "90th_100th_percentile_average",
            "90th_percentile",
            "95th_percentile",
            "99th_percentile",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "peak_wave_period",
            "significant_wave_height",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self, experiment, period, statistic, variable, format_=None, limit=None
    ):
        super().__init__(
            experiment=experiment,
            period=period,
            statistic=statistic,
            variable=variable,
            format_=format_,
            limit=limit,
        )
