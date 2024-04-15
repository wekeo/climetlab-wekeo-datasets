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


class clms_global_lst_5km_v2_10daily_daily_cycle_netcdf(Main):
    name = "EO:CLMS:DAT:CLMS_GLOBAL_LST_5KM_V2_10DAILY-DAILY-CYCLE_NETCDF"
    dataset = "EO:CLMS:DAT:CLMS_GLOBAL_LST_5KM_V2_10DAILY-DAILY-CYCLE_NETCDF"

    @normalize(
        "productionStatus",
        [
            "ARCHIVED",
            "CANCELLED",
        ],
        multiple=True,
    )
    @normalize(
        "platform",
        [
            "GOES-16",
            "GOES-R",
            "HIMAWARI-8",
            "MSG-1",
            "MSG-4",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("bbox", "bounding-box(list)")
    @normalize(
        "productType",
        [
            "LST10",
        ],
    )
    @normalize(
        "acquisitionType",
        [
            "NOMINAL",
        ],
    )
    @normalize(
        "processingCenter",
        [
            "IPMA",
        ],
    )
    @normalize(
        "productGroupId",
        [
            "DC",
        ],
    )
    def __init__(
        self,
        productionStatus=None,
        platform=None,
        start=None,
        end=None,
        bbox=None,
        productType="LST10",
        acquisitionType="NOMINAL",
        processingCenter="IPMA",
        productGroupId="DC",
        limit=None,
    ):
        super().__init__(
            productionStatus=productionStatus,
            platform=platform,
            start=start,
            end=end,
            bbox=bbox,
            productType=productType,
            acquisitionType=acquisitionType,
            processingCenter=processingCenter,
            productGroupId=productGroupId,
            limit=limit,
        )
