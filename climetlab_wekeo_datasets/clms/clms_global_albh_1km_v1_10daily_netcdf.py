#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_datasets.clms.main import Main


class clms_global_albh_1km_v1_10daily_netcdf(Main):
    name = "EO:CLMS:DAT:CLMS_GLOBAL_ALBH_1KM_V1_10DAILY_NETCDF"
    dataset = "EO:CLMS:DAT:CLMS_GLOBAL_ALBH_1KM_V1_10DAILY_NETCDF"

    @normalize(
        "acquisitionType",
        [
            "NOMINAL",
        ],
    )
    @normalize("bbox", "bounding-box(list)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "platform",
        [
            "PROBA-V",
            "SPOT-4",
            "SPOT-5",
        ],
        multiple=True,
    )
    @normalize(
        "processingCenter",
        [
            "VITO",
        ],
    )
    @normalize(
        "productType",
        [
            "ALBH",
        ],
    )
    @normalize(
        "productionStatus",
        [
            "ARCHIVED",
            "CANCELLED",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        acquisitionType=None,
        bbox=None,
        end=None,
        platform=None,
        processingCenter=None,
        productType=None,
        productionStatus=None,
        start=None,
        limit=None,
    ):
        super().__init__(
            acquisitionType=acquisitionType,
            bbox=bbox,
            end=end,
            platform=platform,
            processingCenter=processingCenter,
            productType=productType,
            productionStatus=productionStatus,
            start=start,
            limit=limit,
        )
