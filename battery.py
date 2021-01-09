from progress.bar import Bar
import os,time

niv = 95
rpt = 10
ckt = 5

#Extraer el nivel de la bateria y devuelve true o false si el nivel es igual al establecido en la variable niv
def status():
    os.system('termux-battery-status > .bat.tmp')
    get = open('.bat.tmp', 'r')
    size = get.read().split(':')[2].split(',')[0].split(' ')[1]

    return size

#Emision de alertas sonoras y vibracion
def sound():
    i=1
    slp=10
    vel=1

    try:
        while i <= rpt:
            sys('termux-tts-speak -r ' + str(vel) + ' "Nivel de carga al ' + str(status()) + ' porciento"')
            sys('termux-vibrate -f')
            i+=1
            time.sleep(slp)
            slp-=1
    except KeyboardInterrupt:
        play('/storage/emulated/0/Download/trabar-carro-alarma-auto-.mp3')
        sys('cls')
        print('\nAlarma detenida: code 0')


#reproduccion de contenido multimedia
def play(a):
    os.system('termux-media-player play ' + a)

#Ejecucion de comandos externos
def sys(a):
    os.system(a)

#Revisa y devielve el estatus de la carga
def connected():
    sys('termux-battery-status > .sbat.tmp')
    get = open('.sbat.tmp','r') 
    snip = get.read().split('"')[13]

    return snip

#devuelve el volumen actual
def vol():
    sys('termux-volume > .vbat.tmp')
    get = open('.vbat.tmp','r')
    vmus = get.read().split('"')[30].split(' ')[1].split(',')[0]
    return vmus
    


def main():
    al = 0
    bar = Bar('Carga: ',max=100)
    try:
        while int(status()) <= niv:
            if connected() == "DISCHARGING":
                print('\nCargador desconectado: code 1')
                print('\nSonara la alarma...')

                time.sleep(4)

                if int(vol()) != 30:
                    sys('termux-volume music 30')

                while al <= 5:
                    play('/storage/emulated/0/Download/alarma-de-evacuacin-evacuacion.mp3')
                    time.sleep(7)
                    al+=1

                break
            bar.goto(int(status()))
            sys('termux-notification -t Carga -c ' + str(status()) + '% -id=123')
            time.sleep(ckt)
        else:
            #sys('termux-telephony-call 5581532662')
            bar.next()
            bar.finish()
            sound()
    except KeyboardInterrupt:
        bar.finish()
        play('/storage/emulated/0/Download/trabar-carro-alarma-auto-.mp3')
        sys('cls')
        print('\nAlarma desactivada: code 0')


try:
    while connected() == "DISCHARGING":
        sys('cls')
        print('Conecte el cargador...')
        time.sleep(3)
    else:
        play('/storage/emulated/0/Download/trabar-carro-alarma-auto-.mp3')
        print(' •La alarma sonara cuando <= ' + str(niv) + '% de carga.')
        main()
except KeyboardInterrupt:
    sys('cls')
    print('\nAlarma cancelada: code 0')

