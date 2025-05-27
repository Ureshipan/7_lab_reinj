#!/bin/bash

# Получаем путь к текущей директории
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Чтение параметров из файла
p_input=$(head -n 2 params.txt | tail -n 1)
t_input=$(head -n 5 params.txt | tail -n -1)
p_output=$(head -n 8 params.txt | tail -n 1)
G=$(head -n 11 params.txt | tail -n 1)
alpha=$(head -n 14 params.txt | tail -n 1)
betta=$(head -n 17 params.txt | tail -n 1)

echo p_input = $p_input
echo t_input = $t_input
echo p_output = $p_output
echo G = $G
echo alpha = $alpha
echo betta = $betta

# Используем относительные пути
sed -i "18s/.*/internalField   uniform ${p_output};/;25s/.*/value uniform ${p_input};/;36s/.*/ value uniform ${p_output};/" 0/p.org

sed -i "18s/.*/internalField   uniform ${t_input};/;25s/.*/        value           uniform ${t_input};/;36s/.*/        value           uniform ${t_input};/" 0/T

sed -i "19s/.*/    volScalarFieldValue p ${p_output}/;29s/.*/            volScalarFieldValue p ${p_input}/;" system/setFieldsDict

sed -i "18s/.*/P_input = ${p_input}/;19s/.*/T_input = ${t_input}/;20s/.*/P_output = ${p_output}/;21s/.*/G = ${G}/;22s/.*/alpha_ = ${alpha}/;23s/.*/betta_ = ${betta}/" geometry/Mesh.py
