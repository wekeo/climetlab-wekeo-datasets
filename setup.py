#!/usr/bin/env python
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_wekeo_datasets"  # noqa: E501

version = None
lines = read(f"{package_name}/version").split("\n")
if lines:
    version = lines[0]

assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description=("A dataset plugin for climetlab for the WEkEO dataset"),  # noqa: E501
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Germano Guerrini",
    author_email="germano.guerrini@exprivia.com",
    url="http://github.com/wekeo/climetlab-wekeo-datasets",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "climetlab>=0.10.0",
        "climetlab-wekeo-source",
    ],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            # End-users will use cml.load_dataset("wekeo-", ...)
            # see the tests/ folder for a example.
            # CLMS
            "wekeo-clms-clms-hrvpp-st=climetlab_wekeo_datasets.clms.clms_hrvpp_st:clms_hrvpp_st",  # noqa: E501
            "wekeo-clms-clms-global-albh-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_albh_1km_v1_10daily_netcdf:clms_global_albh_1km_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-aldh-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_aldh_1km_v1_10daily_netcdf:clms_global_aldh_1km_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-dmp-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_dmp_1km_v2_10daily_netcdf:clms_global_dmp_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-dmp-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_dmp_300m_v1_10daily_netcdf:clms_global_dmp_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fapar-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fapar_1km_v1_10daily_netcdf:clms_global_fapar_1km_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fapar-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fapar_1km_v2_10daily_netcdf:clms_global_fapar_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fapar-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fapar_300m_v1_10daily_netcdf:clms_global_fapar_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fcover-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fcover_1km_v1_10daily_netcdf:clms_global_fcover_1km_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fcover-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fcover_1km_v2_10daily_netcdf:clms_global_fcover_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-fcover-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_fcover_300m_v1_10daily_netcdf:clms_global_fcover_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-gdmp-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_gdmp_1km_v2_10daily_netcdf:clms_global_gdmp_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-gdmp-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_gdmp_300m_v1_10daily_netcdf:clms_global_gdmp_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-gpp-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_gpp_300m_v1_10daily_netcdf:clms_global_gpp_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lai-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_lai_1km_v1_10daily_netcdf:clms_global_lai_1km_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lai-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_lai_1km_v2_10daily_netcdf:clms_global_lai_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lai-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_lai_300m_v1_10daily_netcdf:clms_global_lai_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v1-10daily-daily-cycle-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v1_10daily_daily_cycle_netcdf:clms_global_lst_5km_v1_10daily_daily_cycle_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v1-10daily-tci-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v1_10daily_tci_netcdf:clms_global_lst_5km_v1_10daily_tci_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v1-hourly-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v1_hourly_netcdf:clms_global_lst_5km_v1_hourly_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v2-10daily-daily-cycle-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v2_10daily_daily_cycle_netcdf:clms_global_lst_5km_v2_10daily_daily_cycle_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v2-10daily-tci-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v2_10daily_tci_netcdf:clms_global_lst_5km_v2_10daily_tci_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-lst-5km-v2-hourly-netcdf=climetlab_wekeo_datasets.clms.clms_global_lst_5km_v2_hourly_netcdf:clms_global_lst_5km_v2_hourly_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-ndvi-1km-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_ndvi_1km_v2_10daily_netcdf:clms_global_ndvi_1km_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-ndvi-1km-v3-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_ndvi_1km_v3_10daily_netcdf:clms_global_ndvi_1km_v3_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-ndvi-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_ndvi_300m_v1_10daily_netcdf:clms_global_ndvi_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-ndvi-300m-v2-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_ndvi_300m_v2_10daily_netcdf:clms_global_ndvi_300m_v2_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-npp-300m-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_npp_300m_v1_10daily_netcdf:clms_global_npp_300m_v1_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-ssm-1km-v1-daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_ssm_1km_v1_daily_netcdf:clms_global_ssm_1km_v1_daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-swi-12-5km-v3-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_swi_12_5km_v3_10daily_netcdf:clms_global_swi_12_5km_v3_10daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-swi-12-5km-v3-daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_swi_12_5km_v3_daily_netcdf:clms_global_swi_12_5km_v3_daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-swi-1km-v1-daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_swi_1km_v1_daily_netcdf:clms_global_swi_1km_v1_daily_netcdf",  # noqa: E501
            "wekeo-clms-clms-global-tocr-1km-v1-10daily-netcdf=climetlab_wekeo_datasets.clms.clms_global_tocr_1km_v1_10daily_netcdf:clms_global_tocr_1km_v1_10daily_netcdf",  # noqa: E501
            # ECMWF
            "wekeo-ecmwf-cams-europe-air-quality-forecasts=climetlab_wekeo_datasets.ecmwf.cams_europe_air_quality_forecasts:cams_europe_air_quality_forecasts",  # noqa: E501
            "wekeo-ecmwf-cams-europe-air-quality-reanalyses=climetlab_wekeo_datasets.ecmwf.cams_europe_air_quality_reanalyses:cams_europe_air_quality_reanalyses",  # noqa: E501
            "wekeo-ecmwf-cams-global-atmospheric-composition-forecasts=climetlab_wekeo_datasets.ecmwf.cams_global_atmospheric_composition_forecasts:cams_global_atmospheric_composition_forecasts",  # noqa: E501
            "wekeo-ecmwf-cams-global-emission-inventories=climetlab_wekeo_datasets.ecmwf.cams_global_emission_inventories:cams_global_emission_inventories",  # noqa: E501
            "wekeo-ecmwf-cams-global-fire-emissions-gfas=climetlab_wekeo_datasets.ecmwf.cams_global_fire_emissions_gfas:cams_global_fire_emissions_gfas",  # noqa: E501
            "wekeo-ecmwf-cams-global-ghg-reanalysis-egg4-monthly=climetlab_wekeo_datasets.ecmwf.cams_global_ghg_reanalysis_egg4_monthly:cams_global_ghg_reanalysis_egg4_monthly",  # noqa: E501
            "wekeo-ecmwf-cams-global-ghg-reanalysis-egg4=climetlab_wekeo_datasets.ecmwf.cams_global_ghg_reanalysis_egg4:cams_global_ghg_reanalysis_egg4",  # noqa: E501
            "wekeo-ecmwf-cams-global-greenhouse-gas-inversion=climetlab_wekeo_datasets.ecmwf.cams_global_greenhouse_gas_inversion:cams_global_greenhouse_gas_inversion",  # noqa: E501
            "wekeo-ecmwf-cams-global-radiative-forcing-auxilliary-variables=climetlab_wekeo_datasets.ecmwf.cams_global_radiative_forcing_auxilliary_variables:cams_global_radiative_forcing_auxilliary_variables",  # noqa: E501
            "wekeo-ecmwf-cams-global-radiative-forcings=climetlab_wekeo_datasets.ecmwf.cams_global_radiative_forcings:cams_global_radiative_forcings",  # noqa: E501
            "wekeo-ecmwf-cams-global-reanalysis-eac4-monthly=climetlab_wekeo_datasets.ecmwf.cams_global_reanalysis_eac4_monthly:cams_global_reanalysis_eac4_monthly",  # noqa: E501
            "wekeo-ecmwf-cams-global-reanalysis-eac4=climetlab_wekeo_datasets.ecmwf.cams_global_reanalysis_eac4:cams_global_reanalysis_eac4",  # noqa: E501
            "wekeo-ecmwf-cams-solar-radiation-timeseries=climetlab_wekeo_datasets.ecmwf.cams_solar_radiation_timeseries:cams_solar_radiation_timeseries",  # noqa: E501
            "wekeo-ecmwf-cems-fire-historical-v1=climetlab_wekeo_datasets.ecmwf.cems_fire_historical_v1:cems_fire_historical_v1",  # noqa: E501
            "wekeo-ecmwf-derived-near-surface-meteorological-variables=climetlab_wekeo_datasets.ecmwf.derived_near_surface_meteorological_variables:derived_near_surface_meteorological_variables",  # noqa: E501
            "wekeo-ecmwf-derived-reanalysis-energy-moisture-budget=climetlab_wekeo_datasets.ecmwf.derived_reanalysis_energy_moisture_budget:derived_reanalysis_energy_moisture_budget",  # noqa: E501
            "wekeo-ecmwf-derived-utci-historical=climetlab_wekeo_datasets.ecmwf.derived_utci_historical:derived_utci_historical",  # noqa: E501
            "wekeo-ecmwf-ecv-for-climate-change=climetlab_wekeo_datasets.ecmwf.ecv_for_climate_change:ecv_for_climate_change",  # noqa: E501
            "wekeo-ecmwf-efas-forecast=climetlab_wekeo_datasets.ecmwf.efas_forecast:efas_forecast",  # noqa: E501
            "wekeo-ecmwf-efas-historical=climetlab_wekeo_datasets.ecmwf.efas_historical:efas_historical",  # noqa: E501
            "wekeo-ecmwf-efas-reforecast=climetlab_wekeo_datasets.ecmwf.efas_reforecast:efas_reforecast",  # noqa: E501
            "wekeo-ecmwf-efas-seasonal-reforecast=climetlab_wekeo_datasets.ecmwf.efas_seasonal_reforecast:efas_seasonal_reforecast",  # noqa: E501
            "wekeo-ecmwf-efas-seasonal=climetlab_wekeo_datasets.ecmwf.efas_seasonal:efas_seasonal",  # noqa: E501
            "wekeo-ecmwf-insitu-glaciers-elevation-mass=climetlab_wekeo_datasets.ecmwf.insitu_glaciers_elevation_mass:insitu_glaciers_elevation_mass",  # noqa: E501
            "wekeo-ecmwf-insitu-glaciers-extent=climetlab_wekeo_datasets.ecmwf.insitu_glaciers_extent:insitu_glaciers_extent",  # noqa: E501
            "wekeo-ecmwf-insitu-gridded-observations-alpine-precipitation=climetlab_wekeo_datasets.ecmwf.insitu_gridded_observations_alpine_precipitation:insitu_gridded_observations_alpine_precipitation",  # noqa: E501
            "wekeo-ecmwf-insitu-gridded-observations-europe=climetlab_wekeo_datasets.ecmwf.insitu_gridded_observations_europe:insitu_gridded_observations_europe",  # noqa: E501
            "wekeo-ecmwf-insitu-gridded-observations-global-and-regional=climetlab_wekeo_datasets.ecmwf.insitu_gridded_observations_global_and_regional:insitu_gridded_observations_global_and_regional",  # noqa: E501
            "wekeo-ecmwf-insitu-gridded-observations-nordic=climetlab_wekeo_datasets.ecmwf.insitu_gridded_observations_nordic:insitu_gridded_observations_nordic",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-gnss=climetlab_wekeo_datasets.ecmwf.insitu_observations_gnss:insitu_observations_gnss",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-gruan-reference-network=climetlab_wekeo_datasets.ecmwf.insitu_observations_gruan_reference_network:insitu_observations_gruan_reference_network",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-igra-baseline-network=climetlab_wekeo_datasets.ecmwf.insitu_observations_igra_baseline_network:insitu_observations_igra_baseline_network",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-surface-land=climetlab_wekeo_datasets.ecmwf.insitu_observations_surface_land:insitu_observations_surface_land",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-surface-marine=climetlab_wekeo_datasets.ecmwf.insitu_observations_surface_marine:insitu_observations_surface_marine",  # noqa: E501
            "wekeo-ecmwf-insitu-observations-woudc-ozone-total-column-and-profiles=climetlab_wekeo_datasets.ecmwf.insitu_observations_woudc_ozone_total_column_and_profiles:insitu_observations_woudc_ozone_total_column_and_profiles",  # noqa: E501
            "wekeo-ecmwf-projections-cmip5-daily-pressure-levels=climetlab_wekeo_datasets.ecmwf.projections_cmip5_daily_pressure_levels:projections_cmip5_daily_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-projections-cmip5-daily-single-levels=climetlab_wekeo_datasets.ecmwf.projections_cmip5_daily_single_levels:projections_cmip5_daily_single_levels",  # noqa: E501
            "wekeo-ecmwf-projections-cmip5-monthly-pressure-levels=climetlab_wekeo_datasets.ecmwf.projections_cmip5_monthly_pressure_levels:projections_cmip5_monthly_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-projections-cmip5-monthly-single-levels=climetlab_wekeo_datasets.ecmwf.projections_cmip5_monthly_single_levels:projections_cmip5_monthly_single_levels",  # noqa: E501
            "wekeo-ecmwf-projections-cmip6=climetlab_wekeo_datasets.ecmwf.projections_cmip6:projections_cmip6",  # noqa: E501
            "wekeo-ecmwf-projections-cordex-domains-single-levels=climetlab_wekeo_datasets.ecmwf.projections_cordex_domains_single_levels:projections_cordex_domains_single_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-carra-height-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_carra_height_levels:reanalysis_carra_height_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-carra-model-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_carra_model_levels:reanalysis_carra_model_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-carra-pressure-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_carra_pressure_levels:reanalysis_carra_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-carra-single-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_carra_single_levels:reanalysis_carra_single_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-cerra-height-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_cerra_height_levels:reanalysis_cerra_height_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-cerra-land=climetlab_wekeo_datasets.ecmwf.reanalysis_cerra_land:reanalysis_cerra_land",  # noqa: E501
            "wekeo-ecmwf-reanalysis-cerra-model-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_cerra_model_levels:reanalysis_cerra_model_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-cerra-pressure-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_cerra_pressure_levels:reanalysis_cerra_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-cerra-single-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_cerra_single_levels:reanalysis_cerra_single_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-land-monthly-means=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_land_monthly_means:reanalysis_era5_land_monthly_means",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-land=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_land:reanalysis_era5_land",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_pressure_levels_monthly_means:reanalysis_era5_pressure_levels_monthly_means",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-pressure-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_pressure_levels:reanalysis_era5_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_single_levels_monthly_means:reanalysis_era5_single_levels_monthly_means",  # noqa: E501
            "wekeo-ecmwf-reanalysis-era5-single-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_era5_single_levels:reanalysis_era5_single_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-oras5=climetlab_wekeo_datasets.ecmwf.reanalysis_oras5:reanalysis_oras5",  # noqa: E501
            "wekeo-ecmwf-reanalysis-uerra-europe-height-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_uerra_europe_height_levels:reanalysis_uerra_europe_height_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-uerra-europe-pressure-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_uerra_europe_pressure_levels:reanalysis_uerra_europe_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-uerra-europe-single-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_uerra_europe_single_levels:reanalysis_uerra_europe_single_levels",  # noqa: E501
            "wekeo-ecmwf-reanalysis-uerra-europe-soil-levels=climetlab_wekeo_datasets.ecmwf.reanalysis_uerra_europe_soil_levels:reanalysis_uerra_europe_soil_levels",  # noqa: E501
            "wekeo-ecmwf-satellite-aerosol-properties=climetlab_wekeo_datasets.ecmwf.satellite_aerosol_properties:satellite_aerosol_properties",  # noqa: E501
            "wekeo-ecmwf-satellite-albedo=climetlab_wekeo_datasets.ecmwf.satellite_albedo:satellite_albedo",  # noqa: E501
            "wekeo-ecmwf-satellite-carbon-dioxide=climetlab_wekeo_datasets.ecmwf.satellite_carbon_dioxide:satellite_carbon_dioxide",  # noqa: E501
            "wekeo-ecmwf-satellite-cloud-properties=climetlab_wekeo_datasets.ecmwf.satellite_cloud_properties:satellite_cloud_properties",  # noqa: E501
            "wekeo-ecmwf-satellite-earth-radiation-budget=climetlab_wekeo_datasets.ecmwf.satellite_earth_radiation_budget:satellite_earth_radiation_budget",  # noqa: E501
            "wekeo-ecmwf-satellite-fire-burned-area=climetlab_wekeo_datasets.ecmwf.satellite_fire_burned_area:satellite_fire_burned_area",  # noqa: E501
            "wekeo-ecmwf-satellite-fire-radiative-power=climetlab_wekeo_datasets.ecmwf.satellite_fire_radiative_power:satellite_fire_radiative_power",  # noqa: E501
            "wekeo-ecmwf-satellite-greenland-ice-sheet-velocity=climetlab_wekeo_datasets.ecmwf.satellite_greenland_ice_sheet_velocity:satellite_greenland_ice_sheet_velocity",  # noqa: E501
            "wekeo-ecmwf-satellite-humidity-profiles=climetlab_wekeo_datasets.ecmwf.satellite_humidity_profiles:satellite_humidity_profiles",  # noqa: E501
            "wekeo-ecmwf-satellite-ice-sheet-elevation-change=climetlab_wekeo_datasets.ecmwf.satellite_ice_sheet_elevation_change:satellite_ice_sheet_elevation_change",  # noqa: E501
            "wekeo-ecmwf-satellite-ice-sheet-mass-balance=climetlab_wekeo_datasets.ecmwf.satellite_ice_sheet_mass_balance:satellite_ice_sheet_mass_balance",  # noqa: E501
            "wekeo-ecmwf-satellite-lai-fapar=climetlab_wekeo_datasets.ecmwf.satellite_lai_fapar:satellite_lai_fapar",  # noqa: E501
            "wekeo-ecmwf-satellite-lake-water-level=climetlab_wekeo_datasets.ecmwf.satellite_lake_water_level:satellite_lake_water_level",  # noqa: E501
            "wekeo-ecmwf-satellite-lake-water-temperature=climetlab_wekeo_datasets.ecmwf.satellite_lake_water_temperature:satellite_lake_water_temperature",  # noqa: E501
            "wekeo-ecmwf-satellite-land-cover=climetlab_wekeo_datasets.ecmwf.satellite_land_cover:satellite_land_cover",  # noqa: E501
            "wekeo-ecmwf-satellite-methane=climetlab_wekeo_datasets.ecmwf.satellite_methane:satellite_methane",  # noqa: E501
            "wekeo-ecmwf-satellite-ocean-colour=climetlab_wekeo_datasets.ecmwf.satellite_ocean_colour:satellite_ocean_colour",  # noqa: E501
            "wekeo-ecmwf-satellite-ozone-v1=climetlab_wekeo_datasets.ecmwf.satellite_ozone_v1:satellite_ozone_v1",  # noqa: E501
            "wekeo-ecmwf-satellite-precipitation-microwave=climetlab_wekeo_datasets.ecmwf.satellite_precipitation_microwave:satellite_precipitation_microwave",  # noqa: E501
            "wekeo-ecmwf-satellite-precipitation=climetlab_wekeo_datasets.ecmwf.satellite_precipitation:satellite_precipitation",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-ice-concentration=climetlab_wekeo_datasets.ecmwf.satellite_sea_ice_concentration:satellite_sea_ice_concentration",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-ice-edge-type=climetlab_wekeo_datasets.ecmwf.satellite_sea_ice_edge_type:satellite_sea_ice_edge_type",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-ice-thickness=climetlab_wekeo_datasets.ecmwf.satellite_sea_ice_thickness:satellite_sea_ice_thickness",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-level-black-sea=climetlab_wekeo_datasets.ecmwf.satellite_sea_level_black_sea:satellite_sea_level_black_sea",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-level-global=climetlab_wekeo_datasets.ecmwf.satellite_sea_level_global:satellite_sea_level_global",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-level-mediterranean=climetlab_wekeo_datasets.ecmwf.satellite_sea_level_mediterranean:satellite_sea_level_mediterranean",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-surface-temperature-ensemble-product=climetlab_wekeo_datasets.ecmwf.satellite_sea_surface_temperature_ensemble_product:satellite_sea_surface_temperature_ensemble_product",  # noqa: E501
            "wekeo-ecmwf-satellite-sea-surface-temperature=climetlab_wekeo_datasets.ecmwf.satellite_sea_surface_temperature:satellite_sea_surface_temperature",  # noqa: E501
            "wekeo-ecmwf-satellite-soil-moisture=climetlab_wekeo_datasets.ecmwf.satellite_soil_moisture:satellite_soil_moisture",  # noqa: E501
            "wekeo-ecmwf-satellite-surface-radiation-budget=climetlab_wekeo_datasets.ecmwf.satellite_surface_radiation_budget:satellite_surface_radiation_budget",  # noqa: E501
            "wekeo-ecmwf-satellite-total-column-water-vapour-land-ocean=climetlab_wekeo_datasets.ecmwf.satellite_total_column_water_vapour_land_ocean:satellite_total_column_water_vapour_land_ocean",  # noqa: E501
            "wekeo-ecmwf-satellite-total-column-water-vapour-ocean=climetlab_wekeo_datasets.ecmwf.satellite_total_column_water_vapour_ocean:satellite_total_column_water_vapour_ocean",  # noqa: E501
            "wekeo-ecmwf-satellite-upper-troposphere-humidity=climetlab_wekeo_datasets.ecmwf.satellite_upper_troposphere_humidity:satellite_upper_troposphere_humidity",  # noqa: E501
            "wekeo-ecmwf-seasonal-monthly-ocean=climetlab_wekeo_datasets.ecmwf.seasonal_monthly_ocean:seasonal_monthly_ocean",  # noqa: E501
            "wekeo-ecmwf-seasonal-monthly-pressure-levels=climetlab_wekeo_datasets.ecmwf.seasonal_monthly_pressure_levels:seasonal_monthly_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-seasonal-monthly-single-levels=climetlab_wekeo_datasets.ecmwf.seasonal_monthly_single_levels:seasonal_monthly_single_levels",  # noqa: E501
            "wekeo-ecmwf-seasonal-original-pressure-levels=climetlab_wekeo_datasets.ecmwf.seasonal_original_pressure_levels:seasonal_original_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-seasonal-original-single-levels=climetlab_wekeo_datasets.ecmwf.seasonal_original_single_levels:seasonal_original_single_levels",  # noqa: E501
            "wekeo-ecmwf-seasonal-postprocessed-pressure-levels=climetlab_wekeo_datasets.ecmwf.seasonal_postprocessed_pressure_levels:seasonal_postprocessed_pressure_levels",  # noqa: E501
            "wekeo-ecmwf-seasonal-postprocessed-single-levels=climetlab_wekeo_datasets.ecmwf.seasonal_postprocessed_single_levels:seasonal_postprocessed_single_levels",  # noqa: E501
            "wekeo-ecmwf-sis-agroclimatic-indicators=climetlab_wekeo_datasets.ecmwf.sis_agroclimatic_indicators:sis_agroclimatic_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-agrometeorological-indicators=climetlab_wekeo_datasets.ecmwf.sis_agrometeorological_indicators:sis_agrometeorological_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-agroproductivity-indicators=climetlab_wekeo_datasets.ecmwf.sis_agroproductivity_indicators:sis_agroproductivity_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-biodiversity-cmip5-global=climetlab_wekeo_datasets.ecmwf.sis_biodiversity_cmip5_global:sis_biodiversity_cmip5_global",  # noqa: E501
            "wekeo-ecmwf-sis-biodiversity-cmip5-regional=climetlab_wekeo_datasets.ecmwf.sis_biodiversity_cmip5_regional:sis_biodiversity_cmip5_regional",  # noqa: E501
            "wekeo-ecmwf-sis-biodiversity-era5-global=climetlab_wekeo_datasets.ecmwf.sis_biodiversity_era5_global:sis_biodiversity_era5_global",  # noqa: E501
            "wekeo-ecmwf-sis-biodiversity-era5-regional=climetlab_wekeo_datasets.ecmwf.sis_biodiversity_era5_regional:sis_biodiversity_era5_regional",  # noqa: E501
            "wekeo-ecmwf-sis-ecv-cmip5-bias-corrected=climetlab_wekeo_datasets.ecmwf.sis_ecv_cmip5_bias_corrected:sis_ecv_cmip5_bias_corrected",  # noqa: E501
            "wekeo-ecmwf-sis-energy-derived-projections=climetlab_wekeo_datasets.ecmwf.sis_energy_derived_projections:sis_energy_derived_projections",  # noqa: E501
            "wekeo-ecmwf-sis-energy-derived-reanalysis=climetlab_wekeo_datasets.ecmwf.sis_energy_derived_reanalysis:sis_energy_derived_reanalysis",  # noqa: E501
            "wekeo-ecmwf-sis-european-risk-extreme-precipitation-indicators=climetlab_wekeo_datasets.ecmwf.sis_european_risk_extreme_precipitation_indicators:sis_european_risk_extreme_precipitation_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-european-risk-flood-indicators=climetlab_wekeo_datasets.ecmwf.sis_european_risk_flood_indicators:sis_european_risk_flood_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-european-wind-storm-indicators=climetlab_wekeo_datasets.ecmwf.sis_european_wind_storm_indicators:sis_european_wind_storm_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-european-wind-storm-synthetic-events=climetlab_wekeo_datasets.ecmwf.sis_european_wind_storm_synthetic_events:sis_european_wind_storm_synthetic_events",  # noqa: E501
            "wekeo-ecmwf-sis-extreme-indices-cmip6=climetlab_wekeo_datasets.ecmwf.sis_extreme_indices_cmip6:sis_extreme_indices_cmip6",  # noqa: E501
            "wekeo-ecmwf-sis-fisheries-abundance=climetlab_wekeo_datasets.ecmwf.sis_fisheries_abundance:sis_fisheries_abundance",  # noqa: E501
            "wekeo-ecmwf-sis-fisheries-eutrophication=climetlab_wekeo_datasets.ecmwf.sis_fisheries_eutrophication:sis_fisheries_eutrophication",  # noqa: E501
            "wekeo-ecmwf-sis-fisheries-ocean-fronts=climetlab_wekeo_datasets.ecmwf.sis_fisheries_ocean_fronts:sis_fisheries_ocean_fronts",  # noqa: E501
            "wekeo-ecmwf-sis-health-vector=climetlab_wekeo_datasets.ecmwf.sis_health_vector:sis_health_vector",  # noqa: E501
            "wekeo-ecmwf-sis-heat-and-cold-spells=climetlab_wekeo_datasets.ecmwf.sis_heat_and_cold_spells:sis_heat_and_cold_spells",  # noqa: E501
            "wekeo-ecmwf-sis-hydrology-meteorology-derived-projections=climetlab_wekeo_datasets.ecmwf.sis_hydrology_meteorology_derived_projections:sis_hydrology_meteorology_derived_projections",  # noqa: E501
            "wekeo-ecmwf-sis-hydrology-variables-derived-projections=climetlab_wekeo_datasets.ecmwf.sis_hydrology_variables_derived_projections:sis_hydrology_variables_derived_projections",  # noqa: E501
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-forecast=climetlab_wekeo_datasets.ecmwf.sis_hydrology_variables_derived_seasonal_forecast:sis_hydrology_variables_derived_seasonal_forecast",  # noqa: E501
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-reforecast=climetlab_wekeo_datasets.ecmwf.sis_hydrology_variables_derived_seasonal_reforecast:sis_hydrology_variables_derived_seasonal_reforecast",  # noqa: E501
            "wekeo-ecmwf-sis-marine-properties=climetlab_wekeo_datasets.ecmwf.sis_marine_properties:sis_marine_properties",  # noqa: E501
            "wekeo-ecmwf-sis-ocean-wave-indicators=climetlab_wekeo_datasets.ecmwf.sis_ocean_wave_indicators:sis_ocean_wave_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-ocean-wave-timeseries=climetlab_wekeo_datasets.ecmwf.sis_ocean_wave_timeseries:sis_ocean_wave_timeseries",  # noqa: E501
            "wekeo-ecmwf-sis-offshore-windfarm-indicators=climetlab_wekeo_datasets.ecmwf.sis_offshore_windfarm_indicators:sis_offshore_windfarm_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-shipping-arctic=climetlab_wekeo_datasets.ecmwf.sis_shipping_arctic:sis_shipping_arctic",  # noqa: E501
            "wekeo-ecmwf-sis-shipping-consumption-on-routes=climetlab_wekeo_datasets.ecmwf.sis_shipping_consumption_on_routes:sis_shipping_consumption_on_routes",  # noqa: E501
            "wekeo-ecmwf-sis-soil-erosion=climetlab_wekeo_datasets.ecmwf.sis_soil_erosion:sis_soil_erosion",  # noqa: E501
            "wekeo-ecmwf-sis-temperature-statistics=climetlab_wekeo_datasets.ecmwf.sis_temperature_statistics:sis_temperature_statistics",  # noqa: E501
            "wekeo-ecmwf-sis-tourism-climate-suitability-indicators=climetlab_wekeo_datasets.ecmwf.sis_tourism_climate_suitability_indicators:sis_tourism_climate_suitability_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-tourism-fire-danger-indicators=climetlab_wekeo_datasets.ecmwf.sis_tourism_fire_danger_indicators:sis_tourism_fire_danger_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-tourism-snow-indicators=climetlab_wekeo_datasets.ecmwf.sis_tourism_snow_indicators:sis_tourism_snow_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-urban-climate-cities=climetlab_wekeo_datasets.ecmwf.sis_urban_climate_cities:sis_urban_climate_cities",  # noqa: E501
            "wekeo-ecmwf-sis-water-hydrological-change=climetlab_wekeo_datasets.ecmwf.sis_water_hydrological_change:sis_water_hydrological_change",  # noqa: E501
            "wekeo-ecmwf-sis-water-level-change-indicators-cmip6=climetlab_wekeo_datasets.ecmwf.sis_water_level_change_indicators_cmip6:sis_water_level_change_indicators_cmip6",  # noqa: E501
            "wekeo-ecmwf-sis-water-level-change-indicators=climetlab_wekeo_datasets.ecmwf.sis_water_level_change_indicators:sis_water_level_change_indicators",  # noqa: E501
            "wekeo-ecmwf-sis-water-level-change-timeseries-cmip6=climetlab_wekeo_datasets.ecmwf.sis_water_level_change_timeseries_cmip6:sis_water_level_change_timeseries_cmip6",  # noqa: E501
            "wekeo-ecmwf-sis-water-level-change-timeseries=climetlab_wekeo_datasets.ecmwf.sis_water_level_change_timeseries:sis_water_level_change_timeseries",  # noqa: E501
            # Eumetsat
            "wekeo-eum-metop-glb-sst-nc=climetlab_wekeo_datasets.eumetsat.eum_metop_glb_sst_nc:eum_metop_glb_sst_nc",  # noqa: E501
            # Mercator
            "wekeo-mercator-arctic-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.arctic_analysisforecast_bgc:arctic_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-arctic-analysisforecast-phy-ice=climetlab_wekeo_datasets.mercator.arctic_analysisforecast_phy_ice:arctic_analysisforecast_phy_ice",  # noqa: E501
            "wekeo-mercator-arctic-analysisforecast-phy=climetlab_wekeo_datasets.mercator.arctic_analysisforecast_phy:arctic_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-arctic-multiyear-bgc=climetlab_wekeo_datasets.mercator.arctic_multiyear_bgc:arctic_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-arctic-multiyear-phy=climetlab_wekeo_datasets.mercator.arctic_multiyear_phy:arctic_multiyear_phy",  # noqa: E501
            "wekeo-mercator-balticsea-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.balticsea_analysisforecast_bgc:balticsea_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-balticsea-analysisforecast-phy=climetlab_wekeo_datasets.mercator.balticsea_analysisforecast_phy:balticsea_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-balticsea-analysisforecast-wav=climetlab_wekeo_datasets.mercator.balticsea_analysisforecast_wav:balticsea_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-balticsea-multiyear-bgc=climetlab_wekeo_datasets.mercator.balticsea_multiyear_bgc:balticsea_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-balticsea-multiyear-phy=climetlab_wekeo_datasets.mercator.balticsea_multiyear_phy:balticsea_multiyear_phy",  # noqa: E501
            "wekeo-mercator-balticsea-reanalysis-wav=climetlab_wekeo_datasets.mercator.balticsea_reanalysis_wav:balticsea_reanalysis_wav",  # noqa: E501
            "wekeo-mercator-blksea-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.blksea_analysisforecast_bgc:blksea_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-blksea-analysisforecast-phy=climetlab_wekeo_datasets.mercator.blksea_analysisforecast_phy:blksea_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-blksea-analysisforecast-wav=climetlab_wekeo_datasets.mercator.blksea_analysisforecast_wav:blksea_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-blksea-multiyear-bgc=climetlab_wekeo_datasets.mercator.blksea_multiyear_bgc:blksea_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-blksea-multiyear-phy=climetlab_wekeo_datasets.mercator.blksea_multiyear_phy:blksea_multiyear_phy",  # noqa: E501
            "wekeo-mercator-blksea-multiyear-wav=climetlab_wekeo_datasets.mercator.blksea_multiyear_wav:blksea_multiyear_wav",  # noqa: E501
            "wekeo-mercator-global-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.global_analysisforecast_bgc:global_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-global-analysisforecast-phy=climetlab_wekeo_datasets.mercator.global_analysisforecast_phy:global_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-global-analysisforecast-wav=climetlab_wekeo_datasets.mercator.global_analysisforecast_wav:global_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-global-multiyear-bgc=climetlab_wekeo_datasets.mercator.global_multiyear_bgc:global_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-global-multiyear-phy-ens=climetlab_wekeo_datasets.mercator.global_multiyear_phy_ens:global_multiyear_phy_ens",  # noqa: E501
            "wekeo-mercator-global-multiyear-phy=climetlab_wekeo_datasets.mercator.global_multiyear_phy:global_multiyear_phy",  # noqa: E501
            "wekeo-mercator-global-multiyear-wav=climetlab_wekeo_datasets.mercator.global_multiyear_wav:global_multiyear_wav",  # noqa: E501
            "wekeo-mercator-ibi-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.ibi_analysisforecast_bgc:ibi_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-ibi-analysisforecast-phy=climetlab_wekeo_datasets.mercator.ibi_analysisforecast_phy:ibi_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-ibi-analysisforecast-wav=climetlab_wekeo_datasets.mercator.ibi_analysisforecast_wav:ibi_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-ibi-multiyear-bgc=climetlab_wekeo_datasets.mercator.ibi_multiyear_bgc:ibi_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-ibi-multiyear-phy=climetlab_wekeo_datasets.mercator.ibi_multiyear_phy:ibi_multiyear_phy",  # noqa: E501
            "wekeo-mercator-ibi-multiyear-wav=climetlab_wekeo_datasets.mercator.ibi_multiyear_wav:ibi_multiyear_wav",  # noqa: E501
            "wekeo-mercator-insitu-glo-phy-ts-oa-my=climetlab_wekeo_datasets.mercator.insitu_glo_phy_ts_oa_my:insitu_glo_phy_ts_oa_my",  # noqa: E501
            "wekeo-mercator-insitu-glo-phy-ts-oa-nrt=climetlab_wekeo_datasets.mercator.insitu_glo_phy_ts_oa_nrt:insitu_glo_phy_ts_oa_nrt",  # noqa: E501
            "wekeo-mercator-medsea-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.medsea_analysisforecast_bgc:medsea_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-medsea-analysisforecast-phy=climetlab_wekeo_datasets.mercator.medsea_analysisforecast_phy:medsea_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-medsea-analysisforecast-wav=climetlab_wekeo_datasets.mercator.medsea_analysisforecast_wav:medsea_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-medsea-multiyear-bgc=climetlab_wekeo_datasets.mercator.medsea_multiyear_bgc:medsea_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-medsea-multiyear-phy=climetlab_wekeo_datasets.mercator.medsea_multiyear_phy:medsea_multiyear_phy",  # noqa: E501
            "wekeo-mercator-medsea-multiyear-wav=climetlab_wekeo_datasets.mercator.medsea_multiyear_wav:medsea_multiyear_wav",  # noqa: E501
            "wekeo-mercator-multiobs-glo-bio-bgc-3d-rep=climetlab_wekeo_datasets.mercator.multiobs_glo_bio_bgc_3d_rep:multiobs_glo_bio_bgc_3d_rep",  # noqa: E501
            "wekeo-mercator-multiobs-glo-bio-carbon-surface-rep=climetlab_wekeo_datasets.mercator.multiobs_glo_bio_carbon_surface_rep:multiobs_glo_bio_carbon_surface_rep",  # noqa: E501
            "wekeo-mercator-multiobs-glo-phy-mynrt=climetlab_wekeo_datasets.mercator.multiobs_glo_phy_mynrt:multiobs_glo_phy_mynrt",  # noqa: E501
            "wekeo-mercator-multiobs-glo-phy-s-surface-mynrt=climetlab_wekeo_datasets.mercator.multiobs_glo_phy_s_surface_mynrt:multiobs_glo_phy_s_surface_mynrt",  # noqa: E501
            "wekeo-mercator-multiobs-glo-phy-sss-l4-my=climetlab_wekeo_datasets.mercator.multiobs_glo_phy_sss_l4_my:multiobs_glo_phy_sss_l4_my",  # noqa: E501
            "wekeo-mercator-multiobs-glo-phy-tsuv-3d-mynrt=climetlab_wekeo_datasets.mercator.multiobs_glo_phy_tsuv_3d_mynrt:multiobs_glo_phy_tsuv_3d_mynrt",  # noqa: E501
            "wekeo-mercator-multiobs-glo-phy-w-3d-rep=climetlab_wekeo_datasets.mercator.multiobs_glo_phy_w_3d_rep:multiobs_glo_phy_w_3d_rep",  # noqa: E501
            "wekeo-mercator-nwshelf-analysisforecast-bgc=climetlab_wekeo_datasets.mercator.nwshelf_analysisforecast_bgc:nwshelf_analysisforecast_bgc",  # noqa: E501
            "wekeo-mercator-nwshelf-analysisforecast-phy=climetlab_wekeo_datasets.mercator.nwshelf_analysisforecast_phy:nwshelf_analysisforecast_phy",  # noqa: E501
            "wekeo-mercator-nwshelf-analysisforecast-wav=climetlab_wekeo_datasets.mercator.nwshelf_analysisforecast_wav:nwshelf_analysisforecast_wav",  # noqa: E501
            "wekeo-mercator-nwshelf-multiyear-bgc=climetlab_wekeo_datasets.mercator.nwshelf_multiyear_bgc:nwshelf_multiyear_bgc",  # noqa: E501
            "wekeo-mercator-nwshelf-multiyear-phy=climetlab_wekeo_datasets.mercator.nwshelf_multiyear_phy:nwshelf_multiyear_phy",  # noqa: E501
            "wekeo-mercator-nwshelf-reanalysis-wav=climetlab_wekeo_datasets.mercator.nwshelf_reanalysis_wav:nwshelf_reanalysis_wav",  # noqa: E501
            "wekeo-mercator-oceancolour-arc-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_arc_bgc_l3_my:oceancolour_arc_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-arc-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_arc_bgc_l4_my:oceancolour_arc_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-atl-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_atl_bgc_l3_my:oceancolour_atl_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-atl-bgc-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_atl_bgc_l3_nrt:oceancolour_atl_bgc_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-atl-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_atl_bgc_l4_my:oceancolour_atl_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-atl-bgc-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_atl_bgc_l4_nrt:oceancolour_atl_bgc_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-hr-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_hr_l3_nrt:oceancolour_bal_bgc_hr_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-hr-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_hr_l4_nrt:oceancolour_bal_bgc_hr_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_l3_my:oceancolour_bal_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_l3_nrt:oceancolour_bal_bgc_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_l4_my:oceancolour_bal_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-bal-bgc-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_bal_bgc_l4_nrt:oceancolour_bal_bgc_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-hr-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_hr_l3_nrt:oceancolour_blk_bgc_hr_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-hr-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_hr_l4_nrt:oceancolour_blk_bgc_hr_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_l3_my:oceancolour_blk_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_l3_nrt:oceancolour_blk_bgc_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_l4_my:oceancolour_blk_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-blk-bgc-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_blk_bgc_l4_nrt:oceancolour_blk_bgc_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-glo-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_glo_bgc_l3_my:oceancolour_glo_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-glo-bgc-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_glo_bgc_l3_nrt:oceancolour_glo_bgc_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-glo-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_glo_bgc_l4_my:oceancolour_glo_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-glo-bgc-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_glo_bgc_l4_nrt:oceancolour_glo_bgc_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-ibi-bgc-hr-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_ibi_bgc_hr_l3_nrt:oceancolour_ibi_bgc_hr_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-ibi-bgc-hr-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_ibi_bgc_hr_l4_nrt:oceancolour_ibi_bgc_hr_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-hr-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_hr_l3_nrt:oceancolour_med_bgc_hr_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-hr-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_hr_l4_nrt:oceancolour_med_bgc_hr_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-l3-my=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_l3_my:oceancolour_med_bgc_l3_my",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_l3_nrt:oceancolour_med_bgc_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-l4-my=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_l4_my:oceancolour_med_bgc_l4_my",  # noqa: E501
            "wekeo-mercator-oceancolour-med-bgc-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_med_bgc_l4_nrt:oceancolour_med_bgc_l4_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-nws-bgc-hr-l3-nrt=climetlab_wekeo_datasets.mercator.oceancolour_nws_bgc_hr_l3_nrt:oceancolour_nws_bgc_hr_l3_nrt",  # noqa: E501
            "wekeo-mercator-oceancolour-nws-bgc-hr-l4-nrt=climetlab_wekeo_datasets.mercator.oceancolour_nws_bgc_hr_l4_nrt:oceancolour_nws_bgc_hr_l4_nrt",  # noqa: E501
            "wekeo-mercator-seaice-ant-phy-l3-my=climetlab_wekeo_datasets.mercator.seaice_ant_phy_l3_my:seaice_ant_phy_l3_my",  # noqa: E501
            "wekeo-mercator-seaice-arc-phy-climate-l3-my=climetlab_wekeo_datasets.mercator.seaice_arc_phy_climate_l3_my:seaice_arc_phy_climate_l3_my",  # noqa: E501
            "wekeo-mercator-seaice-arc-phy-climate-l4-my=climetlab_wekeo_datasets.mercator.seaice_arc_phy_climate_l4_my:seaice_arc_phy_climate_l4_my",  # noqa: E501
            "wekeo-mercator-seaice-arc-seaice-l3-rep-observations=climetlab_wekeo_datasets.mercator.seaice_arc_seaice_l3_rep_observations:seaice_arc_seaice_l3_rep_observations",  # noqa: E501
            "wekeo-mercator-seaice-arc-seaice-l4-nrt-observations=climetlab_wekeo_datasets.mercator.seaice_arc_seaice_l4_nrt_observations:seaice_arc_seaice_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-seaice-bal-phy-l4-my=climetlab_wekeo_datasets.mercator.seaice_bal_phy_l4_my:seaice_bal_phy_l4_my",  # noqa: E501
            "wekeo-mercator-seaice-bal-seaice-l4-nrt-observations=climetlab_wekeo_datasets.mercator.seaice_bal_seaice_l4_nrt_observations:seaice_bal_seaice_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-seaice-glo-phy-climate-l3-my=climetlab_wekeo_datasets.mercator.seaice_glo_phy_climate_l3_my:seaice_glo_phy_climate_l3_my",  # noqa: E501
            "wekeo-mercator-seaice-glo-seaice-l4-rep-observations=climetlab_wekeo_datasets.mercator.seaice_glo_seaice_l4_rep_observations:seaice_glo_seaice_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-sealevel-eur-phy-l4-my=climetlab_wekeo_datasets.mercator.sealevel_eur_phy_l4_my:sealevel_eur_phy_l4_my",  # noqa: E501
            "wekeo-mercator-sealevel-eur-phy-l4-nrt=climetlab_wekeo_datasets.mercator.sealevel_eur_phy_l4_nrt:sealevel_eur_phy_l4_nrt",  # noqa: E501
            "wekeo-mercator-sealevel-glo-phy-climate-l4-my=climetlab_wekeo_datasets.mercator.sealevel_glo_phy_climate_l4_my:sealevel_glo_phy_climate_l4_my",  # noqa: E501
            "wekeo-mercator-sealevel-glo-phy-l4-my=climetlab_wekeo_datasets.mercator.sealevel_glo_phy_l4_my:sealevel_glo_phy_l4_my",  # noqa: E501
            "wekeo-mercator-sealevel-glo-phy-l4-nrt=climetlab_wekeo_datasets.mercator.sealevel_glo_phy_l4_nrt:sealevel_glo_phy_l4_nrt",  # noqa: E501
            "wekeo-mercator-sst-atl-phy-l3s-my=climetlab_wekeo_datasets.mercator.sst_atl_phy_l3s_my:sst_atl_phy_l3s_my",  # noqa: E501
            "wekeo-mercator-sst-atl-phy-l3s-nrt=climetlab_wekeo_datasets.mercator.sst_atl_phy_l3s_nrt:sst_atl_phy_l3s_nrt",  # noqa: E501
            "wekeo-mercator-sst-atl-sst-l4-nrt-observations=climetlab_wekeo_datasets.mercator.sst_atl_sst_l4_nrt_observations:sst_atl_sst_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-atl-sst-l4-rep-observations=climetlab_wekeo_datasets.mercator.sst_atl_sst_l4_rep_observations:sst_atl_sst_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-sst-bal-phy-l3s-my=climetlab_wekeo_datasets.mercator.sst_bal_phy_l3s_my:sst_bal_phy_l3s_my",  # noqa: E501
            "wekeo-mercator-sst-bal-phy-subskin-l4-nrt=climetlab_wekeo_datasets.mercator.sst_bal_phy_subskin_l4_nrt:sst_bal_phy_subskin_l4_nrt",  # noqa: E501
            "wekeo-mercator-sst-bal-sst-l3s-nrt-observations=climetlab_wekeo_datasets.mercator.sst_bal_sst_l3s_nrt_observations:sst_bal_sst_l3s_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-bal-sst-l4-rep-observations=climetlab_wekeo_datasets.mercator.sst_bal_sst_l4_rep_observations:sst_bal_sst_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-sst-bs-phy-l3s-my=climetlab_wekeo_datasets.mercator.sst_bs_phy_l3s_my:sst_bs_phy_l3s_my",  # noqa: E501
            "wekeo-mercator-sst-bs-phy-subskin-l4-nrt=climetlab_wekeo_datasets.mercator.sst_bs_phy_subskin_l4_nrt:sst_bs_phy_subskin_l4_nrt",  # noqa: E501
            "wekeo-mercator-sst-bs-sst-l3s-nrt-observations=climetlab_wekeo_datasets.mercator.sst_bs_sst_l3s_nrt_observations:sst_bs_sst_l3s_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-bs-sst-l4-nrt-observations=climetlab_wekeo_datasets.mercator.sst_bs_sst_l4_nrt_observations:sst_bs_sst_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-bs-sst-l4-rep-observations=climetlab_wekeo_datasets.mercator.sst_bs_sst_l4_rep_observations:sst_bs_sst_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-sst-glo-phy-l3s-my=climetlab_wekeo_datasets.mercator.sst_glo_phy_l3s_my:sst_glo_phy_l3s_my",  # noqa: E501
            "wekeo-mercator-sst-glo-phy-l4-nrt=climetlab_wekeo_datasets.mercator.sst_glo_phy_l4_nrt:sst_glo_phy_l4_nrt",  # noqa: E501
            "wekeo-mercator-sst-glo-sst-l3s-nrt-observations=climetlab_wekeo_datasets.mercator.sst_glo_sst_l3s_nrt_observations:sst_glo_sst_l3s_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-glo-sst-l4-nrt-observations=climetlab_wekeo_datasets.mercator.sst_glo_sst_l4_nrt_observations:sst_glo_sst_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-glo-sst-l4-rep-observations=climetlab_wekeo_datasets.mercator.sst_glo_sst_l4_rep_observations:sst_glo_sst_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-sst-med-phy-l3s-my=climetlab_wekeo_datasets.mercator.sst_med_phy_l3s_my:sst_med_phy_l3s_my",  # noqa: E501
            "wekeo-mercator-sst-med-phy-subskin-l4-nrt=climetlab_wekeo_datasets.mercator.sst_med_phy_subskin_l4_nrt:sst_med_phy_subskin_l4_nrt",  # noqa: E501
            "wekeo-mercator-sst-med-sst-l3s-nrt-observations=climetlab_wekeo_datasets.mercator.sst_med_sst_l3s_nrt_observations:sst_med_sst_l3s_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-med-sst-l4-nrt-observations=climetlab_wekeo_datasets.mercator.sst_med_sst_l4_nrt_observations:sst_med_sst_l4_nrt_observations",  # noqa: E501
            "wekeo-mercator-sst-med-sst-l4-rep-observations=climetlab_wekeo_datasets.mercator.sst_med_sst_l4_rep_observations:sst_med_sst_l4_rep_observations",  # noqa: E501
            "wekeo-mercator-wave-glo-phy-spc-l4-nrt=climetlab_wekeo_datasets.mercator.wave_glo_phy_spc_l4_nrt:wave_glo_phy_spc_l4_nrt",  # noqa: E501
            "wekeo-mercator-wave-glo-phy-swh-l4-my=climetlab_wekeo_datasets.mercator.wave_glo_phy_swh_l4_my:wave_glo_phy_swh_l4_my",  # noqa: E501
            "wekeo-mercator-wave-glo-phy-swh-l4-nrt=climetlab_wekeo_datasets.mercator.wave_glo_phy_swh_l4_nrt:wave_glo_phy_swh_l4_nrt",  # noqa: E501
            "wekeo-mercator-wind-glo-phy-climate-l4-my=climetlab_wekeo_datasets.mercator.wind_glo_phy_climate_l4_my:wind_glo_phy_climate_l4_my",  # noqa: E501
            "wekeo-mercator-wind-glo-phy-l3-my=climetlab_wekeo_datasets.mercator.wind_glo_phy_l3_my:wind_glo_phy_l3_my",  # noqa: E501
            "wekeo-mercator-wind-glo-phy-l3-nrt=climetlab_wekeo_datasets.mercator.wind_glo_phy_l3_nrt:wind_glo_phy_l3_nrt",  # noqa: E501
            "wekeo-mercator-wind-glo-phy-l4-my=climetlab_wekeo_datasets.mercator.wind_glo_phy_l4_my:wind_glo_phy_l4_my",  # noqa: E501
            "wekeo-mercator-wind-glo-phy-l4-nrt=climetlab_wekeo_datasets.mercator.wind_glo_phy_l4_nrt:wind_glo_phy_l4_nrt",  # noqa: E501
        ]
        # source plugins would be here
        # "climetlab.sources": []
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
