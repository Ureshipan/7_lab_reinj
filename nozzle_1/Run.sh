#!/bin/bash

# Получаем путь к текущей директории
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Запуск генерации сетки в Salome
# Предполагаем, что SALOME установлен и доступен в PATH
salome -t "$CURRENT_DIR/geometry/Mesh.py"

# Импорт сетки в OpenFOAM
cd "$CURRENT_DIR"
ideasUnvToFoam geometry/Mesh.unv
transformPoints "scale = (0.001 0.001 0.001)"

# Корректировка типов патчей в boundary
sed -i '/wall/,/}/s/type[ \t]*patch/type wall/' constant/polyMesh/boundary
sed -i '/front/,/}/s/type[ \t]*patch/type wedge/' constant/polyMesh/boundary
sed -i '/back/,/}/s/type[ \t]*patch/type wedge/' constant/polyMesh/boundary

# Также обновим начальные условия в 0/p
sed -i '/front/,/}/s/type[ \t]*patch/type wedge/' 0/p
sed -i '/back/,/}/s/type[ \t]*patch/type wedge/' 0/p
sed -i '/wall/,/}/s/type[ \t]*patch/type wall/' 0/p

width=$(head -n 20 params.txt | tail -n 1)
height=$(head -n 23 params.txt | tail -n 1)

sed -i "26s/.*/   box (-${width} 0 -1) (0 ${height} 1);/" system/setFieldsDict

# Установим поля и запустим визуализацию
setFields
decomposePar
mpirun -np 4 rhoPimpleFoam -parallel >log
#reconstructPar
#paraFoam
