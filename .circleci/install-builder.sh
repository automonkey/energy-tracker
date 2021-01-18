#!/usr/bin/env bash

set -eo pipefail

(
    cd builder;
    make install;
    cp "$(make getbinpath)/energy-tracker-build" .;
    echo "export PATH=$PATH:$(make getbinpath)" >> $BASH_ENV
)
