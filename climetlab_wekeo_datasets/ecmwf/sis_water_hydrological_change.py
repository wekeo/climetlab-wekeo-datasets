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


class sis_water_hydrological_change(Main):
    name = "EO:ECMWF:DAT:SIS_WATER_HYDROLOGICAL_CHANGE"
    dataset = "EO:ECMWF:DAT:SIS_WATER_HYDROLOGICAL_CHANGE"

    @normalize(
        "experiment",
        [
            "rcp_2_6",
            "rcp_8_5",
        ],
        multiple=True,
    )
    @normalize(
        "gcm_model",
        [
            "esm_chem",
            "gfdl_esm2m",
            "hadgem2_es",
            "ipsl_cm5a_lr",
            "noresm1_m",
        ],
        multiple=True,
    )
    @normalize(
        "hydrological_model",
        [
            "mesoscale_hydrological_model",
            "noah_mp",
            "pcr_globwb",
            "variable_infiltration_capacity",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "area_drought_extent",
            "change_in_the_annual_10_exceedance",
            "change_in_the_annual_90_exceedance",
            "change_in_the_annual_95_exceedence",
            "change_in_the_annual_mean",
            "change_in_the_daily_maximum",
            "change_in_the_monthly_mean",
            "change_in_the_seasonal_mean",
            "drought_duration",
        ],
    )
    @normalize(
        "time_aggregation",
        [
            "april",
            "august",
            "autumn",
            "december",
            "february",
            "january",
            "july",
            "june",
            "march",
            "may",
            "november",
            "october",
            "september",
            "spring",
            "summer",
            "winter",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "air_temperature",
            "groundwater_recharge",
            "potential_evapotranspiration",
            "precipitation",
            "river_discharge",
            "snow_water_equivalent",
            "volumetric_soil_moisture",
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
        gcm_model,
        hydrological_model,
        statistic,
        time_aggregation,
        variable,
        format_=None,
        limit=None,
    ):
        super().__init__(
            experiment=experiment,
            gcm_model=gcm_model,
            hydrological_model=hydrological_model,
            statistic=statistic,
            time_aggregation=time_aggregation,
            variable=variable,
            format_=format_,
            limit=limit,
        )
