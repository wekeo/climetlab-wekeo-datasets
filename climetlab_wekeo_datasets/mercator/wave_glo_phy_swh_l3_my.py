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

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
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
    def __init__(
        self,
        bbox,
        layer,
        max_date="2020-07-08T23:43:04Z",
        min_date="2010-07-16T00:22:29Z",
        variables=None,
        limit=None,
    ):
        if layer == "cci_obs-wave_glo_phy-swh_my_al-l3_PT1S_202112":
            if min_date is None:
                min_date = "2013-03-14T05:44:48Z"

            if max_date is None:
                max_date = "2019-11-11T17:39:14Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_c2-l3_PT1S_202112":
            if min_date is None:
                min_date = "2010-07-16T00:22:29Z"

            if max_date is None:
                max_date = "2020-07-08T23:43:04Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_en-l3_PT1S_202112":
            if min_date is None:
                min_date = "2002-05-14T18:45:41Z"

            if max_date is None:
                max_date = "2012-04-08T10:55:53Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_j1-l3_PT1S_202112":
            if min_date is None:
                min_date = "2002-01-15T06:29:22Z"

            if max_date is None:
                max_date = "2012-03-03T12:59:11Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_j2-l3_PT1S_202112":
            if min_date is None:
                min_date = "2008-07-04T12:19:19Z"

            if max_date is None:
                max_date = "2017-05-17T22:00:53Z"

        if layer == "cci_obs-wave_glo_phy-swh_my_j3-l3_PT1S_202112":
            if min_date is None:
                min_date = "2016-02-17T10:28:45Z"

            if max_date is None:
                max_date = "2019-06-01T05:28:13Z"

        if layer == "cmems_obs-wave_glo_phy-swh_my_cfo-l3_PT1S_202112":
            if min_date is None:
                min_date = "2018-11-03T08:42:31Z"

            if max_date is None:
                max_date = "2020-12-31T23:59:14Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
