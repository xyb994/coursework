#!/bin/bash

time wget -pqO - "$1" | head -n 8
