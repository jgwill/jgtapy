if [ "$2" != "" ]; then
pversion=$1
nversion=$2
cdir=$(pwd)
json2bash package.json > .package-autobuild.sh && . .package-autobuild.sh && \
	json2bash package.json "directories" > .package-autobuild-directories.sh && . .package-autobuild-directories.sh && \
	export subdir=$src
#if [ -e "jgtpy/.flag" ] ;then 
cd $subdir
for f in $(ls *);do if [ -f "$f" ]; then sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;fi;done
cd $cdir
if [ -d "test" ]; then 
	cd test
	for f in $(ls *);do if [ -f "$f" ]; then sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;fi;done
fi
cd $cdir
for f in $(ls *);do if [ -f "$f" ]; then sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;fi;done
#else
#	echo " MUST USE VM  To have jgtpy Mounted: use dkrun "
#fi
else
	echo "Must supply old and new version number"
fi
