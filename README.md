# LOL Stats

[![Build Status](https://travis-ci.org/baptistelinel/lol-stats.svg?branch=master)](https://travis-ci.org/baptistelinel/lol-stats)
[![Maintainability](https://api.codeclimate.com/v1/badges/436dc7fce112defb6ae9/maintainability)](https://codeclimate.com/github/baptistelinel/lol-stats/maintainability)

## Description

Warning: this project is not currently in production.

This application is based on Riot API. It aims to show the play style 
of a League Of Legends summoner with statistics.

## API key

In order to run this application it first mandatory to get an API key.
This can be done [here](https://developer.riotgames.com/).

## Architecture

* The application code is into `sources/`.
    * The python libraries that needed to be adapter are in `sources/adapters`.
    * The python code who makes HTTP requests is in `soources/requesters`.
* The tests are into `tests/`
* The Dockerfile are into `dockers/`

## Continuous integration

The project uses [Travis](https://travis-ci.org/).
More information about the CI pipeline into `.travis.yml`

## Versions

* python 3.5.6
* docker 19.03.8, build afacb8b
* docker-compose 1.25.4, build 8d51620a