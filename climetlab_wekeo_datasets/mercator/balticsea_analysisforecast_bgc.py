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
    "cmems_mod_bal_bgc-pp_anfc_P1D-i_202311",  # noqa: E501 cmems_mod_bal_bgc-pp_anfc_P1D-i
    "cmems_mod_bal_bgc_anfc_P1D-m_202311",  # noqa: E501 cmems_mod_bal_bgc_anfc_P1D-m
    "cmems_mod_bal_bgc_anfc_P1M-m_202311",  # noqa: E501 cmems_mod_bal_bgc_anfc_P1M-m
]


class balticsea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_BGC_003_007"
    dataset = "EO:MO:DAT:BALTICSEA_ANALYSISFORECAST_BGC_003_007"

    @normalize("layer", LAYERS)
    @normalize(
        "variables",
        [
            "chl",
            "dissic",
            "kd",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "o2b",
            "pH",
            "phyc",
            "po4",
            "si",
            "spCO2",
            "zooc",
            "zsd",
        ],
        multiple=True,
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "maximum_depth",
        [
            "-0.5016462206840515",
            "-1.5159924030303955",
            "-10.809036254882812",
            "-103.82470703125",
            "-117.62200164794922",
            "-12.270469665527344",
            "-13.857369422912598",
            "-132.66796875",
            "-148.90380859375",
            "-15.59900951385498",
            "-166.24795532226562",
            "-17.53092384338379",
            "-184.60281372070312",
            "-19.69594383239746",
            "-2.548084020614624",
            "-203.86167907714844",
            "-22.14525604248047",
            "-223.91526794433594",
            "-24.93938446044922",
            "-244.65684509277344",
            "-265.9862365722656",
            "-28.148958206176758",
            "-287.8121643066406",
            "-3.6022984981536865",
            "-31.855070114135742",
            "-310.0535583496094",
            "-332.6397399902344",
            "-355.5102233886719",
            "-36.14898681640625",
            "-378.6138000488281",
            "-4.684081077575684",
            "-401.9076843261719",
            "-41.13091278076172",
            "-425.3562927246094",
            "-448.93035888671875",
            "-46.907535552978516",
            "-472.60589599609375",
            "-496.3633728027344",
            "-5.80019998550415",
            "-520.1868896484375",
            "-53.58818435668945",
            "-544.0635375976562",
            "-567.98291015625",
            "-591.9366455078125",
            "-6.959054946899414",
            "-61.279541015625",
            "-615.9179077148438",
            "-639.9213256835938",
            "-663.9425048828125",
            "-687.9779052734375",
            "-70.07921600341797",
            "-712.024658203125",
            "-8.171056747436523",
            "-80.06874084472656",
            "-9.449085235595703",
            "-91.30695343017578",
        ],
    )
    @normalize(
        "minimum_depth",
        [
            "-0.5016462206840515",
            "-1.5159924030303955",
            "-10.809036254882812",
            "-103.82470703125",
            "-117.62200164794922",
            "-12.270469665527344",
            "-13.857369422912598",
            "-132.66796875",
            "-148.90380859375",
            "-15.59900951385498",
            "-166.24795532226562",
            "-17.53092384338379",
            "-184.60281372070312",
            "-19.69594383239746",
            "-2.548084020614624",
            "-203.86167907714844",
            "-22.14525604248047",
            "-223.91526794433594",
            "-24.93938446044922",
            "-244.65684509277344",
            "-265.9862365722656",
            "-28.148958206176758",
            "-287.8121643066406",
            "-3.6022984981536865",
            "-31.855070114135742",
            "-310.0535583496094",
            "-332.6397399902344",
            "-355.5102233886719",
            "-36.14898681640625",
            "-378.6138000488281",
            "-4.684081077575684",
            "-401.9076843261719",
            "-41.13091278076172",
            "-425.3562927246094",
            "-448.93035888671875",
            "-46.907535552978516",
            "-472.60589599609375",
            "-496.3633728027344",
            "-5.80019998550415",
            "-520.1868896484375",
            "-53.58818435668945",
            "-544.0635375976562",
            "-567.98291015625",
            "-591.9366455078125",
            "-6.959054946899414",
            "-61.279541015625",
            "-615.9179077148438",
            "-639.9213256835938",
            "-663.9425048828125",
            "-687.9779052734375",
            "-70.07921600341797",
            "-712.024658203125",
            "-8.171056747436523",
            "-80.06874084472656",
            "-9.449085235595703",
            "-91.30695343017578",
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
        end_datetime="2024-06-25T00:00:00Z",
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
