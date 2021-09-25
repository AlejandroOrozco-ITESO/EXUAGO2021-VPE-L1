#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA QUE IMPRIME LA TABLA DE MULTIPLICAR SOLICITADA POR EL USUARIO
"""


num_tabla = int(input("Ingresa la tabla que deseas visualizar: "))

print("||Tabla del", num_tabla, "||")

for m in range (1, 11):
    resultado = m * num_tabla
    print(num_tabla,"x", m,"=", resultado)


