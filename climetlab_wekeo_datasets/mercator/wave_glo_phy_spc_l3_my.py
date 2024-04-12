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
    "dataset-wav-sar-l3-spc-rep-global-s1a_202105",  # noqa: E501 dataset-wav-sar-l3-spc-rep-global-s1a_202105
    "dataset-wav-sar-l3-spc-rep-global-s1b_202105",  # noqa: E501 dataset-wav-sar-l3-spc-rep-global-s1b_202105
]


class wave_glo_phy_spc_l3_my(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L3_MY_014_006"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SPC_L3_MY_014_006"

    @normalize("layer", LAYERS)
    @normalize("bbox", "bounding-box(list)")
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "%2Fexp_params%2Ffoc_latitude",
            "%2Fexp_params%2Ffoc_longitude",
            "%2Fexp_params%2Ffoc_size",
            "%2Fexp_params%2Ffoc_size_across",
            "%2Fexp_params%2Ffoc_size_along",
            "%2Fexp_params%2Ffoc_time",
            "%2Fobs_params%2FL2_partition_quality_flag",
            "%2Fobs_params%2FL2_source_product",
            "%2Fobs_params%2FVAVH",
            "%2Fobs_params%2FVAVH_flag",
            "%2Fobs_params%2FVPED",
            "%2Fobs_params%2FVPED_flag",
            "%2Fobs_params%2FVTPK",
            "%2Fobs_params%2FVTPK_flag",
            "%2Fobs_params%2Fdirection_spec",
            "%2Fobs_params%2Finten",
            "%2Fobs_params%2Flatitude",
            "%2Fobs_params%2Flongitude",
            "%2Fobs_params%2Fn_box",
            "%2Fobs_params%2Fn_posneg",
            "%2Fobs_params%2Fnv",
            "%2Fobs_params%2Fpartition_domain_spec",
            "%2Fobs_params%2Fresolution_spec",
            "%2Fobs_params%2Fsnr",
            "%2Fobs_params%2Fstorm_id",
            "%2Fobs_params%2Ftime",
            "%2Fobs_params%2Fwave_spec",
            "%2Fobs_params%2Fwavenumber_spec",
            "VAVH",
            "VPED",
            "VTPK",
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        bbox,
        max_date="2021-08-24T00:00:00Z",
        min_date="2021-06-08T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "dataset-wav-sar-l3-spc-rep-global-s1a_202105":
            if min_date is None:
                min_date = "2021-06-08T00:00:00Z"

            if max_date is None:
                max_date = "2021-08-24T00:00:00Z"

        if layer == "dataset-wav-sar-l3-spc-rep-global-s1b_202105":
            if min_date is None:
                min_date = "2021-06-08T00:00:00Z"

            if max_date is None:
                max_date = "2021-08-24T00:00:00Z"

        super().__init__(
            layer=layer,
            bbox=bbox,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
