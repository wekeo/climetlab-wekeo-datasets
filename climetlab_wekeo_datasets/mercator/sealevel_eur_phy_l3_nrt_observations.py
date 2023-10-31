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
    "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_h2c-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_h2c-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202207",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202207
    "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202211",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202211
    "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202112
    "dataset-duacs-nrt-europe-al-phy-l3_202003",  # noqa: E501 dataset-duacs-nrt-europe-al-phy-l3_202003
    "dataset-duacs-nrt-europe-c2-phy-l3_202003",  # noqa: E501 dataset-duacs-nrt-europe-c2-phy-l3_202003
    "dataset-duacs-nrt-europe-c2n-phy-l3_202010",  # noqa: E501 dataset-duacs-nrt-europe-c2n-phy-l3_202010
    "dataset-duacs-nrt-europe-h2b-phy-l3_202007",  # noqa: E501 dataset-duacs-nrt-europe-h2b-phy-l3_202007
    "dataset-duacs-nrt-europe-j3-phy-l3_202003",  # noqa: E501 dataset-duacs-nrt-europe-j3-phy-l3_202003
    "dataset-duacs-nrt-europe-s3a-phy-l3_202003",  # noqa: E501 dataset-duacs-nrt-europe-s3a-phy-l3_202003
    "dataset-duacs-nrt-europe-s3b-phy-l3_202003",  # noqa: E501 dataset-duacs-nrt-europe-s3b-phy-l3_202003
]


class sealevel_eur_phy_l3_nrt_observations(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_NRT_OBSERVATIONS_008_059"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_NRT_OBSERVATIONS_008_059"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
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
        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_h2b-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-09-20T07:45:57Z"

            if end is None:
                end = "2022-09-21T18:40:49Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_h2c-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-09-20T07:45:57Z"

            if end is None:
                end = "2022-09-21T18:40:49Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-11-04T00:07:18Z"

            if end is None:
                end = "2023-06-26T03:58:55Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_j3n-l3-duacs_PT1S_202207":
            if start is None:
                start = "2022-03-14T01:03:00Z"

            if end is None:
                end = "2023-06-26T09:59:16Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3a-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-11-04T08:19:03Z"

            if end is None:
                end = "2023-06-25T22:27:56Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s3b-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-11-04T09:16:16Z"

            if end is None:
                end = "2023-06-25T23:24:45Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT0.2S_202211":
            if start is None:
                start = "2022-11-04T01:16:28Z"

            if end is None:
                end = "2023-06-26T03:11:11Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S_202112":
            if start is None:
                start = "2022-03-16T00:00:00Z"

            if end is None:
                end = "2023-06-26T09:05:32Z"

        if layer == "dataset-duacs-nrt-europe-al-phy-l3_202003":
            if start is None:
                start = "2019-09-17T03:32:29Z"

            if end is None:
                end = "2023-06-26T18:21:27Z"

        if layer == "dataset-duacs-nrt-europe-c2-phy-l3_202003":
            if start is None:
                start = "2019-04-01T09:38:41Z"

            if end is None:
                end = "2020-07-13T01:31:32Z"

        if layer == "dataset-duacs-nrt-europe-c2n-phy-l3_202010":
            if start is None:
                start = "2020-10-09T06:06:45Z"

            if end is None:
                end = "2023-06-26T08:35:36Z"

        if layer == "dataset-duacs-nrt-europe-h2b-phy-l3_202007":
            if start is None:
                start = "2020-05-06T05:23:49Z"

            if end is None:
                end = "2023-06-25T17:55:20Z"

        if layer == "dataset-duacs-nrt-europe-j3-phy-l3_202003":
            if start is None:
                start = "2019-04-01T01:04:45Z"

            if end is None:
                end = "2022-04-04T19:49:00Z"

        if layer == "dataset-duacs-nrt-europe-s3a-phy-l3_202003":
            if start is None:
                start = "2019-04-01T09:02:00Z"

            if end is None:
                end = "2023-06-26T12:19:12Z"

        if layer == "dataset-duacs-nrt-europe-s3b-phy-l3_202003":
            if start is None:
                start = "2019-04-01T08:20:28Z"

            if end is None:
                end = "2023-06-26T13:11:06Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
