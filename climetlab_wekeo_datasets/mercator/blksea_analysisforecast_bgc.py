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
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-bio_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-car_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202311",  # noqa: E501 cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-nut_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-opt_anfc_3km_P1M-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1D-m
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202311",  # noqa: E501 cmems_mod_blk_bgc-pft_anfc_3km_P1M-m
]


class blksea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "fpco2",
            "kd",
            "lght",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "ph",
            "phyc",
            "po4",
            "spco2",
            "talk",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-0.2546195089817047",
            "-0.7741973996162415",
            "-1.3163247108459473",
            "-1.8850828409194946",
            "-10.680734634399414",
            "-1008.3468627929688",
            "-108.27497100830078",
            "-1114.811767578125",
            "-12.15567684173584",
            "-1227.0989990234375",
            "-125.23257446289062",
            "-13.824886322021484",
            "-1344.841064453125",
            "-144.83216857910156",
            "-1467.6365966796875",
            "-15.722981452941895",
            "-1595.0645751953125",
            "-167.42984008789062",
            "-17.890621185302734",
            "-1726.698974609375",
            "-1862.119384765625",
            "-193.40847778320312",
            "-2.485290050506592",
            "-20.37550163269043",
            "-2000.9207763671875",
            "-2142.72021484375",
            "-223.173095703125",
            "-2287.16162109375",
            "-23.233518600463867",
            "-2433.66650390625",
            "-257.1440124511719",
            "-26.53006362915039",
            "-295.74755859375",
            "-3.122633695602417",
            "-3.8038270473480225",
            "-30.34151840209961",
            "-339.40447998046875",
            "-34.75691604614258",
            "-388.5162658691406",
            "-39.87977981567383",
            "-4.53679084777832",
            "-443.45037841796875",
            "-45.83015060424805",
            "-5.330871105194092",
            "-504.5245056152344",
            "-52.74676513671875",
            "-571.9923095703125",
            "-6.197091579437256",
            "-60.789329528808594",
            "-646.030517578125",
            "-7.14845085144043",
            "-70.1408462524414",
            "-726.7300415039062",
            "-8.200271606445312",
            "-81.0099105834961",
            "-814.0908203125",
            "-9.370611190795898",
            "-908.0220336914062",
            "-93.63275146484375",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-0.2546195089817047",
            "-0.7741973996162415",
            "-1.3163247108459473",
            "-1.8850828409194946",
            "-10.680734634399414",
            "-1008.3468627929688",
            "-108.27497100830078",
            "-1114.811767578125",
            "-12.15567684173584",
            "-1227.0989990234375",
            "-125.23257446289062",
            "-13.824886322021484",
            "-1344.841064453125",
            "-144.83216857910156",
            "-1467.6365966796875",
            "-15.722981452941895",
            "-1595.0645751953125",
            "-167.42984008789062",
            "-17.890621185302734",
            "-1726.698974609375",
            "-1862.119384765625",
            "-193.40847778320312",
            "-2.485290050506592",
            "-20.37550163269043",
            "-2000.9207763671875",
            "-2142.72021484375",
            "-223.173095703125",
            "-2287.16162109375",
            "-23.233518600463867",
            "-2433.66650390625",
            "-257.1440124511719",
            "-26.53006362915039",
            "-295.74755859375",
            "-3.122633695602417",
            "-3.8038270473480225",
            "-30.34151840209961",
            "-339.40447998046875",
            "-34.75691604614258",
            "-388.5162658691406",
            "-39.87977981567383",
            "-4.53679084777832",
            "-443.45037841796875",
            "-45.83015060424805",
            "-5.330871105194092",
            "-504.5245056152344",
            "-52.74676513671875",
            "-571.9923095703125",
            "-6.197091579437256",
            "-60.789329528808594",
            "-646.030517578125",
            "-7.14845085144043",
            "-70.1408462524414",
            "-726.7300415039062",
            "-8.200271606445312",
            "-81.0099105834961",
            "-814.0908203125",
            "-9.370611190795898",
            "-908.0220336914062",
            "-93.63275146484375",
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
        end_datetime="2024-02-01T00:00:00Z",
        start_datetime="2021-11-01T00:00:00Z",
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
