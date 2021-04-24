#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet Hackathon COVID
@author: Thomas Guyet, Institut Agro/IRISA
"""

import pandas as pd

# chargement des données
# -> nombre de nouveaux cas par jours et par département 
hospi=pd.read_csv("donnees-hospitalieres-nouveaux-covid19-2021-04-22-18h06.csv",sep=";")
regions = pd.read_csv("../commun/departements-region.csv",sep=",")

# ajout des régions aux hospitalisations
hospi=hospi.merge(regions, left_on="dep", right_on="num_dep", how="inner")
hospi["jour"]=pd.to_datetime(hospi["jour"])
del(hospi['dep_name'])


#Ici, on a les données par jours et par département

#pas besoin des départements
del(hospi['dep'])
hospi['jour'] = pd.to_datetime( hospi['jour'] )

#Attention ... la ligne suivante est violente : elle fait tout ce dont on a besoin!
data=hospi.groupby('region_name').resample("W-MON", on="jour").sum()
data.reset_index(inplace=True)

data.rename(columns={'region_name':'region',
                     'jour':'date',
                     'incid_dc':'incid_dc_features_hospit',
                     'incid_rea':'incid_rea_features_hospit',
                     'incid_rad':'incid_rad_features_hospit',
                     'incid_hosp':'incid_hosp_features_hospit'}, inplace=True)

# on génère le fichier de sortie dans "final"
data.to_csv("../final/hospit_formatted.csv", index=False)

    