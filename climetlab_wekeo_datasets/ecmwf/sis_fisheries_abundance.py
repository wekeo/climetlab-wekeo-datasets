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


class sis_fisheries_abundance(Main):
    name = "EO:ECMWF:DAT:SIS_FISHERIES_ABUNDANCE"
    dataset = "EO:ECMWF:DAT:SIS_FISHERIES_ABUNDANCE"

    @normalize(
        "experiment",
        [
            "rcp4_5",
            "rcp8_5",
        ],
    )
    @normalize(
        "maximum_sustainable_yield",
        [
            "0_6",
            "0_8",
            "1_1",
        ],
        multiple=True,
    )
    @normalize(
        "origin",
        [
            "ss_dbem_nemo",
            "ss_dbem_polcoms",
        ],
        multiple=True,
    )
    @normalize(
        "species",
        [
            "anchovy",
            "atlantic_halibut",
            "atlantic_horse_mackerel",
            "atlantic_salmon",
            "blue_whiting",
            "bluefin_tuna",
            "capelin",
            "cod",
            "common_cuttlefish",
            "dab",
            "dolphinfish",
            "european_seabass",
            "european_sprat",
            "european_squid",
            "gilt_head_seabream",
            "haddock",
            "hake",
            "herring",
            "mackerel",
            "meagre",
            "plaice",
            "red_mullet",
            "saithe",
            "sardine",
            "shrimp",
            "sole",
            "turbot",
            "veined_squid",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "species_abundance",
            "species_catch",
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
        experiment,
        maximum_sustainable_yield,
        origin,
        species,
        variable,
        format_=None,
        limit=None,
    ):
        super().__init__(
            experiment=experiment,
            maximum_sustainable_yield=maximum_sustainable_yield,
            origin=origin,
            species=species,
            variable=variable,
            format_=format_,
            limit=limit,
        )
