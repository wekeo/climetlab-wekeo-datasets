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


class sis_agroproductivity_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_AGROPRODUCTIVITY_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_AGROPRODUCTIVITY_INDICATORS"

    @normalize(
        "crop_type",
        [
            "maize",
            "soybean",
            "spring_wheat",
            "wet_rice",
            "winter_wheat",
        ],
        multiple=True,
    )
    @normalize(
        "day",
        [
            "01",
            "10",
            "11",
            "20",
            "21",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "growing_season",
        [
            "1st_season_per_campaign",
            "2nd_season_per_campaign",
        ],
        multiple=True,
    )
    @normalize(
        "harvest_year",
        [
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
            "2024",
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
        "product_family",
        [
            "crop_productivity_indicators",
            "evapotranspiration_indicators",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "actual_evaporation",
            "crop_development_stage",
            "potential_evaporation",
            "total_above_ground_production",
            "total_weight_storage_organs",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "2024",
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
        crop_type,
        day,
        growing_season,
        harvest_year,
        month,
        product_family,
        variable,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            crop_type=crop_type,
            day=day,
            growing_season=growing_season,
            harvest_year=harvest_year,
            month=month,
            product_family=product_family,
            variable=variable,
            year=year,
            format_=format_,
            limit=limit,
        )
