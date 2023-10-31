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
    "cmems_mod_arc_phy_anfc_topaz4_P1M-m_202211",  # noqa: E501 Arctic ocean physics analysis, 12.5km monthly mean
    "dataset-topaz4-arc-1hr-myoceanv2-be",  # noqa: E501 Arctic ocean physics analysis and forecast, 12.5km hourly instantaneous surface fields
    "dataset-topaz4-arc-myoceanv2-be",  # noqa: E501 Arctic ocean physics analysis and forecast, 12.5km daily mean (dataset-topaz4-arc-myoceanv2-be)
]


class arctic_analysis_forecast_phys(Main):
    name = "EO:MO:DAT:ARCTIC_ANALYSIS_FORECAST_PHYS_002_001_a"
    dataset = "EO:MO:DAT:ARCTIC_ANALYSIS_FORECAST_PHYS_002_001_a"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "albedo",
            "bsfd",
            "btemp",
            "depth",
            "fice",
            "fy_age",
            "fy_frac",
            "hice",
            "hsnow",
            "latitude",
            "longitude",
            "mlp",
            "model_depth",
            "salinity",
            "ssh",
            "stereographic",
            "temperature",
            "time",
            "u",
            "uice",
            "v",
            "vice",
            "x",
            "y",
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
        if layer == "cmems_mod_arc_phy_anfc_topaz4_P1M-m_202211":
            if start is None:
                start = "2018-01-01T00:00:00Z"

            if end is None:
                end = "2023-09-28T00:00:00Z"

        if layer == "dataset-topaz4-arc-1hr-myoceanv2-be":
            if start is None:
                start = "2018-01-01T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        if layer == "dataset-topaz4-arc-myoceanv2-be":
            if start is None:
                start = "2018-01-08T00:00:00Z"

            if end is None:
                end = "2023-10-27T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
