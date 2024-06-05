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

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "dac",
            "internal_tide",
            "lwe",
            "mdt",
            "ocean_tide",
            "sla_filtered",
            "sla_unfiltered",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    def __init__(self, layer, variables, bbox=None, limit=None):
        super().__init__(layer=layer, variables=variables, bbox=bbox, limit=limit)
