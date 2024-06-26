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


class sis_extreme_indices_cmip6(Main):
    name = "EO:ECMWF:DAT:SIS_EXTREME_INDICES_CMIP6"
    dataset = "EO:ECMWF:DAT:SIS_EXTREME_INDICES_CMIP6"

    @normalize(
        "ensemble_member",
        [
            "r10i1p1f1",
            "r10i1p2f1",
            "r11i1p1f1",
            "r11i1p2f1",
            "r12i1p1f1",
            "r12i1p2f1",
            "r13i1p1f1",
            "r13i1p2f1",
            "r14i1p1f1",
            "r14i1p2f1",
            "r15i1p1f1",
            "r15i1p2f1",
            "r16i1p1f1",
            "r16i1p2f1",
            "r17i1p1f1",
            "r17i1p2f1",
            "r18i1p1f1",
            "r18i1p2f1",
            "r19i1p1f1",
            "r19i1p2f1",
            "r1i1p1f1",
            "r1i1p1f2",
            "r1i1p1f3",
            "r1i1p2f1",
            "r20i1p1f1",
            "r20i1p2f1",
            "r21i1p1f1",
            "r21i1p2f1",
            "r22i1p1f1",
            "r22i1p2f1",
            "r23i1p1f1",
            "r23i1p2f1",
            "r24i1p1f1",
            "r24i1p2f1",
            "r25i1p1f1",
            "r25i1p2f1",
            "r26i1p1f1",
            "r27i1p1f1",
            "r28i1p1f1",
            "r29i1p1f1",
            "r2i1p1f1",
            "r2i1p2f1",
            "r30i1p1f1",
            "r31i1p1f1",
            "r32i1p1f1",
            "r33i1p1f1",
            "r34i1p1f1",
            "r35i1p1f1",
            "r36i1p1f1",
            "r37i1p1f1",
            "r38i1p1f1",
            "r39i1p1f1",
            "r3i1p1f1",
            "r3i1p2f1",
            "r40i1p1f1",
            "r41i1p1f1",
            "r42i1p1f1",
            "r43i1p1f1",
            "r44i1p1f1",
            "r45i1p1f1",
            "r46i1p1f1",
            "r47i1p1f1",
            "r48i1p1f1",
            "r49i1p1f1",
            "r4i1p1f1",
            "r4i1p2f1",
            "r50i1p1f1",
            "r5i1p1f1",
            "r5i1p2f1",
            "r6i1p1f1",
            "r6i1p2f1",
            "r7i1p1f1",
            "r7i1p2f1",
            "r8i1p1f1",
            "r8i1p2f1",
            "r9i1p1f1",
            "r9i1p2f1",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "historical",
            "ssp1_2_6",
            "ssp2_4_5",
            "ssp3_7_0",
            "ssp5_8_5",
        ],
        multiple=True,
    )
    @normalize(
        "model",
        [
            "access_cm2",
            "access_esm1_5",
            "bcc_csm2_mr",
            "canesm5",
            "cnrm_cm6_1",
            "cnrm_cm6_1_hr",
            "cnrm_esm2_1",
            "ec_earth3",
            "ec_earth3_veg",
            "fgoals_g3",
            "gfdl_cm4",
            "gfdl_esm4",
            "hadgem3_gc31_ll",
            "hadgem3_gc31_mm",
            "inm_cm4_8",
            "inm_cm5_0",
            "kace_1_0_g",
            "kiost_esm",
            "miroc6",
            "miroc_es2l",
            "mpi_esm1_2_hr",
            "mpi_esm1_2_lr",
            "mri_esm2_0",
            "nesm3",
            "noresm2_lm",
            "noresm2_mm",
            "ukesm1_0_ll",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1849-2014",
            "184901-201412",
            "1850-2014",
            "1850-2016",
            "185001-201412",
            "185001-201612",
            "1951-2014",
            "195101-201412",
            "19510101-20101230",
            "19510101-20101231",
            "19510101-20141230",
            "19510101-20141231",
            "20110101-21001230",
            "20110101-21001231",
            "2015-2039",
            "2015-2100",
            "2015-2180",
            "2015-2300",
            "201501-203912",
            "201501-210012",
            "201501-218012",
            "201501-230012",
            "20150101-21001230",
            "20150101-21001231",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "base_independent",
            "base_period_1961_1990",
            "base_period_1981_2010",
            "bias_adjusted",
            "non_bias_adjusted",
        ],
        multiple=True,
    )
    @normalize(
        "temporal_aggregation",
        [
            "daily",
            "monthly",
            "yearly",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "cold_days",
            "cold_nights",
            "cold_spell_duration_index",
            "consecutive_dry_days",
            "consecutive_wet_days",
            "diurnal_temperature_range",
            "extremely_wet_day_precipitation",
            "frost_days",
            "growing_season_length",
            "heat_index",
            "heavy_precipitation_days",
            "humidex",
            "ice_days",
            "maximum_1_day_precipitation",
            "maximum_5_day_precipitation",
            "maximum_value_of_daily_maximum_temperature",
            "maximum_value_of_daily_minimum_temperature",
            "minimum_value_of_daily_maximum_temperature",
            "minimum_value_of_daily_minimum_temperature",
            "number_of_wet_days",
            "simple_daily_intensity_index",
            "summer_days",
            "total_wet_day_precipitation",
            "tropical_nights",
            "universal_thermal_climate_index",
            "very_heavy_precipitation_days",
            "very_wet_day_precipitation",
            "warm_days",
            "warm_nights",
            "warm_spell_duration_index",
            "wet_bulb_globe_temperature_index",
            "wet_bulb_temperature_index",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1_0",
            "2_0",
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
        ensemble_member,
        experiment,
        model,
        period,
        product_type,
        temporal_aggregation,
        variable,
        version,
        format_=None,
        limit=None,
    ):
        super().__init__(
            ensemble_member=ensemble_member,
            experiment=experiment,
            model=model,
            period=period,
            product_type=product_type,
            temporal_aggregation=temporal_aggregation,
            variable=variable,
            version=version,
            format_=format_,
            limit=limit,
        )
