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


class cams_global_greenhouse_gas_inversion(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_GREENHOUSE_GAS_INVERSION"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_GREENHOUSE_GAS_INVERSION"

    @normalize(
        "input_observations",
        [
            "first_guess",
            "satellite",
            "surface",
            "surface_satellite",
        ],
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
        "quantity",
        [
            "concentration",
            "loss_rate",
            "mean_column",
            "surface_flux",
        ],
    )
    @normalize(
        "time_aggregation",
        [
            "daily_mean",
            "instantaneous",
            "monthly_mean",
        ],
    )
    @normalize(
        "variable",
        [
            "carbon_dioxide",
            "methane",
            "nitrous_oxide",
        ],
    )
    @normalize(
        "version",
        [
            "latest",
            "v16r1",
            "v17r1",
            "v18r1",
            "v18r2",
            "v18r3",
            "v19r1",
            "v20r1",
            "v20r2",
            "v20r3",
            "v21r1",
            "v21r2",
            "v22r1",
            "v22r2",
            "v23r1",
            "v23r2",
            "v23r3",
        ],
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
            "2023",
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
        input_observations,
        month,
        quantity,
        time_aggregation,
        variable,
        version,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            input_observations=input_observations,
            month=month,
            quantity=quantity,
            time_aggregation=time_aggregation,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
