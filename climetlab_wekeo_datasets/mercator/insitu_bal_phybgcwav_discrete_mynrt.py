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
    "cmems_obs-ins_bal_phybgcwav_mynrt_na_irr_202211",  # noqa: E501 cmems_obs-ins_bal_phybgcwav_mynrt_na_irr_202211
]


class insitu_bal_phybgcwav_discrete_mynrt(Main):
    name = "EO:MO:DAT:INSITU_BAL_PHYBGCWAV_DISCRETE_MYNRT_013_032"
    dataset = "EO:MO:DAT:INSITU_BAL_PHYBGCWAV_DISCRETE_MYNRT_013_032"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "CDOM",
            "CDOM_QC",
            "DEPH",
            "DEPH_QC",
            "DOX1",
            "DOX1_QC",
            "FLU2",
            "FLU2_QC",
            "LATITUDE",
            "LONGITUDE",
            "PHYC",
            "PHYC_QC",
            "POSITION_QC",
            "PSAL",
            "PSAL_QC",
            "TEMP",
            "TEMP_QC",
            "TIME",
            "TIME_QC",
            "TUR4",
            "TUR4_QC",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer="cmems_obs-ins_bal_phybgcwav_mynrt_na_irr_202211",
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-ins_bal_phybgcwav_mynrt_na_irr_202211":
            if start is None:
                start = "1841-03-21T00:00:00Z"

            if end is None:
                end = "2023-06-27T17:10:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
