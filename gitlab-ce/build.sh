#!/bin/bash
echo Dockerfile copies a local file called RELEASE into container file-system that is sourced by the startup wrapper script
echo Dockerfile copies the startup wrapper script and more from the git repos docker/assets -- so use a sym-link to assets
echo 'docker run -dit -p80:80 -p8022:22 -p8443:443 --name gitlab gitlab-ce:ubu20 /usr/local/bin/wrapper'
export GITLAB_HOME=/opt/gitlab
touch RELEASE 
echo 'RELEASE_PACKAGE=gitlab-ce' > RELEASE
echo 'RELEASE_VERSION=13.1.2-ce.0' >> RELEASE
if [ ! -e omnibus-gitlab ] ; then
  git clone --recursive https://gitlab.com/gitlab-org/omnibus-gitlab.git
fi
if [ ! -e assets ] ; then
  ln -s ./omnibus-gitlab/docker/assets
fi
if [ ! -e Dockerfile ] ; then
  ln -s Dockerfile.gitlabce_focal_fossa Dockerfile
fi
docker build -t gitlab-ce:ubu20 ./
echo 'docker run -dit -p80:80 -p8022:22 -p8443:443 --name gitlab gitlab-ce:ubu20 /usr/local/bin/wrapper'

