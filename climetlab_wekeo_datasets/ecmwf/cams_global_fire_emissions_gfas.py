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


class cams_global_fire_emissions_gfas(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_FIRE_EMISSIONS_GFAS"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_FIRE_EMISSIONS_GFAS"

    @normalize(
        "variable",
        [
            "altitude_of_plume_bottom",
            "altitude_of_plume_top",
            "injection_height",
            "mean_altitude_of_maximum_injection",
            "wildfire_combustion_rate",
            "wildfire_flux_of_acetaldehyde",
            "wildfire_flux_of_acetone",
            "wildfire_flux_of_ammonia",
            "wildfire_flux_of_benzene",
            "wildfire_flux_of_black_carbon",
            "wildfire_flux_of_butanes",
            "wildfire_flux_of_butenes",
            "wildfire_flux_of_carbon_dioxide",
            "wildfire_flux_of_carbon_monoxide",
            "wildfire_flux_of_dimethyl_sulfide",
            "wildfire_flux_of_ethane",
            "wildfire_flux_of_ethanol",
            "wildfire_flux_of_ethene",
            "wildfire_flux_of_formaldehyde",
            "wildfire_flux_of_heptane",
            "wildfire_flux_of_hexanes",
            "wildfire_flux_of_hexene",
            "wildfire_flux_of_higher_alkanes",
            "wildfire_flux_of_higher_alkenes",
            "wildfire_flux_of_hydrogen",
            "wildfire_flux_of_isoprene",
            "wildfire_flux_of_methane",
            "wildfire_flux_of_methanol",
            "wildfire_flux_of_nitrogen_oxides",
            "wildfire_flux_of_nitrous_oxide",
            "wildfire_flux_of_non_methane_hydrocarbons",
            "wildfire_flux_of_octene",
            "wildfire_flux_of_organic_carbon",
            "wildfire_flux_of_particulate_matter_d_2_5_µm",
            "wildfire_flux_of_pentanes",
            "wildfire_flux_of_pentenes",
            "wildfire_flux_of_propane",
            "wildfire_flux_of_propene",
            "wildfire_flux_of_sulphur_dioxide",
            "wildfire_flux_of_terpenes",
            "wildfire_flux_of_toluene",
            "wildfire_flux_of_toluene_lump",
            "wildfire_flux_of_total_carbon_in_aerosols",
            "wildfire_flux_of_total_particulate_matter",
            "wildfire_flux_of_xylene",
            "wildfire_fraction_of_area_observed",
            "wildfire_overall_flux_of_burnt_carbon",
            "wildfire_radiative_power",
        ],
        multiple=True,
    )
    @normalize("dtend", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize("dtstart", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    def __init__(
        self,
        variable,
        dtend="2024-05-20",
        dtstart="2003-01-01",
        format_=None,
        limit=None,
    ):
        super().__init__(
            variable=variable,
            dtend=dtend,
            dtstart=dtstart,
            format_=format_,
            limit=limit,
        )
