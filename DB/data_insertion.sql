USE MANAGE_IT

EXEC IDIOMAS_CREATE 'Inglés'
EXEC IDIOMAS_CREATE 'Español'
EXEC IDIOMAS_CREATE 'Portugues'

EXEC USUARIOS_CREATE 'gysmoy', 'gysmoy@gmail.com',
    '96087c07b838bd8f4192c1bd369625b1f52553a02da38c220076006ab99019dc',
    '72941485', 'Gamboa', 'Palomino', 'Carlos Manuel', 'M', '2001-06-15',
    'IDI00002'
EXEC USUARIOS_CREATE 'yopirata', 'yoninantearce@gmail.com',
    'fae3698dd81b9d8c075e051947bc7dbe3f60c61adb696b5dfb7e17aec1fddb2f',
    '71895392', 'Infante', 'Arce', 'Yon Gerli', 'M', '2003-01-01',
    'IDI00002'
EXEC USUARIOS_CREATE 'jadejadiel', 'jabeker.espinoza.daniel@gmail.com',
    '637e3f7a12d484b2a2b9f0f4146049e88ed7144e4f9cc3bb8975e14406c12383',
    '71126574', 'Espinoza', 'Encarnación', 'Jabeker Daniel', 'M', '2000-09-05',
    'IDI00001'

SELECT * FROM IDIOMAS
SELECT * FROM USUARIOS