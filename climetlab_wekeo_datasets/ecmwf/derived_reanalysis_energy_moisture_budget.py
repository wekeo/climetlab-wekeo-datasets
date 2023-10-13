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


class derived_reanalysis_energy_moisture_budget(Main):
    name = "EO:ECMWF:DAT:DERIVED_REANALYSIS_ENERGY_MOISTURE_BUDGET"
    dataset = "EO:ECMWF:DAT:DERIVED_REANALYSIS_ENERGY_MOISTURE_BUDGET"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "month",
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
            "2020",
            "2021",
            "2022",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "divergence_of_vertical_integral_of_latent_heat_flux",
            "divergence_of_vertical_integral_of_total_energy_flux",
            "divergence_of_vertical_integral_of_water_vapour_flux",
            "tendency_of_vertical_integral_of_latent_heat",
            "tendency_of_vertical_integral_of_total_energy",
            "tendency_of_vertical_integral_of_water_vapour",
            "vertical_integral_of_eastward_latent_heat_flux",
            "vertical_integral_of_eastward_total_energy_flux",
            "vertical_integral_of_eastward_water_vapour_flux",
            "vertical_integral_of_northward_latent_heat_flux",
            "vertical_integral_of_northward_total_energy_flux",
            "vertical_integral_of_northward_water_vapour_flux",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        month,
        year,
        variable,
        format_,
        area=None,
    ):
        super().__init__(
            month=month,
            year=year,
            variable=variable,
            format_=format_,
            area=area,
        )
