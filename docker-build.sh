#!/bin/bash

cp helper.py Database/dockerfile/

cp bot.py Database/dockerfile/

cd Database

docker-compose up --build -d

rm dockerfile/helper.py
rm dockerfile/bot.py