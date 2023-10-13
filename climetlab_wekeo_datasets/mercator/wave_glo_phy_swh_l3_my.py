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
    "cci_obs-wave_glo_phy-swh_my_al-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_al-l3_PT1S_202112
    "cci_obs-wave_glo_phy-swh_my_c2-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_c2-l3_PT1S_202112
    "cci_obs-wave_glo_phy-swh_my_en-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_en-l3_PT1S_202112
    "cci_obs-wave_glo_phy-swh_my_j1-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_j1-l3_PT1S_202112
    "cci_obs-wave_glo_phy-swh_my_j2-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_j2-l3_PT1S_202112
    "cci_obs-wave_glo_phy-swh_my_j3-l3_PT1S_202112",  # noqa: E501 cci_obs-wave_glo_phy-swh_my_j3-l3_PT1S_202112
    "cmems_obs-wave_glo_phy-swh_my_cfo-l3_PT1S_202112",  # noqa: E501 cmems_obs-wave_glo_phy-swh_my_cfo-l3_PT1S_202112
]


class wave_glo_phy_swh_l3_my(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L3_MY_014_005"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L3_MY_014_005"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "VAVH",
            "VAVH_UNFILTERED",
            "latitude",
            "longitude",
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
        if layer == "cci_obs-wave_glo_phy-swh_my_j1-l3_PT1S_202112":
            if start is None:
                start = "2002-01-15T06:29:22.022000Z"

            if end is None:
                end = "2012-03-03T12:59:11.022000Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_al-l3_PT1S_202112":
            if start is None:
                start = "2013-03-14T05:44:48.774000Z"

            if end is None:
                end = "2019-11-11T17:39:14.564000Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_c2-l3_PT1S_202112":
            if start is None:
                start = "2010-07-16T00:22:29.676000Z"

            if end is None:
                end = "2020-07-08T23:43:04.637000Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_j2-l3_PT1S_202112":
            if start is None:
                start = "2008-07-04T12:19:19.570000Z"

            if end is None:
                end = "2017-05-17T22:00:53.348000Z"

        if layer == "cmems_obs-wave_glo_phy-swh_my_cfo-l3_PT1S_202112":
            if start is None:
                start = "2018-11-03T08:42:31Z"

            if end is None:
                end = "2020-12-31T23:59:14Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_en-l3_PT1S_202112":
            if start is None:
                start = "2002-05-14T18:45:41.467000Z"

            if end is None:
                end = "2012-04-08T10:55:53.869000Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_j3-l3_PT1S_202112":
            if start is None:
                start = "2016-02-17T10:28:45.235000Z"

            if end is None:
                end = "2019-06-01T05:28:13.147000Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
