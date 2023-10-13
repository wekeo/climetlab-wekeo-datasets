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


class cams_global_radiative_forcing_auxilliary_variables(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_RADIATIVE_FORCING_AUXILLIARY_VARIABLES"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_RADIATIVE_FORCING_AUXILLIARY_VARIABLES"

    choices = [
        "format_",
    ]

    string_selects = [
        "aerosol_type",
        "band",
        "level",
        "month",
        "sky_type",
        "variable",
        "version",
        "year",
    ]

    @normalize(
        "aerosol_type",
        [
            "anthropogenic",
            "marine",
            "mineral_dust",
            "natural_land",
            "total",
        ],
        multiple=True,
    )
    @normalize(
        "band",
        [
            "short_wave",
        ],
        multiple=True,
    )
    @normalize(
        "level",
        [
            "surface",
            "top_of_atmosphere",
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
            "clear_sky",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "aerosol_absorption_optical_depth_550nm",
            "aerosol_optical_depth_550nm",
            "aerosol_radiation_effect",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.5",
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
        aerosol_type,
        band,
        level,
        month,
        sky_type,
        variable,
        version,
        year,
        format_,
    ):
        super().__init__(
            aerosol_type=aerosol_type,
            band=band,
            level=level,
            month=month,
            sky_type=sky_type,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
        )
