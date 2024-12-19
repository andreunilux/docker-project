# A docker dummy project for my DevOps Course

## Overview
This project aims to provide you with a docker image that you can run with one command. It provides you the option to play a collection CLI games (at the moment just 1) 

## Features
- Dockerized and integrated with GitHub Actions for CI/CD
- the app is written in Python 

## Requirements
- Install Docker 

## Installation
For the specifications you can have a look at the git repository.
You can directly deploy the CLI games by running:
```
docker pull andre794/my-app:latest
```
and then use:
```
docker run -it andre794/my-app:latest
```
