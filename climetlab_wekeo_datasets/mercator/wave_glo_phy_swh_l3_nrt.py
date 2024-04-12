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
    "cmems_obs-wave_glo_phy-swh_nrt_al-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_al-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_c2-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_c2-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_cfo-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_cfo-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_h2b-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_h2b-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_h2c-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_h2c-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_j3-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_j3-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_s3a-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_s3a-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_s3b-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_s3b-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_s6a-l3_PT1S_202211",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_s6a-l3_PT1S_202211
    "cmems_obs-wave_glo_phy-swh_nrt_swon-l3_PT1S_202311",  # noqa: E501 cmems_obs-wave_glo_phy-swh_nrt_swon-l3_PT1S_202311
]


class wave_glo_phy_swh_l3_nrt(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L3_NRT_014_001"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L3_NRT_014_001"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "VAVH",
            "VAVH_UNFILTERED",
            "WIND_SPEED",
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2024-01-25T18:32:52Z",
        min_date="2021-01-01T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-wave_glo_phy-swh_nrt_al-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:27:03Z"

            if max_date is None:
                max_date = "2024-04-02T19:18:03Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_c2-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T18:12:18Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_cfo-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:34:11Z"

            if max_date is None:
                max_date = "2024-04-02T19:08:47Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_h2b-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-01-25T18:32:52Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_h2c-l3_PT1S_202211":
            if min_date is None:
                min_date = "2022-12-01T01:07:06Z"

            if max_date is None:
                max_date = "2024-03-31T19:58:05Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_j3-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:08:17Z"

            if max_date is None:
                max_date = "2024-03-19T19:20:59Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_s3a-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:14:33Z"

            if max_date is None:
                max_date = "2024-03-19T19:55:52Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_s3b-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-01-01T00:00:39Z"

            if max_date is None:
                max_date = "2024-04-02T19:54:25Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_s6a-l3_PT1S_202211":
            if min_date is None:
                min_date = "2021-09-21T00:02:30Z"

            if max_date is None:
                max_date = "2024-04-02T19:51:54Z"

        if layer == "cmems_obs-wave_glo_phy-swh_nrt_swon-l3_PT1S_202311":
            if min_date is None:
                min_date = "2023-08-01T04:38:25Z"

            if max_date is None:
                max_date = "2024-03-19T13:24:48Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
