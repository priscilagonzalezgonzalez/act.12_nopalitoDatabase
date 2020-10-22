import mysql.connector

bd = mysql.connector.connect(user='sarahi',
    password='sayonarasaly4',
    database='nopalito')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar usuarios')
    print('0) Salir')
    op = input()

    if op == '1':
        correo = input('Correo: ')
        contra = input('Contraseña: ')

        consulta = "INSERT INTO usuario (correo, contrasena)"\
                    "VALUES (%s, %s)"
        cursor.execute(consulta,(correo, contra))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print('Error')

    elif op == '2':
        consulta = "SELECT * FROM usuario"
        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("Id: ", row[0])
            print("Correo: ", row[1])
            print("Contraseña: ", row[2])
            print("\n")


    elif op == '0':
        break
