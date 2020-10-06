#!/usr/bin/env bash

set -eo pipefail

(
    cd builder;
    make install;
    echo "export PATH=$PATH:$(make getbinpath)" >> $BASH_ENV
)
