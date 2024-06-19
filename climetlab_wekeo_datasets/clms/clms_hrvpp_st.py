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


class clms_hrvpp_st(Main):
    name = "EO:EEA:DAT:CLMS_HRVPP_ST"
    dataset = "EO:EEA:DAT:CLMS_HRVPP_ST"

    @normalize("bbox", "bounding-box(list)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "platformSerialIdentifier",
        [
            "S2A, S2B",
        ],
    )
    @normalize("processingDate", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    @normalize(
        "productType",
        [
            "PPI",
            "QFLAG",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%S.%fZ)")
    def __init__(
        self,
        bbox=None,
        end=None,
        platformSerialIdentifier=None,
        processingDate=None,
        productType=None,
        start=None,
        limit=None,
    ):
        super().__init__(
            bbox=bbox,
            end=end,
            platformSerialIdentifier=platformSerialIdentifier,
            processingDate=processingDate,
            productType=productType,
            start=start,
            limit=limit,
        )
