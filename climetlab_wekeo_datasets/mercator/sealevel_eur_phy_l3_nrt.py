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
    "cmems_obs-sl_eur_phy-ssh_nrt_al-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_al-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311
    "cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT1S_202311
]


class sealevel_eur_phy_l3_nrt(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_NRT_008_059"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_NRT_008_059"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
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
        layer,
        bbox,
        max_date="2024-04-02T12:31:27Z",
        min_date="2022-01-01T09:14:23Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_al-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T03:04:52Z"

            if max_date is None:
                max_date = "2024-04-01T19:49:52Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T08:04:18Z"

            if max_date is None:
                max_date = "2024-04-01T15:52:00Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T07:13:10Z"

            if max_date is None:
                max_date = "2023-09-03T19:49:17Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T04:48:48Z"

            if max_date is None:
                max_date = "2024-03-31T09:28:38Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2022-11-04T00:07:18Z"

            if max_date is None:
                max_date = "2024-04-02T11:12:04Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-03-14T01:03:00Z"

            if max_date is None:
                max_date = "2024-04-02T11:12:04Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2022-11-04T08:19:03Z"

            if max_date is None:
                max_date = "2024-04-02T12:31:27Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T09:14:23Z"

            if max_date is None:
                max_date = "2024-04-02T12:31:27Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2022-11-04T09:16:16Z"

            if max_date is None:
                max_date = "2024-04-02T11:57:52Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T08:40:02Z"

            if max_date is None:
                max_date = "2024-04-02T11:57:52Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2022-11-04T01:16:28Z"

            if max_date is None:
                max_date = "2024-04-02T12:11:58Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-03-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T12:11:57Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:36:43Z"

            if max_date is None:
                max_date = "2024-04-02T03:49:11Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_swon-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:36:44Z"

            if max_date is None:
                max_date = "2024-04-02T03:49:10Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
