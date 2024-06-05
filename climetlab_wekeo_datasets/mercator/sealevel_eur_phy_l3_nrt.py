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
    "cmems_obs-sl_eur_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311",  # noqa: E501 cmems_obs-sl_eur_phy-ssh_nrt_c2n-l3-duacs_PT1S_202311
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
    @normalize(
        "variables",
        [
            "dac",
            "ib_lf",
            "internal_tide",
            "lwe",
            "mdt",
            "ocean_tide",
            "ocean_tide",
            "sla_filtered",
            "sla_unfiltered",
            "xtdir",
            "xtgosa",
            "xtgosm",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
