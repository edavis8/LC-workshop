#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:17:03 2021

@author: admin
"""
import requests
import json
import pandas as pd
import csv

query = "COVID covid testing tested vaccine vaccinated mask masks mandate anti-vax anti-vaxxers \
    lockdown Pfizer Moderna Johnson J&J Fauci delta ventilator ventilators beds hospital Texas \
        Missouri Florida California Missouri Connecticut Louisiana NYC spread pandemic virus China India Brazil US \
            Belgium UK NZ Australia taste smell"
language = "en"
metric = "rank"
rt = "false"

r = requests.get(f"https://storywrangling.org/api/ngrams/{query}?language={language}&metric={metric}&rt={rt}").json()

dfs = {}
for ngram in r['data']:
    dfs[ngram] = pd.DataFrame(r['data'][ngram], columns=list(r['data'][ngram].keys()))
dfs.keys()

all_data = pd.DataFrame(columns=list(r['data'][ngram].keys())+['ngram'])
for ngram in dfs:
    df = dfs[ngram]
    df['ngram']=ngram
    all_data = all_data.append(df)
    #dfs[ngram].to_csv(f"twitter-data/{ngram}.csv")
    
all_data = all_data.reset_index(drop=True)
#all_data = all_data.set_index('date')
all_data.to_csv('twitter-covid.csv', index=False)
