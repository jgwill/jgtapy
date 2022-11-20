pversion=1.9.7
nversion=1.9.8
cdir=$(pwd)

cd jgtapy
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
cd test
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done
cd $cdir
for f in $(ls *);do sed -i 's/'$pversion'/'$nversion'/g' $f &>/dev/null;done

