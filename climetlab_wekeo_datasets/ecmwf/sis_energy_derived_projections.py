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


class sis_energy_derived_projections(Main):
    name = "EO:ECMWF:DAT:SIS_ENERGY_DERIVED_PROJECTIONS"
    dataset = "EO:ECMWF:DAT:SIS_ENERGY_DERIVED_PROJECTIONS"

    @normalize(
        "energy_product_type",
        [
            "capacity_factor_ratio",
            "energy",
            "power",
        ],
        multiple=True,
    )
    @normalize(
        "ensemble_member",
        [
            "r12i1p1",
            "r1i1p1",
            "r3i1p1",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
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
        "rcm",
        [
            "aladin63",
            "cclm4_8_17",
            "hirham5",
            "racmo22e",
            "rca4",
            "regcm4",
            "wrf381p",
        ],
    )
    @normalize(
        "spatial_aggregation",
        [
            "country_level",
            "maritime_country_level",
            "maritime_sub_country_level",
            "original_grid",
            "sub_country_level",
        ],
    )
    @normalize(
        "temporal_aggregation",
        [
            "3_hourly",
            "annual",
            "daily",
            "monthly",
            "seasonal",
        ],
    )
    @normalize(
        "variable",
        [
            "2m_air_temperature",
            "electricity_demand",
            "hydro_power_generation_reservoirs",
            "hydro_power_generation_rivers",
            "solar_photovoltaic_power_generation",
            "surface_downwelling_shortwave_radiation",
            "total_precipitation",
            "wind_power_generation_offshore",
            "wind_power_generation_onshore",
            "wind_speed_at_100m",
            "wind_speed_at_10m",
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
        energy_product_type,
        ensemble_member,
        experiment,
        gcm,
        rcm,
        spatial_aggregation,
        temporal_aggregation,
        variable,
        format_=None,
        limit=None,
    ):
        super().__init__(
            energy_product_type=energy_product_type,
            ensemble_member=ensemble_member,
            experiment=experiment,
            gcm=gcm,
            rcm=rcm,
            spatial_aggregation=spatial_aggregation,
            temporal_aggregation=temporal_aggregation,
            variable=variable,
            format_=format_,
            limit=limit,
        )
