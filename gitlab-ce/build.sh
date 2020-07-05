#!/bin/bash
export GITLAB_HOME=/opt/gitlab
git clone --recursive https://gitlab.com/gitlab-org/omnibus-gitlab.git
ln -s ./omnibus-gitlab/docker/assets
docker build -t gitlab-ce:ubuntu18 ./
