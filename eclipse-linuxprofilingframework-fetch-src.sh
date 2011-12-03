#!/bin/sh
usage="usage: $0 <tag>"
name=eclipse-linuxprofilingframework
tag=$1
tar_name=$name-fetched-src-$tag

if [ "x${tag}"x = "xx" ]; then
   echo >&2 ${usage}
   exit 1
fi

rm -fr $tar_name && mkdir $tar_name
pushd $tar_name

svn export http://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/profiling/tags/$tag/
mv $tag/* .
rmdir $tag

popd
# create archive
tar -cjf $tar_name.tar.bz2 $tar_name
