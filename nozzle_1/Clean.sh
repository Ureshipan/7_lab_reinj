#!/bin/bash

cd /home/mark/OpenFOAM/mark-12/run/nozzle_1

rm -rf 0.*
rm -rf processor*
rm -rf constant/polyMesh
rm -rf geometry/Mesh.unv
rm 0/p
cp 0/p.org 0/p
rm log

sed -i '19,23d' params.txt

echo Done
