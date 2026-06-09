#!/bin/bash

sudo systemctl start buscador.service

sleep 3

google-chrome http://localhost:2405 &
