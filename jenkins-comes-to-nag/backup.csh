#!/bin/tcsh
cd $JENKINS_HOME
svn add -q --parents \
  *.xml jobs/*/config.xml users/*/config.xml userContent/* >& /dev/null
svn pd -q svn:mime-type \
  *.xml jobs/*/config.xml users/*/config.xml userContent/*.xml
echo "fingerprints\nwarnlog\n*.log\n*.tmp\n*.old\n*.bak\n*.jar" > myignores
echo "*.json\n*.lck\n.owner\nidentity.key\njenkins" >> myignores
echo "jenkins.security*\njenkins.diagnostics*\nlog*\nplugins*" >> myignores
echo "secret*\nupdates" >> myignores
svn ps -q svn:ignore -F myignores .
rm myignores
echo "builds\nlast*\nnext*\n*.txt\n*.log\nworkspace*\ncobertura" > myjobignores
echo "javadoc\nhtmlreports\nncover\ndoclinks\noutOfOrderBuilds" >> myjobignores
svn ps -q svn:ignore -F myjobignores jobs/*
rm myjobignores
svn status | grep '!' | awk '{print $2;}' | xargs -r svn rm
if ($# == 0) then
  set msg="Jenkins configuration updated automatically"
else
  set msg="${1}"
endif
svn ci --non-interactive --username=jenkins -m "${msg}" || exit 1
svn st
