#! /usr/bin/env bash

set -euo pipefail

function main(){

  echo "Stopping and removing old container if exists..."
  docker stop recipe_container || true && docker rm recipe_container || true

  echo "Building image..."
  docker build -t recipe_image .

  echo "Running container..."
  docker run --env EDAMAM_APP_ID --env EDAMAM_APP_KEY -p 5000:5000 --name recipe_container recipe_image
}

main
