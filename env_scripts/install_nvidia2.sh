#!/bin/bash

apt-get --purge remove nvidia-*
apt -y install nvidia-driver-430

# reboot

