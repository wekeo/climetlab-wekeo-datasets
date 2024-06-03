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


class cams_global_radiative_forcings(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_RADIATIVE_FORCINGS"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_RADIATIVE_FORCINGS"

    @normalize(
        "band",
        [
            "long_wave",
            "net",
            "short_wave",
        ],
        multiple=True,
    )
    @normalize(
        "forcing_type",
        [
            "effective",
            "instantaneous",
            "stratospherically_adjusted",
        ],
    )
    @normalize(
        "level",
        [
            "surface",
            "top_of_atmosphere",
            "tropopause",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "sky_type",
        [
            "all_sky",
            "clear_sky",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "radiative_forcing_of_aerosol_cloud_interactions",
            "radiative_forcing_of_aerosol_radiation_interactions",
            "radiative_forcing_of_carbon_dioxide",
            "radiative_forcing_of_methane",
            "radiative_forcing_of_stratospheric_ozone",
            "radiative_forcing_of_tropospheric_ozone",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.5",
            "2",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
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
        band,
        forcing_type,
        level,
        month,
        sky_type,
        variable,
        version,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            band=band,
            forcing_type=forcing_type,
            level=level,
            month=month,
            sky_type=sky_type,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
