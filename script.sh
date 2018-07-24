#!/usr/bin/env bash

set -euo pipefail

KAGGLE_DIR=".kaggle"

mkdir $KAGGLE_DIR

echo '{"username":"tmosley","key":"'"$KAGGLE_API_KEY"'"}' > $KAGGLE_DIR/kaggle.json

kaggle competitions download -c whale-categorization-playground

mv $KAGGLE_DIR/competitions/whale-categorization-playground .
