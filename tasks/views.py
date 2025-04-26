from django.shortcuts import render
import re


def index(request):
    title = 'Validación de archivos'
    info = 'Por favor cargue el archivo que desea validar. Recuerde que el formato debe ser .txt '
    modal = False
    error_modal = False

    table_content = []

    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            content = file.read().decode('utf-8')
            table_row = content.splitlines()
            for i, row in enumerate(table_row):
                table_column = row.split(',')
                table_content.append(table_column)
            file_error = validate_file(content)

            if file_error:
                error_modal = file_error
            else:
                error_modal = False
            modal = True
        else:
            modal = True
            error_modal = 'No se ha recibido ningún archivo.'

    return render(request, 'index.html', {
        'title': title,
        'info': info,
        'modal': modal,
        'error_modal': error_modal,
        'content': table_content if 'content' in locals() else None
    })


# Función validación
def validate_file(content):
    error = ''
    rows = content.split('\n')
    for i, row in enumerate(rows):
        columns = row.split(',')

        # Reglas
        # 5 columnas
        if len(columns) != 5:
            return f'Error en la fila {i + 1}: Se esperaban 5 columnas, pero se encontraron {len(columns)}.'

        # Columna 1: Enteros entre 3 y 10 caracteres
        try:
            col1 = int(columns[0])
            condition = 3 <= len(str(col1)) <= 10
            error += '' if condition else f'Error en la fila {i + 1}: El dato de la columna 1 debe tener entre 3 y 10 caracteres.\n'

        except ValueError:
            error += f'Error en la fila {i + 1}: El dato de la columna 1 debe ser un número entero.\n'

        # Columna 2: Email
        email_regex = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, columns[1].strip()):
            error += f'Error en la fila {i + 1}: El dato de la columna 2 debe ser un email válido.\n'

        # Columna 3: 'CC' o 'TI'
        if not columns[2].strip() in ['CC', 'TI']:
            error += f'Error en la fila {i + 1}: En la columna 3 solo se permite "CC" o "TI".\n'

        # Columna 4: Valores entre 500k y 1.500k
        try:
            col4 = float(columns[3])
            condition = 500000 <= col4 <= 1500000
            error += '' if condition else f'Error en la fila {i + 1}: El dato de la columna 4 debe estar entre 500k y 1.500k.\n'
        except ValueError:
            error += f'Error en la fila {i + 1}: El dato debe ser un valor numérico.\n'
    return error
