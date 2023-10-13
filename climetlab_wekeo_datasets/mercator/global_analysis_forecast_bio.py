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
    "global-analysis-forecast-bio-001-028-daily_202211",  # noqa: E501 Daily mean fields from global ocean biogeochemistry analysis and forecast
    "global-analysis-forecast-bio-001-028-monthly_202211",  # noqa: E501 Monthly mean fields for product global analysis forecast bio 001 028
]


class global_analysis_forecast_bio(Main):
    name = "EO:MO:DAT:GLOBAL_ANALYSIS_FORECAST_BIO_001_028"
    dataset = "EO:MO:DAT:GLOBAL_ANALYSIS_FORECAST_BIO_001_028"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "dissic",
            "fe",
            "latitude",
            "longitude",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "talk",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "global-analysis-forecast-bio-001-028-monthly_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-08-28T00:00:00Z"

        if layer == "global-analysis-forecast-bio-001-028-daily_202211":
            if start is None:
                start = "0201-10-01T00:00:00Z"

            if end is None:
                end = "2023-09-29T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
