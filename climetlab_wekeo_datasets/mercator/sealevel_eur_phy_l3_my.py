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
    "cmems_obs-sl_eur_phy-ssh_my_al-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_al-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_alg-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_alg-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_c2-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_c2-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_c2n-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_c2n-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_e1-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_e1-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_e1g-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_e1g-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_e2-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_e2-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_en-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_en-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_enn-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_enn-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_g2-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_g2-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_h2a-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_h2a-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_h2ag-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_h2ag-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_h2b-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_h2b-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_h2c-l3-duacs_PT1S_202207",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_h2c-l3-duacs_PT1S_202207
    "cmems_obs-sl_eur_phy-ssh_my_j1-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j1-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j1g-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j1g-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j1n-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j1n-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j2-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j2-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j2g-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j2g-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j2n-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j2n-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j3-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j3-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_j3n-l3-duacs_PT1S_202207",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_j3n-l3-duacs_PT1S_202207
    "cmems_obs-sl_eur_phy-ssh_my_s3a-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_s3a-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_s3b-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_s3b-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_s6a-lr-l3-duacs_PT1S_202207",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_s6a-lr-l3-duacs_PT1S_202207
    "cmems_obs-sl_eur_phy-ssh_my_tp-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_tp-l3-duacs_PT1S_202112
    "cmems_obs-sl_eur_phy-ssh_my_tpn-l3-duacs_PT1S_202112",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_my_tpn-l3-duacs_PT1S_202112
]


class sealevel_eur_phy_l3_my(Main):
    name = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_MY_008_061"
    dataset = "EO:MO:DAT:SEALEVEL_EUR_PHY_L3_MY_008_061"

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
            "internal_tide",
            "latitude",
            "longitude",
            "lwe",
            "mdt",
            "ocean_tide",
            "sla_filtered",
            "sla_unfiltered",
            "time",
            "tpa_correction",
            "track",
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
        if layer == "cmems_obs-sl_eur_phy-ssh_my_al-l3-duacs_PT1S_202112":
            if start is None:
                start = "2013-03-14T06:14:06Z"

            if end is None:
                end = "2015-03-31T20:35:37Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_alg-l3-duacs_PT1S_202112":
            if start is None:
                start = "2015-04-01T01:12:57Z"

            if end is None:
                end = "2022-08-04T20:12:23Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_c2-l3-duacs_PT1S_202112":
            if start is None:
                start = "2010-07-16T00:47:38Z"

            if end is None:
                end = "2020-07-31T10:42:28Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_c2n-l3-duacs_PT1S_202112":
            if start is None:
                start = "2020-08-01T11:21:18Z"

            if end is None:
                end = "2022-08-04T23:49:58Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_e1-l3-duacs_PT1S_202112":
            if start is None:
                start = "1992-10-23T22:39:06Z"

            if end is None:
                end = "1995-05-15T20:37:41Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_e1g-l3-duacs_PT1S_202112":
            if start is None:
                start = "1994-04-10T19:31:02Z"

            if end is None:
                end = "1995-03-20T23:18:04Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_e2-l3-duacs_PT1S_202112":
            if start is None:
                start = "1995-05-15T22:39:09Z"

            if end is None:
                end = "2002-05-14T12:38:43Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_en-l3-duacs_PT1S_202112":
            if start is None:
                start = "2002-05-24T18:12:23Z"

            if end is None:
                end = "2010-10-18T20:38:56Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_enn-l3-duacs_PT1S_202112":
            if start is None:
                start = "2010-10-26T08:08:12Z"

            if end is None:
                end = "2012-04-08T09:27:10Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_g2-l3-duacs_PT1S_202112":
            if start is None:
                start = "2000-01-09T05:45:18Z"

            if end is None:
                end = "2008-09-07T20:42:36Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_h2a-l3-duacs_PT1S_202112":
            if start is None:
                start = "2014-04-12T04:48:18Z"

            if end is None:
                end = "2016-03-15T19:33:34Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_h2ag-l3-duacs_PT1S_202112":
            if start is None:
                start = "2016-03-31T04:59:13Z"

            if end is None:
                end = "2020-06-09T18:50:30Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_h2b-l3-duacs_PT1S_202112":
            if start is None:
                start = "2019-12-21T04:37:37Z"

            if end is None:
                end = "2022-11-17T00:00:00Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_h2c-l3-duacs_PT1S_202207":
            if start is None:
                start = "2021-03-01T05:23:46Z"

            if end is None:
                end = "2021-03-02T19:27:47Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j1-l3-duacs_PT1S_202112":
            if start is None:
                start = "2002-04-24T15:12:17Z"

            if end is None:
                end = "2008-10-19T00:45:11Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j1g-l3-duacs_PT1S_202112":
            if start is None:
                start = "2012-05-07T17:11:40Z"

            if end is None:
                end = "2013-06-20T23:12:17Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j1n-l3-duacs_PT1S_202112":
            if start is None:
                start = "2009-02-10T18:01:39Z"

            if end is None:
                end = "2012-03-03T11:36:09Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j2-l3-duacs_PT1S_202112":
            if start is None:
                start = "2008-10-19T11:21:33Z"

            if end is None:
                end = "2016-05-26T09:53:26Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j2g-l3-duacs_PT1S_202112":
            if start is None:
                start = "2017-07-11T11:11:25Z"

            if end is None:
                end = "2017-09-14T04:31:05Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j2n-l3-duacs_PT1S_202112":
            if start is None:
                start = "2016-10-17T15:12:31Z"

            if end is None:
                end = "2017-04-03T18:12:43Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j3-l3-duacs_PT1S_202112":
            if start is None:
                start = "2016-05-26T20:30:11Z"

            if end is None:
                end = "2022-02-09T15:55:34Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_j3n-l3-duacs_PT1S_202207":
            if start is None:
                start = "2021-03-01T01:46:40Z"

            if end is None:
                end = "2022-08-04T21:43:13Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_s3a-l3-duacs_PT1S_202112":
            if start is None:
                start = "2016-03-01T20:10:50Z"

            if end is None:
                end = "2022-08-04T22:53:51Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_s3b-l3-duacs_PT1S_202112":
            if start is None:
                start = "2018-11-27T00:03:05Z"

            if end is None:
                end = "2022-08-04T22:15:40Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_s6a-lr-l3-duacs_PT1S_202207":
            if start is None:
                start = "2021-03-01T08:11:06Z"

            if end is None:
                end = "2022-08-04T22:47:46Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_tp-l3-duacs_PT1S_202112":
            if start is None:
                start = "1992-10-03T07:53:03Z"

            if end is None:
                end = "2002-04-24T04:38:01Z"

        if layer == "cmems_obs-sl_eur_phy-ssh_my_tpn-l3-duacs_PT1S_202112":
            if start is None:
                start = "2002-09-20T08:57:09Z"

            if end is None:
                end = "2005-10-08T23:49:27Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
