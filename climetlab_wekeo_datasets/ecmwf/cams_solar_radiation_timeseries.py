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

    @normalize("altitude")
    @normalize("latitude")
    @normalize("longitude")
    @normalize(
        "sky_type",
        [
            "clear",
            "observed_cloud",
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
        "time_step",
        [
            "15minute",
            "1day",
            "1hour",
            "1minute",
            "1month",
        ],
    )
    @normalize("dtend", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("dtstart", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "format_",
        [
            "csv",
            "csv_expert",
            "netcdf",
        ],
    )
    def __init__(
        self,
        altitude,
        latitude,
        longitude,
        sky_type,
        time_reference,
        time_step,
        dtend="2024-05-19",
        dtstart="2004-01-01",
        format_=None,
        limit=None,
    ):
        super().__init__(
            altitude=altitude,
            latitude=latitude,
            longitude=longitude,
            sky_type=sky_type,
            time_reference=time_reference,
            time_step=time_step,
            dtend=dtend,
            dtstart=dtstart,
            format_=format_,
            limit=limit,
        )
