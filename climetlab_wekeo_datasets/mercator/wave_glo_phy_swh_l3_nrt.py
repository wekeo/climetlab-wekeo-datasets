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
    @normalize(
        "variables",
        [
            "VAVH",
            "VAVH_UNFILTERED",
            "WIND_SPEED",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
