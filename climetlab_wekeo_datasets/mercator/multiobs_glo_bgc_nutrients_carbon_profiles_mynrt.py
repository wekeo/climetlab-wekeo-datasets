#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.mercator.main import Main

LAYERS = [
    "cmems_obs-mob_glo_bgc-nut-car_mynrt_irr_i_202303",  # noqa: E501 cmems_obs-mob_glo_bgc-nut-car_mynrt_irr_i_202303
]


class multiobs_glo_bgc_nutrients_carbon_profiles_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_BGC_NUTRIENTS_CARBON_PROFILES_MYNRT_015_009"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_BGC_NUTRIENTS_CARBON_PROFILES_MYNRT_015_009"

    @normalize("bbox", "bounding-box(list)")
    @normalize("layer", LAYERS)
    @normalize("max_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("min_date", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "CYCLE_NUMBER",
            "DATA_CENTRE",
            "DOXY_ADJUSTED",
            "DOXY_ADJUSTED_ERROR",
            "DOXY_ADJUSTED_QC",
            "JULD",
            "JULD_QC",
            "LATITUDE",
            "LONGITUDE",
            "NITRATE_CANYON",
            "NITRATE_CANYON_ERROR",
            "NITRATE_CANYON_QC",
            "PCO2_CONTENT",
            "PCO2_CONTENT_ERROR",
            "PCO2_CONTENT_QC",
            "PHOSPHATE_CANYON",
            "PHOSPHATE_CANYON_ERROR",
            "PHOSPHATE_CANYON_QC",
            "PH_CONTENT",
            "PH_CONTENT_ERROR",
            "PH_CONTENT_QC",
            "PI_NAME",
            "PLATFORM_NUMBER",
            "POSITION_QC",
            "PRES_ADJUSTED",
            "PRES_ADJUSTED_ERROR",
            "PRES_ADJUSTED_QC",
            "PSAL_ADJUSTED",
            "PSAL_ADJUSTED_ERROR",
            "PSAL_ADJUSTED_QC",
            "REFERENCE_DATE_TIME",
            "SILICATE_CANYON",
            "SILICATE_CANYON_ERROR",
            "SILICATE_CANYON_QC",
            "STATION_PARAMETERS",
            "TALK_CONTENT",
            "TALK_CONTENT_ERROR",
            "TALK_CONTENT_QC",
            "TCO2_CONTENT",
            "TCO2_CONTENT_ERROR",
            "TCO2_CONTENT_QC",
            "TEMP_ADJUSTED",
            "TEMP_ADJUSTED_ERROR",
            "TEMP_ADJUSTED_QC",
            "WMO_INST_TYPE",
        ],
        multiple=True,
    )
    def __init__(
        self,
        bbox,
        layer="cmems_obs-mob_glo_bgc-nut-car_mynrt_irr_i_202303",
        max_date="2023-10-03T00:00:00Z",
        min_date="2022-10-03T00:00:00Z",
        variables=None,
        limit=None,
    ):
        if layer == "cmems_obs-mob_glo_bgc-nut-car_mynrt_irr_i_202303":
            if min_date is None:
                min_date = "2022-10-03T00:00:00Z"

            if max_date is None:
                max_date = "2023-10-03T00:00:00Z"

        super().__init__(
            bbox=bbox,
            layer=layer,
            max_date=max_date,
            min_date=min_date,
            variables=variables,
            limit=limit,
        )
