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


class cams_solar_radiation_timeseries(Main):
    name = "EO:ECMWF:DAT:CAMS_SOLAR_RADIATION_TIMESERIES"
    dataset = "EO:ECMWF:DAT:CAMS_SOLAR_RADIATION_TIMESERIES"
    inputs = [
        "latitude",
        "longitude",
        "altitude",
    ]
    choices = [
        "sky_type",
        "time_step",
        "time_reference",
        "format_",
    ]

    @normalize(
        "sky_type",
        [
            "clear",
            "observed_cloud",
        ],
    )
    @normalize(
        "time_step",
        [
            "15minute",
            "1day",
            "1hour",
            "1minute",
            "1month",
        ],
    )
    @normalize(
        "time_reference",
        [
            "true_solar_time",
            "universal_time",
        ],
    )
    @normalize(
        "format_",
        [
            "csv",
            "csv_expert",
            "netcdf",
        ],
    )
    @normalize("latitude")
    @normalize("longitude")
    @normalize("altitude")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        sky_type,
        time_step,
        time_reference,
        format_,
        latitude=None,
        longitude=None,
        altitude=None,
        start="2004-01-01",
        end="2023-09-10",
    ):
        super().__init__(
            sky_type=sky_type,
            time_step=time_step,
            time_reference=time_reference,
            format_=format_,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
            start=start,
            end=end,
        )
