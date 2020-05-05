#!/bin/bash

# place 'blacklist-nouveau.conf' at the same directory
# run with 'sudo' 

cp blacklist-nouveau.conf /etc/modprobe.d/

update-initramfs -u
