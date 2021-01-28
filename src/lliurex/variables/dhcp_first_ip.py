#from string import maketrans;

def init(args=None):
    DEBUG=0;
    try:
        network = args['NETWORK']
        mask = args['MASK']
    except:
        network = "10.10.0.30"
        mask = 22
    
    global tpc_reserv;
    try:
        tpc_reserv = args['RESERVATION']
    except:
        tpc_reserv = 5;
    

    # pasamos ip -> binario
    netbinary=to_bin(network);
    # mas alla de la mascara, sustituimos por 0's
    netbinary=netbinary[:mask]+netbinary[mask:].translate(str.maketrans('1','0'));
    # generamos wildcard como 0's y mas alla de la mascara 1's
    wildcard='';
    for i in range(mask,32):
        wildcard+='1';
    wildcard=wildcard.zfill(32);
    # para generar binario de la mascara, invertimos wildcard
    maskbinary=wildcard.translate(str.maketrans('10','01'));
    # calculamos numero maximo de host en la red como el valor del numero (binario) de la mascara -2 host (dir red, dir broadcast)
    total_hosts=int(wildcard,2)+1-2;
    # calculo de direcciones reservadas en funcion del size de la red
    reservas=calc_reservas(total_hosts);
    num_hosts=total_hosts-reservas;
    # el primer host es el siguiente despues del valor de red mas las reservas, 
    first_host=bin(int(netbinary,2)+1+reservas)[2:].zfill(32);
    
    # calculo de direccion broadcast mediante un OR entre la direccion de red y la wildcard
    broadcast=bin(int(netbinary,2) | int(wildcard,2))[2:].zfill(32);
    # el ultimo host calculado como uno menos de el valor de broadcast 
    last_host=bin(int(broadcast,2)-1)[2:].zfill(32);
    
    if DEBUG:
        print ('{0:25s} {1:20s}'.format('Address/Mask: ',network+'/'+str(mask)))
        print ('{0:25s} {1:20s}'.format('Num Hosts: ',str(num_hosts)+' + Reservas:('+str(reservas)+') = TOTAL:'+str(total_hosts)))
        print ('{0:25s} {1:20s}/{2:35s} {3:20}'.format('Network/Mask (binary):',netbinary,maskbinary,to_ip(netbinary)+'/'+str(mask)))
        print ('{0:25s} {1:20s} {2:35s}'.format('Wildcard     (binary/ip):',wildcard,to_ip(wildcard)))
        print ('{0:25s} {1:20s} {2:35s}'.format('First Host   (binary/ip):',first_host,to_ip(first_host)))
        print ('{0:25s} {1:20s} {2:35s}'.format('Last Host    (binary/ip):',last_host,to_ip(last_host)))   
        print ('{0:25s} {1:20s} {2:35s}'.format('Broadcast    (binary/ip):',broadcast,to_ip(broadcast)))

    return to_ip(first_host)
#def init

def to_ip(ipbin):
    return str(int(ipbin[:8],2))+'.'+str(int(ipbin[8:16],2))+'.'+str(int(ipbin[16:24],2))+'.'+str(int(ipbin[24:32],2));
#def to_ip

def to_bin(ip):
    net_tuple=ip.split('.');
    ipbin='';
    for i in range(0,4):
        ipbin += str(bin(int(net_tuple[i])))[2:].zfill(8);
    return ipbin;
#def to_bin

def calc_reservas(num):
    #calcula el numero de reservas segun el rango de red 5%
    global tpc_reserv
    return num*tpc_reserv/100
#def calc_reservas

#init({'NETWORK':"10.2.1.0",'MASK':24})
#init({'NETWORK':"10.2.1.0",'MASK':24,'RESERVATION':5})
