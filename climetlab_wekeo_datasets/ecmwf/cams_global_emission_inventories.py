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


class cams_global_emission_inventories(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_EMISSION_INVENTORIES"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_EMISSION_INVENTORIES"

    @normalize(
        "source",
        [
            "anthropogenic",
            "aviation",
            "biogenic",
            "oceanic",
            "shipping",
            "soil",
            "termites",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "acetaldehyde",
            "acetic_acid",
            "acetone",
            "acetylene",
            "acids",
            "alcohols",
            "alpha_pinene",
            "ammonia",
            "ash",
            "benzene",
            "beta_pinene",
            "black_carbon",
            "bromoform",
            "butanes",
            "butanes_and_higher_alkanes",
            "butenes_and_higher_alkenes",
            "carbon_dioxide",
            "carbon_dioxide_excl_short_cycle",
            "carbon_monoxide",
            "chlorinated_hydrocarbons",
            "dibromomethane",
            "dimethyl_sulphide",
            "elemental_carbon",
            "esters",
            "ethane",
            "ethanol",
            "ethene",
            "ethers",
            "formaldehyde",
            "formic_acid",
            "hexanes",
            "hydrogen_cyanide",
            "iodomethane",
            "isoprene",
            "ketones",
            "methane",
            "methanol",
            "methyl_bromide",
            "methyl_chloride",
            "methyl_iodide",
            "monoterpenes",
            "nitrogen_oxides",
            "non_methane_vocs",
            "organic_carbon",
            "other_aldehydes",
            "other_alkenes_alkynes",
            "other_aromatics",
            "other_ketones",
            "other_monoterpenes",
            "other_vocs",
            "pentanes",
            "pinene",
            "propane",
            "propene",
            "sesquiterpenes",
            "sulphate",
            "sulphur_dioxide",
            "sulphur_oxides",
            "toluene",
            "trimethylbenzenes",
            "vocs_all",
            "xylenes",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "latest",
            "v1.1",
            "v1.2",
            "v2.1",
            "v2.2",
            "v3.0",
            "v3.1",
            "v4.2",
        ],
        multiple=True,
    )
    @normalize(
        "year",
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
    def __init__(self, source, variable, version, year, format_=None, limit=None):
        super().__init__(
            source=source,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
            limit=limit,
        )
