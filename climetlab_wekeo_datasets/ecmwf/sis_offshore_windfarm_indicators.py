#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.ecmwf.main import Main


class sis_offshore_windfarm_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_OFFSHORE_WINDFARM_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_OFFSHORE_WINDFARM_INDICATORS"

    choices = [
        "variable",
        "sea",
        "time_aggregation",
        "format_",
    ]

    string_selects = [
        "epoch",
        "stat",
    ]

    @normalize(
        "epoch",
        [
            "historical",
            "rcp4_5_end_century",
            "rcp4_5_mid_century",
            "rcp8_5_end_century",
            "rcp8_5_mid_century",
        ],
        multiple=True,
    )
    @normalize(
        "stat",
        [
            "10th_percentile",
            "50th_percentile",
            "90th_percentile",
            "mean",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "energy_based_availability",
            "generated_energy_with_downtime",
            "generated_energy_without_downtime",
            "jack_up_barge_duration",
            "time_based_availability",
        ],
    )
    @normalize(
        "sea",
        [
            "baltic_sea",
            "irish_sea",
            "north_sea_channel",
            "north_sea_denmark",
            "north_sea_germany",
            "northern_north_sea",
            "southern_north_sea",
        ],
    )
    @normalize(
        "time_aggregation",
        [
            "annual",
            "campaign",
            "monthly",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        epoch,
        stat,
        variable,
        sea,
        time_aggregation,
        format_,
    ):
        super().__init__(
            epoch=epoch,
            stat=stat,
            variable=variable,
            sea=sea,
            time_aggregation=time_aggregation,
            format_=format_,
        )
