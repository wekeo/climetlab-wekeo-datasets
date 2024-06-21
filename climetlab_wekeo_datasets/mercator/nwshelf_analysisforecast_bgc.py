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
    "cmems_mod_nws_bgc_anfc_0.027deg-3D_P1D-m_202311",  # noqa: E501 cmems_mod_nws_bgc_anfc_0.027deg-3D_P1D-m
    "cmems_mod_nws_bgc_anfc_0.027deg-3D_P1M-m_202311",  # noqa: E501 cmems_mod_nws_bgc_anfc_0.027deg-3D_P1M-m
]


class nwshelf_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_BGC_004_002"
    dataset = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_BGC_004_002"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "fe",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "zeu",
            "zooc",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-0.4940253794193268",
            "-1.5413753986358643",
            "-1062.439697265625",
            "-109.72927856445312",
            "-11.40500259399414",
            "-1245.2911376953125",
            "-13.467138290405273",
            "-130.66598510742188",
            "-1452.2509765625",
            "-15.810072898864746",
            "-155.85072326660156",
            "-1684.284423828125",
            "-18.495559692382812",
            "-186.1255645751953",
            "-1941.8934326171875",
            "-2.6456685066223145",
            "-21.59881591796875",
            "-222.4751739501953",
            "-2225.077880859375",
            "-25.211408615112305",
            "-2533.336181640625",
            "-266.0402526855469",
            "-2865.70263671875",
            "-29.44472885131836",
            "-3.8194947242736816",
            "-318.12744140625",
            "-3220.8203125",
            "-34.43415451049805",
            "-3597.031982421875",
            "-380.2130126953125",
            "-3992.48388671875",
            "-40.344051361083984",
            "-4405.22412109375",
            "-453.937744140625",
            "-47.373687744140625",
            "-4833.29052734375",
            "-5.078223705291748",
            "-5274.7841796875",
            "-541.0889282226562",
            "-55.76428985595703",
            "-5727.91650390625",
            "-6.440614223480225",
            "-643.5668334960938",
            "-65.8072738647461",
            "-7.92956018447876",
            "-763.3330688476562",
            "-77.85385131835938",
            "-9.572997093200684",
            "-902.3392944335938",
            "-92.3260726928711",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-0.4940253794193268",
            "-1.5413753986358643",
            "-1062.439697265625",
            "-109.72927856445312",
            "-11.40500259399414",
            "-1245.2911376953125",
            "-13.467138290405273",
            "-130.66598510742188",
            "-1452.2509765625",
            "-15.810072898864746",
            "-155.85072326660156",
            "-1684.284423828125",
            "-18.495559692382812",
            "-186.1255645751953",
            "-1941.8934326171875",
            "-2.6456685066223145",
            "-21.59881591796875",
            "-222.4751739501953",
            "-2225.077880859375",
            "-25.211408615112305",
            "-2533.336181640625",
            "-266.0402526855469",
            "-2865.70263671875",
            "-29.44472885131836",
            "-3.8194947242736816",
            "-318.12744140625",
            "-3220.8203125",
            "-34.43415451049805",
            "-3597.031982421875",
            "-380.2130126953125",
            "-3992.48388671875",
            "-40.344051361083984",
            "-4405.22412109375",
            "-453.937744140625",
            "-47.373687744140625",
            "-4833.29052734375",
            "-5.078223705291748",
            "-5274.7841796875",
            "-541.0889282226562",
            "-55.76428985595703",
            "-5727.91650390625",
            "-6.440614223480225",
            "-643.5668334960938",
            "-65.8072738647461",
            "-7.92956018447876",
            "-763.3330688476562",
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
        end_datetime="2024-06-22T00:00:00Z",
        start_datetime="2021-11-13T00:00:00Z",
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
