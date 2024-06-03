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


class sis_agroclimatic_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_AGROCLIMATIC_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_AGROCLIMATIC_INDICATORS"

    @normalize(
        "experiment",
        [
            "historical",
            "rcp2_6",
            "rcp4_5",
            "rcp6_0",
            "rcp8_5",
        ],
    )
    @normalize(
        "origin",
        [
            "era_interim_reanalysis",
            "gfdl_esm2m_model",
            "hadgem2_es_model",
            "ipsl_cm5a_lr_model",
            "miroc_esm_chem_model",
            "noresm1_m_model",
        ],
    )
    @normalize(
        "period",
        [
            "195101_198012",
            "198101_201012",
            "201101_204012",
            "204101_207012",
            "207101_209912",
        ],
        multiple=True,
    )
    @normalize(
        "temporal_aggregation",
        [
            "10_day",
            "annual",
            "season",
        ],
    )
    @normalize(
        "variable",
        [
            "biologically_effective_degree_days",
            "cold_spell_duration_index",
            "frost_days",
            "growing_season_length",
            "heavy_precipitation_days",
            "ice_days",
            "maximum_number_of_consecutive_dry_days",
            "maximum_number_of_consecutive_frost_days",
            "maximum_number_of_consecutive_summer_days",
            "maximum_number_of_consecutive_wet_days",
            "maximum_of_daily_maximum_temperature",
            "maximum_of_daily_minimum_temperature",
            "mean_of_daily_maximum_temperature",
            "mean_of_daily_mean_temperature",
            "mean_of_daily_minimum_temperature",
            "mean_of_diurnal_temperature_range",
            "minimum_of_daily_maximum_temperature",
            "minimum_of_daily_minimum_temperature",
            "precipitation_sum",
            "simple_daily_intensity_index",
            "summer_days",
            "tropical_nights",
            "very_heavy_precipitation_days",
            "warm_and_wet_days",
            "warm_spell_duration_index",
            "wet_days",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.0",
            "1.1",
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
        origin,
        period,
        temporal_aggregation,
        variable,
        version,
        format_=None,
        limit=None,
    ):
        super().__init__(
            experiment=experiment,
            origin=origin,
            period=period,
            temporal_aggregation=temporal_aggregation,
            variable=variable,
            version=version,
            format_=format_,
            limit=limit,
        )
