datos = {
    'nombre': "Omar",
    'apellido': "MT",
    'edad': 29,
    'fn': {
        'day': 7,
        'month': 11,
        'year': 1994
    }
}

print(datos)

# Leer datos
print(
    f"\nNombre: {datos['nombre']} {datos['apellido']} tiene {datos['edad']} años.\nFecha de nacimiento: {datos['fn']['day']}/{datos['fn']['month']}/{datos['fn']['year']}"
)

print(datos.get('phone'))  #None
# Update
#Add attribute
datos['phone'] = '+34 123 456 789'
print(datos)
#Edit att
datos['phone'] = '+52 123 456 789'
print(datos)
#Delete att
del datos['phone']
print(datos)
