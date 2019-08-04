#!/bin/bash
# License: GPL 3.0
# (c) 2019 Star Inc.

if [ -f /etc/os-release ]; then
    OS=$NAME
    VER=$VERSION_ID
fi

if [ "$OS" == "Ubuntu" ] && [ $VER -ge 16 ]; then
    apt-get install -y python3 gir1.2-webkit-3.0 python-gi
else
    echo "Now, it was only support/tested on \"the Ubuntu for AnLinux\""
    echo "But you still can install the browser on other Linux distribution without the shell script."
fi