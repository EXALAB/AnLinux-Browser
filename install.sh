#!/bin/bash
# License: GPL 3.0
# (c) 2022 Star Inc.

if [ $(lsb_release -si) == "Ubuntu" ]; then
    apt-get install -y python3 gir1.2-webkit2-4.0 python3-gi fonts-droid-fallback
else
    echo "Now, it was only support/tested on \"the Ubuntu for AnLinux\""
    echo "But you still can install the browser on other Linux distribution without the shell script."
fi
