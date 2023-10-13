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


class sis_tourism_climate_suitability_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_TOURISM_CLIMATE_SUITABILITY_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_TOURISM_CLIMATE_SUITABILITY_INDICATORS"

    choices = [
        "climate_index",
        "product_type",
        "experiment",
        "format_",
    ]

    string_selects = [
        "gcm",
        "period",
        "time_aggregation",
        "variable",
    ]

    @normalize(
        "gcm",
        [
            "cnrm_cm5",
            "ec_earth",
            "hadgem2_es",
            "ipsl_cm5a_mr",
            "mpi_esm_lr",
            "noresm1_m",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1970_1970",
            "1971_1975",
            "1976_1980",
            "1981_1985",
            "1986_1990",
            "1986_2005",
            "1991_1995",
            "1996_2000",
            "2001_2005",
            "2006_2010",
            "2011_2015",
            "2016_2020",
            "2021_2025",
            "2021_2040",
            "2026_2030",
            "2031_2035",
            "2036_2040",
            "2041_2045",
            "2041_2060",
            "2046_2050",
            "2051_2055",
            "2056_2060",
            "2061_2065",
            "2066_2070",
            "2071_2075",
            "2076_2080",
            "2081_2085",
            "2081_2100",
            "2086_2090",
            "2091_2095",
            "2096_2100",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "10_day",
            "autumn",
            "monthly",
            "spring",
            "summer",
            "winter",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "daily_index",
            "number_of_fair_days",
            "number_of_good_days",
            "number_of_unfavourable_days",
        ],
        multiple=True,
    )
    @normalize(
        "climate_index",
        [
            "climate_index_for_tourism",
            "holiday_climate_index",
        ],
    )
    @normalize(
        "product_type",
        [
            "multi_model_10th_percentile",
            "multi_model_90th_percentile",
            "multi_model_mean",
            "single_model",
        ],
    )
    @normalize(
        "experiment",
        [
            "historical",
            "rcp2_6",
            "rcp4_5",
            "rcp8_5",
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
        gcm,
        period,
        time_aggregation,
        variable,
        climate_index,
        product_type,
        experiment,
        format_,
    ):
        super().__init__(
            gcm=gcm,
            period=period,
            time_aggregation=time_aggregation,
            variable=variable,
            climate_index=climate_index,
            product_type=product_type,
            experiment=experiment,
            format_=format_,
        )
