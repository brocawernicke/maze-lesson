#!/bin/bash

pass=0
total=0

for map in ../maps/*; do
  let total+=1
  python3 maze_server.py $map &
  if python3 runner_client.py; then
    let pass+=1
  fi
done

let score=100*pass/total
echo "Score: $score ($pass/$total)"