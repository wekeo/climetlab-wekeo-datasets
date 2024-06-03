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


class satellite_carbon_dioxide(Main):
    name = "EO:ECMWF:DAT:SATELLITE_CARBON_DIOXIDE"
    dataset = "EO:ECMWF:DAT:SATELLITE_CARBON_DIOXIDE"

    @normalize(
        "day",
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
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
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
        "processing_level",
        [
            "level_2",
            "level_3",
        ],
        multiple=True,
    )
    @normalize(
        "sensor_and_algorithm",
        [
            "airs_nlis",
            "iasi_metop_a_nlis",
            "iasi_metop_b_nlis",
            "iasi_metop_c_nlis",
            "merged_emma",
            "merged_obs4mips",
            "sciamachy_besd",
            "sciamachy_wfmd",
            "tanso2_fts_srfp",
            "tanso_fts_ocfp",
            "tanso_fts_srfp",
        ],
    )
    @normalize(
        "variable",
        [
            "co2",
            "xco2",
        ],
    )
    @normalize(
        "version",
        [
            "02.01.02",
            "02.01.02",
            "10.1",
            "10.1",
            "2.0.0",
            "2.0.0",
            "2.3.8",
            "2.3.8",
            "3",
            "3.0",
            "3.0",
            "3.1",
            "4.0",
            "4.1",
            "4.2",
            "4.3",
            "4.4",
            "4.5",
            "4.5",
            "7.1",
            "7.2",
            "7.3",
            "7.3",
            "8.0",
            "9.1",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        day,
        month,
        processing_level,
        sensor_and_algorithm,
        variable,
        version,
        year,
        format_=None,
        limit=None,
    ):
        super().__init__(
            day=day,
            month=month,
            processing_level=processing_level,
            sensor_and_algorithm=sensor_and_algorithm,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
