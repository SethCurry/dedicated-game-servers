#!/bin/bash

export PYTHONPATH="$PYTHONPATH:$(pwd)/base/dgs"

for dir in ./*; do
  if [ ! -d $dir ]; then
    continue
  fi
  if [ ! -f $dir/gen-docs.py ]; then
    echo "No gen-docs.py in $dir, skipping"
    continue
  fi

  echo "Building docs in $dir"
  pushd $dir &> /dev/null
  python gen-docs.py
  popd &> /dev/null
done