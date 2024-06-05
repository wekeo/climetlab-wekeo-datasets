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

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "VAVH",
            "VAVH_UNFILTERED",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
