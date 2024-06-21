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
    "cmems_mod_glo_phy_my_0.083deg-climatology_P1M-m_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg-climatology_P1M-m
    "cmems_mod_glo_phy_my_0.083deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg_P1D-m
    "cmems_mod_glo_phy_my_0.083deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_phy_my_0.083deg_P1M-m
    "cmems_mod_glo_phy_myint_0.083deg_P1D-m_202311",  # noqa: E501 cmems_mod_glo_phy_myint_0.083deg_P1D-m
    "cmems_mod_glo_phy_myint_0.083deg_P1M-m_202311",  # noqa: E501 cmems_mod_glo_phy_myint_0.083deg_P1M-m
]


class global_multiyear_phy(Main):
    name = "EO:MO:DAT:GLOBAL_MULTIYEAR_PHY_001_030"
    dataset = "EO:MO:DAT:GLOBAL_MULTIYEAR_PHY_001_030"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "bottomT",
            "mlotst",
            "siconc",
            "sithick",
            "so",
            "thetao",
            "uo",
            "usi",
            "vo",
            "vsi",
            "zos",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-0.49402499198913574",
            "-1.5413750410079956",
            "-1062.43994140625",
            "-109.72930145263672",
            "-11.404999732971191",
            "-1245.291015625",
            "-13.467140197753906",
            "-130.66600036621094",
            "-1452.2509765625",
            "-15.810070037841797",
            "-155.85069274902344",
            "-1684.2840576171875",
            "-18.495559692382812",
            "-186.12559509277344",
            "-1941.8929443359375",
            "-2.6456689834594727",
            "-21.598819732666016",
            "-222.47520446777344",
            "-2225.077880859375",
            "-25.211410522460938",
            "-2533.3359375",
            "-266.0403137207031",
            "-2865.702880859375",
            "-29.444730758666992",
            "-3.8194949626922607",
            "-318.1274108886719",
            "-3220.820068359375",
            "-34.43415069580078",
            "-3597.031982421875",
            "-380.2130126953125",
            "-3992.48388671875",
            "-40.344051361083984",
            "-4405.22412109375",
            "-453.9377136230469",
            "-47.37369155883789",
            "-4833.291015625",
            "-5.078224182128906",
            "-5274.7841796875",
            "-541.0889282226562",
            "-55.76428985595703",
            "-5727.9169921875",
            "-6.440614223480225",
            "-643.5667724609375",
            "-65.80726623535156",
            "-7.92956018447876",
            "-763.3331298828125",
            "-77.85385131835938",
            "-9.572997093200684",
            "-902.3392944335938",
            "-92.3260726928711",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-0.49402499198913574",
            "-1.5413750410079956",
            "-1062.43994140625",
            "-109.72930145263672",
            "-11.404999732971191",
            "-1245.291015625",
            "-13.467140197753906",
            "-130.66600036621094",
            "-1452.2509765625",
            "-15.810070037841797",
            "-155.85069274902344",
            "-1684.2840576171875",
            "-18.495559692382812",
            "-186.12559509277344",
            "-1941.8929443359375",
            "-2.6456689834594727",
            "-21.598819732666016",
            "-222.47520446777344",
            "-2225.077880859375",
            "-25.211410522460938",
            "-2533.3359375",
            "-266.0403137207031",
            "-2865.702880859375",
            "-29.444730758666992",
            "-3.8194949626922607",
            "-318.1274108886719",
            "-3220.820068359375",
            "-34.43415069580078",
            "-3597.031982421875",
            "-380.2130126953125",
            "-3992.48388671875",
            "-40.344051361083984",
            "-4405.22412109375",
            "-453.9377136230469",
            "-47.37369155883789",
            "-4833.291015625",
            "-5.078224182128906",
            "-5274.7841796875",
            "-541.0889282226562",
            "-55.76428985595703",
            "-5727.9169921875",
            "-6.440614223480225",
            "-643.5667724609375",
            "-65.80726623535156",
            "-7.92956018447876",
            "-763.3331298828125",
            "-77.85385131835938",
            "-9.572997093200684",
            "-902.3392944335938",
            "-92.3260726928711",
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
        end_datetime="1993-12-01T00:00:00Z",
        start_datetime="1993-01-01T00:00:00Z",
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
