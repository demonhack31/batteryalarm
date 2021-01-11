# batteryalarm
Script python para avisarte cuando tu celular ha llegado a un porcentaje de bateria, de igual manera sonara una alarma si el cargador es desconectado.

Actualmente ya no es recomendable instalar muchas aplicaciones en tu teléfono por la razón de que la mayoría implementan publicidad que terminad pagando conbtus datos móviles.

Por esto decidí implementar mi propia alarma escrita en python ayudándonos con siertos comandos en el sistema.

a) Para comenzar a usar esta alarma es necesario que previo a la des 44 ga del script descargues/instales los siguientes requerimientos:
En termux:
1. pkg install python
2. pip install progress.bar

En Play Store:
1. Termux:API
*Se recomienda usar Termux:Widget

b) Si descargaste Termux:Widget sigue los siguientes pasos, de lo contrario ve al siguiente paso:
1. Abre termux y teclea los siguientes comandos:
2. cd .shorcuts
3. vim battery.sh

Contenido de battery.sh
cd ~ #Ruta del directorio en donde descargamos battery.py
python battery.py

Presionamos la tecla ESC y después escribimos :wq

Ahora ve a la pantalla de inicio de tu teléfono agrega el witget llamado "Termux Witget". Actualiza y veras tu script battery.sh

c) Por último si no instalaste el shorcut vas a tener que escribir "python battery.py" si lo tienes solo presiona el nombre de tu script.
Solo haría falta conectar tu teléfono.

