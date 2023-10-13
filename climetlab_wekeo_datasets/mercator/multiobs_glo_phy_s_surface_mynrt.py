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
    "dataset-sss-ssd-nrt-monthly_202012",  # noqa: E501 Global analysed sea surface salinity and density monthly average
    "dataset-sss-ssd-nrt-weekly_202012",  # noqa: E501 Global analysed sea surface salinity and density
    "dataset-sss-ssd-rep-monthly_202012",  # noqa: E501 Global analysed sea surface salinity and density monthly average
    "dataset-sss-ssd-rep-weekly_202012",  # noqa: E501 Global analysed sea surface salinity and density
]


class multiobs_glo_phy_s_surface_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "depth",
            "dos",
            "dos_error",
            "lat",
            "lon",
            "sea_ice_fraction",
            "sos",
            "sos_error",
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
        if layer == "dataset-sss-ssd-rep-monthly_202012":
            if start is None:
                start = "2020-09-04T00:00:00Z"

            if end is None:
                end = "2022-10-24T00:00:00Z"

        if layer == "dataset-sss-ssd-nrt-weekly_202012":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-09-19T00:00:00Z"

        if layer == "dataset-sss-ssd-nrt-monthly_202012":
            if start is None:
                start = "2022-10-27T00:00:00Z"

            if end is None:
                end = "2023-05-31T00:00:00Z"

        if layer == "dataset-sss-ssd-rep-weekly_202012":
            if start is None:
                start = "2020-09-04T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
