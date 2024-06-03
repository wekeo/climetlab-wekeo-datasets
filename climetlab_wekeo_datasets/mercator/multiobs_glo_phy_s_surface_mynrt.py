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
    "cmems_obs-mob_glo_phy-sss_my_multi_P1D_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi_P1D
    "cmems_obs-mob_glo_phy-sss_my_multi_P1M_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_my_multi_P1M
    "cmems_obs-mob_glo_phy-sss_nrt_multi_P1D_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_nrt_multi_P1D
    "cmems_obs-mob_glo_phy-sss_nrt_multi_P1M_202311",  # noqa: E501 cmems_obs-mob_glo_phy-sss_nrt_multi_P1M
    "dataset-sss-ssd-nrt-monthly_202012",  # noqa: E501 dataset-sss-ssd-nrt-monthly_202012
    "dataset-sss-ssd-nrt-weekly_202012",  # noqa: E501 dataset-sss-ssd-nrt-weekly_202012
    "dataset-sss-ssd-rep-monthly_202012",  # noqa: E501 dataset-sss-ssd-rep-monthly_202012
    "dataset-sss-ssd-rep-weekly_202012",  # noqa: E501 dataset-sss-ssd-rep-weekly_202012
]


class multiobs_glo_phy_s_surface_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-14T00:00:00Z",
        min_date="2023-09-07T00:00:00Z",

        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-mob_glo_phy-sss_my_multi_P1D_202311":
            if min_date is None:
                min_date = "2023-03-22T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-16T00:00:00Z"

        if layer == "cmems_obs-mob_glo_phy-sss_my_multi_P1M_202311":
            if min_date is None:
                min_date = "2023-10-06T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-17T00:00:00Z"

        if layer == "cmems_obs-mob_glo_phy-sss_nrt_multi_P1D_202311":
            if min_date is None:
                min_date = "2023-09-07T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-14T00:00:00Z"

        if layer == "cmems_obs-mob_glo_phy-sss_nrt_multi_P1M_202311":
            if min_date is None:
                min_date = "2023-10-09T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-15T00:00:00Z"

        if layer == "dataset-sss-ssd-nrt-monthly_202012":
            if min_date is None:
                min_date = "2022-10-27T00:00:00Z"

            if max_date is None:
                max_date = "2023-05-31T00:00:00Z"

        if layer == "dataset-sss-ssd-nrt-weekly_202012":
            if min_date is None:
                min_date = "2022-11-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-27T00:00:00Z"

        if layer == "dataset-sss-ssd-rep-monthly_202012":
            if min_date is None:
                min_date = "2020-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2022-10-24T00:00:00Z"

        if layer == "dataset-sss-ssd-rep-weekly_202012":
            if min_date is None:
                min_date = "2020-09-04T00:00:00Z"

            if max_date is None:
                max_date = "2022-11-01T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            
            variables=variables,
            limit=limit,
        )
