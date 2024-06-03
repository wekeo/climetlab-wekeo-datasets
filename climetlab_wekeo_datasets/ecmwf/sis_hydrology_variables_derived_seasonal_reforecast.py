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


class sis_hydrology_variables_derived_seasonal_reforecast(Main):
    name = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_SEASONAL_REFORECAST"
    dataset = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_SEASONAL_REFORECAST"

    @normalize(
        "hydrological_model",
        [
            "e_hypecatch_m00",
            "lisflood_efas",
            "vic_wur",
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
        "variable",
        [
            "brier_skill_score_above_normal_conditions",
            "brier_skill_score_below_normal_conditions",
            "continuous_ranked_probability_skill_score",
            "fair_ranked_probability_skill_score",
            "reference_river_discharge_lower_tercile",
            "reference_river_discharge_upper_tercile",
            "river_discharge",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1",
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
        hydrological_model,
        month,
        variable,
        year,
        version="1",
        format_=None,
        limit=None,
    ):
        super().__init__(
            hydrological_model=hydrological_model,
            month=month,
            variable=variable,
            year=year,
            version=version,
            format_=format_,
            limit=limit,
        )
