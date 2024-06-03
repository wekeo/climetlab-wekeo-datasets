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
    "cmems_obs-sl_glo_phy-ssh_nrt_al-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_al-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT1S_202311
]


class sealevel_glo_phy_l3_nrt(Main):
    name = "EO:MO:DAT:SEALEVEL_GLO_PHY_L3_NRT_008_044"
    dataset = "EO:MO:DAT:SEALEVEL_GLO_PHY_L3_NRT_008_044"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "cycle",
            "dac",
            "distance_from_theoretical",
            "flag",
            "ib_lf",
            "internal_tide",
            "latitude",
            "latitude_theoretical",
            "longitude",
            "longitude_theoretical",
            "lwe",
            "mdt",
            "ocean_tide",
            "sla_filtered",
            "sla_unfiltered",
            "time",
            "track",
            "xtdir",
            "xtgosa",
            "xtgosm",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer,
        max_date="2024-05-06T06:36:46Z",
        min_date="2023-11-09T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_al-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:05:49Z"

            if max_date is None:
                max_date = "2024-05-06T19:44:58Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:10:45Z"

            if max_date is None:
                max_date = "2024-05-06T15:59:16Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:18:10Z"

            if max_date is None:
                max_date = "2023-09-03T23:59:59Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-04T16:46:05Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:18:10Z"

            if max_date is None:
                max_date = "2024-05-06T14:18:52Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-05-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T14:18:52Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T13:58:07Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T13:58:07Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T14:55:32Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:12:33Z"

            if max_date is None:
                max_date = "2024-05-06T14:55:31Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:10:35Z"

            if max_date is None:
                max_date = "2024-05-06T14:52:29Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-03-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T14:52:29Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:00:00Z"

            if max_date is None:
                max_date = "2024-05-06T06:36:46Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:00:01Z"

            if max_date is None:
                max_date = "2024-05-06T06:36:46Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
