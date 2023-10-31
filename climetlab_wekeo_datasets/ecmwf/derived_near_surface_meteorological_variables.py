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


class derived_near_surface_meteorological_variables(Main):
    name = "EO:ECMWF:DAT:DERIVED_NEAR_SURFACE_METEOROLOGICAL_VARIABLES"
    dataset = "EO:ECMWF:DAT:DERIVED_NEAR_SURFACE_METEOROLOGICAL_VARIABLES"

    choices = [
        "reference_dataset",
        "format_",
    ]

    string_selects = [
        "month",
        "variable",
        "version",
        "year",
    ]

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
        "variable",
        [
            "grid_point_altitude",
            "near_surface_air_temperature",
            "near_surface_specific_humidity",
            "near_surface_wind_speed",
            "rainfall_flux",
            "snowfall_flux",
            "surface_air_pressure",
            "surface_downwelling_longwave_radiation",
            "surface_downwelling_shortwave_radiation",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1.1",
            "2.0",
            "2.1",
            "deprecated (1.0)",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
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
            "2019",
        ],
        multiple=True,
    )
    @normalize(
        "reference_dataset",
        [
            "cru",
            "cru_and_gpcc",
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
        month,
        variable,
        version,
        year,
        reference_dataset=None,
        format_=None,
    ):
        super().__init__(
            month=month,
            variable=variable,
            version=version,
            year=year,
            reference_dataset=reference_dataset,
            format_=format_,
        )
