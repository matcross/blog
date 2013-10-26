#!/bin/sh -u
exclude_file=/fserver/mathewc/scripts/archive_diff_excludes
svn diff --no-diff-deleted --diff-cmd diff -x "--ignore-all-space --text --unified=0" $* | \
  filterdiff --verbose --exclude-from-file ${exclude_file} | grep -v --file=${exclude_file} | colordiff | less -RS
