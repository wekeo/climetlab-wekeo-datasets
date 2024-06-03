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


class sis_soil_erosion(Main):
    name = "EO:ECMWF:DAT:SIS_SOIL_EROSION"
    dataset = "EO:ECMWF:DAT:SIS_SOIL_EROSION"

    @normalize(
        "experiment",
        [
            "all_rcps",
            "rcp_2_6",
            "rcp_4_5",
            "rcp_8_5",
        ],
        multiple=True,
    )
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
        "horizontal_aggregation",
        [
            "native_resolution",
            "regridded",
        ],
        multiple=True,
    )
    @normalize(
        "multimodel_statistic",
        [
            "mean",
            "standard_deviation",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1981-2010",
            "2021-2050",
            "2051-2080",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "e_obs",
            "era5",
            "era5_land",
            "euro_cordex",
        ],
        multiple=True,
    )
    @normalize(
        "rcm",
        [
            "cclm4_8_17",
            "csc_remo2009",
            "hirham5",
            "racmo22e",
            "rca4",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "maximum_1_day_precipitation",
            "maximum_5_day_precipitation",
            "number_of_days_with_lwe_greater_than_1_mm",
            "number_of_days_with_lwe_greater_than_20_mm",
            "r_factor",
            "soil_loss",
            "spell_length_of_days_with_lwe_greater_than_1_mm",
            "total_precipitation",
        ],
        multiple=True,
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
        experiment,
        gcm,
        horizontal_aggregation,
        multimodel_statistic,
        period,
        product_type,
        rcm,
        variable,
        format_=None,
        limit=None,
    ):
        super().__init__(
            experiment=experiment,
            gcm=gcm,
            horizontal_aggregation=horizontal_aggregation,
            multimodel_statistic=multimodel_statistic,
            period=period,
            product_type=product_type,
            rcm=rcm,
            variable=variable,
            format_=format_,
            limit=limit,
        )
