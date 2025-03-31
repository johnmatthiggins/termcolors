#!/usr/bin/env sh
ssh infrastructure 'cd repos/termcolors && git pull && bash --login ./deploy.sh';
