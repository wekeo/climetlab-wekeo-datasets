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


class satellite_lake_water_level(Main):
    name = "EO:ECMWF:DAT:SATELLITE_LAKE_WATER_LEVEL"
    dataset = "EO:ECMWF:DAT:SATELLITE_LAKE_WATER_LEVEL"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "lake",
    ]

    @normalize(
        "lake",
        [
            "amadjuak",
            "argentino",
            "athabasca",
            "ayakkum",
            "aylmer",
            "baikal",
            "baker",
            "balbina",
            "balkhash",
            "beysehir",
            "bosten",
            "bratskoye",
            "cahora_bassa",
            "caribou",
            "caspian",
            "cedar",
            "chardarya",
            "dagze_co",
            "des_bois",
            "dogaicoring_q",
            "dubawnt",
            "erie",
            "fort_peck",
            "grande_trois",
            "greatslave",
            "guri",
            "har",
            "hongze",
            "hovsgol",
            "hulun",
            "huron",
            "issykkul",
            "kainji",
            "kapchagayskoye",
            "kara_bogaz_gol",
            "kariba",
            "kasba",
            "khanka",
            "kokonor",
            "krasnoyarskoye",
            "kremenchutska",
            "kuybyshevskoye",
            "kyoga",
            "ladoga",
            "lagoa_dos_patos",
            "langa_co",
            "lixiodain_co",
            "malawi",
            "manitoba",
            "michigan",
            "migriggyangzham",
            "mossoul",
            "mweru",
            "namco",
            "nasser",
            "ngangze",
            "ngoring_co",
            "nicaragua",
            "novosibirskoye",
            "nueltin",
            "onega",
            "ontario",
            "opinac",
            "peipus",
            "rukwa",
            "rybinskoye",
            "saint_jean",
            "sakakawea",
            "saksak",
            "saratovskoye",
            "sarykamish",
            "sasykkol",
            "soungari",
            "superior",
            "tana",
            "tanganika",
            "tangra_yumco",
            "tchad",
            "tchany",
            "tharthar",
            "todos_los_santos",
            "tsimlyanskoye",
            "turkana",
            "ulungur",
            "vanerm",
            "victoria",
            "volta",
            "williston",
            "winnipeg",
            "winnipegosis",
            "yellowstone",
            "zeyskoye",
            "zhari_namco",
            "ziling",
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
    @normalize(
        "variable",
        [
            "all",
        ],
    )
    def __init__(
        self,
        lake,
        format_,
        variable="all",
    ):
        super().__init__(
            lake=lake,
            format_=format_,
            variable=variable,
        )
