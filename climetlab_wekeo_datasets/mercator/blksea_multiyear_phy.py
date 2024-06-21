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
    "cmems_mod_blk_phy-cur_my_2.5km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_phy-cur_my_2.5km_P1D-m
    "cmems_mod_blk_phy-cur_my_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-cur_my_2.5km_P1M-m
    "cmems_mod_blk_phy-cur_my_2.5km_P1Y-m_202211",  # noqa: E501 cmems_mod_blk_phy-cur_my_2.5km_P1Y-m
    "cmems_mod_blk_phy-cur_myint_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-cur_myint_2.5km_P1M-m
    "cmems_mod_blk_phy-mld_my_2.5km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_phy-mld_my_2.5km_P1D-m
    "cmems_mod_blk_phy-mld_my_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-mld_my_2.5km_P1M-m
    "cmems_mod_blk_phy-mld_my_2.5km_P1Y-m_202211",  # noqa: E501 cmems_mod_blk_phy-mld_my_2.5km_P1Y-m
    "cmems_mod_blk_phy-mld_myint_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-mld_myint_2.5km_P1M-m
    "cmems_mod_blk_phy-sal_my_2.5km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_phy-sal_my_2.5km_P1D-m
    "cmems_mod_blk_phy-sal_my_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-sal_my_2.5km_P1M-m
    "cmems_mod_blk_phy-sal_my_2.5km_P1Y-m_202211",  # noqa: E501 cmems_mod_blk_phy-sal_my_2.5km_P1Y-m
    "cmems_mod_blk_phy-sal_myint_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-sal_myint_2.5km_P1M-m
    "cmems_mod_blk_phy-ssh_my_2.5km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_phy-ssh_my_2.5km_P1D-m
    "cmems_mod_blk_phy-ssh_my_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-ssh_my_2.5km_P1M-m
    "cmems_mod_blk_phy-ssh_my_2.5km_P1Y-m_202211",  # noqa: E501 cmems_mod_blk_phy-ssh_my_2.5km_P1Y-m
    "cmems_mod_blk_phy-ssh_myint_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-ssh_myint_2.5km_P1M-m
    "cmems_mod_blk_phy-tem_my_2.5km_P1D-m_202211",  # noqa: E501 cmems_mod_blk_phy-tem_my_2.5km_P1D-m
    "cmems_mod_blk_phy-tem_my_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-tem_my_2.5km_P1M-m
    "cmems_mod_blk_phy-tem_my_2.5km_P1Y-m_202211",  # noqa: E501 cmems_mod_blk_phy-tem_my_2.5km_P1Y-m
    "cmems_mod_blk_phy-tem_myint_2.5km_P1M-m_202211",  # noqa: E501 cmems_mod_blk_phy-tem_myint_2.5km_P1M-m
]


class blksea_multiyear_phy(Main):
    name = "EO:MO:DAT:BLKSEA_MULTIYEAR_PHY_007_004"
    dataset = "EO:MO:DAT:BLKSEA_MULTIYEAR_PHY_007_004"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "so",
            "thetao",
            "uo",
            "vo",
            "zos",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-101.56743621826172",
            "-1109.21923828125",
            "-118.27472686767578",
            "-12.536195755004883",
            "-1342.7784423828125",
            "-140.41339111328125",
            "-1595.2430419921875",
            "-17.583404541015625",
            "-170.27761840820312",
            "-1862.253173828125",
            "-2.5010786056518555",
            "-210.8994598388672",
            "-2140.020751953125",
            "-22.66373634338379",
            "-266.0666809082031",
            "-27.79346466064453",
            "-32.996856689453125",
            "-340.1394348144531",
            "-38.31007385253906",
            "-43.7869758605957",
            "-437.5660400390625",
            "-49.507728576660156",
            "-55.59150695800781",
            "-562.0991821289062",
            "-62.21519470214844",
            "-69.64064025878906",
            "-7.51119327545166",
            "-715.9151611328125",
            "-78.25402069091797",
            "-88.62169647216797",
            "-899.013916015625",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-101.56743621826172",
            "-1109.21923828125",
            "-118.27472686767578",
            "-12.536195755004883",
            "-1342.7784423828125",
            "-140.41339111328125",
            "-1595.2430419921875",
            "-17.583404541015625",
            "-170.27761840820312",
            "-1862.253173828125",
            "-2.5010786056518555",
            "-210.8994598388672",
            "-2140.020751953125",
            "-22.66373634338379",
            "-266.0666809082031",
            "-27.79346466064453",
            "-32.996856689453125",
            "-340.1394348144531",
            "-38.31007385253906",
            "-43.7869758605957",
            "-437.5660400390625",
            "-49.507728576660156",
            "-55.59150695800781",
            "-562.0991821289062",
            "-62.21519470214844",
            "-69.64064025878906",
            "-7.51119327545166",
            "-715.9151611328125",
            "-78.25402069091797",
            "-88.62169647216797",
            "-899.013916015625",
        ],
    )
    @normalize("end_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("start_datetime", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        layer,
        variables,
        bbox=None,
        maximum_depth=None,
        minimum_depth=None,
        end_datetime="2024-04-01T00:00:00Z",
        start_datetime="2021-07-01T00:00:00Z",
        limit=None,
    ):
        super().__init__(
            layer=layer,
            variables=variables,
            bbox=bbox,
            maximum_depth=maximum_depth,
            minimum_depth=minimum_depth,
            end_datetime=end_datetime,
            start_datetime=start_datetime,
            limit=limit,
        )
