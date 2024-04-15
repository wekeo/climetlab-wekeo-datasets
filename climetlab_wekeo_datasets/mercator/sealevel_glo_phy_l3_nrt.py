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
        max_date="2024-04-02T12:50:27Z",
        min_date="2023-09-01T00:18:10Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_al-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:05:49Z"

            if max_date is None:
                max_date = "2024-04-02T19:18:11Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:10:45Z"

            if max_date is None:
                max_date = "2024-04-02T18:12:18Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:18:10Z"

            if max_date is None:
                max_date = "2023-09-03T23:59:59Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_h2b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-03-31T14:33:38Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:18:10Z"

            if max_date is None:
                max_date = "2024-04-02T12:50:27Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-05-03T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T12:50:26Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T13:40:28Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T13:40:27Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T13:03:35Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-01-01T00:12:33Z"

            if max_date is None:
                max_date = "2024-04-02T13:03:34Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-09-01T00:10:35Z"

            if max_date is None:
                max_date = "2024-04-02T13:51:50Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2022-03-16T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T13:51:50Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT0.2S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:00:00Z"

            if max_date is None:
                max_date = "2024-04-02T13:15:13Z"

        if layer == "cmems_obs-sl_glo_phy-ssh_nrt_swon-l3-duacs_PT1S_202311":
            if min_date is None:
                min_date = "2023-11-09T00:00:01Z"

            if max_date is None:
                max_date = "2024-04-02T13:15:13Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
