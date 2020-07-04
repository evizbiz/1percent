#!/bin/bash
git clone --recursive https://gitlab.com/gitlab-org/omnibus-gitlab.git
ln -s ./omnibus-gitlab/docker/assets
docker build -t gitlab-ce:ubuntu18 ./
