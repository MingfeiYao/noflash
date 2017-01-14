#!/usr/bin/env
import requests


key = "RGAPI-8363b691-2bef-4fbb-b05e-e2c3483c24ef"

def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api+key=" + key
    response = requests.get(URL)
    return response.json()

requestSummonerData("euw", "captainsyria")
