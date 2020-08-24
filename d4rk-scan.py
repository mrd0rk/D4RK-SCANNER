import urllib
from socket import *
import time
import subprocess
def ipscan():
    logo = """
             _/  _/  _/              _/      
        _/_/_/  _/  _/    _/  _/_/  _/  _/   
     _/    _/  _/_/_/_/  _/_/      _/_/      
    _/    _/      _/    _/        _/  _/     
     _/_/_/      _/    _/        _/    _/    




         _/_/_/    _/_/_/    _/_/_/  _/_/_/    _/_/_/      _/_/    _/  _/_/   
      _/_/      _/        _/    _/  _/    _/  _/    _/  _/_/_/_/  _/_/        
         _/_/  _/        _/    _/  _/    _/  _/    _/  _/        _/           
    _/_/_/      _/_/_/    _/_/_/  _/    _/  _/    _/    _/_/_/  _/            

                                                                  ~* by Mr-D4r|< 
                                {ip scanner}                                           """
    print(logo)

    startTime = time.time()

    if __name__ == '__main__':
        target = input('*Enter the host to be scanned:*: ')
        t_IP = gethostbyname(target)
        print('* Starting scan on host:*: ', t_IP)

        for i in range(50, 500):
            s = socket(AF_INET, SOCK_STREAM)

            conn = s.connect_ex((t_IP, i))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
    print('Time taken:', time.time() - startTime)

def mrad():
    logo = """
             _/  _/  _/              _/      
        _/_/_/  _/  _/    _/  _/_/  _/  _/   
     _/    _/  _/_/_/_/  _/_/      _/_/      
    _/    _/      _/    _/        _/  _/     
     _/_/_/      _/    _/        _/    _/    




         _/_/_/    _/_/_/    _/_/_/  _/_/_/    _/_/_/      _/_/    _/  _/_/   
      _/_/      _/        _/    _/  _/    _/  _/    _/  _/_/_/_/  _/_/        
         _/_/  _/        _/    _/  _/    _/  _/    _/  _/        _/           
    _/_/_/      _/_/_/    _/_/_/  _/    _/  _/    _/    _/_/_/  _/            

                                                                  ~* by Mr-D4r|<  """
    print(logo)
    import subprocess
    ip = input("* ENTER AN IP ADDRESS:*:")
    for ping in range(200, 225):
        address = ip + str(ping)
        res = subprocess.call(['ping', '-c', '1', address])
        if res == 0:
            print("trying to", address, "OK")
        elif res == 2:
            print("no response from", address)
        else:
            print("trying to", address, "failed!")


logo = """
         _/  _/  _/              _/      
    _/_/_/  _/  _/    _/  _/_/  _/  _/   
 _/    _/  _/_/_/_/  _/_/      _/_/      
_/    _/      _/    _/        _/  _/     
 _/_/_/      _/    _/        _/    _/    




     _/_/_/    _/_/_/    _/_/_/  _/_/_/    _/_/_/      _/_/    _/  _/_/   
  _/_/      _/        _/    _/  _/    _/  _/    _/  _/_/_/_/  _/_/        
     _/_/  _/        _/    _/  _/    _/  _/    _/  _/        _/           
_/_/_/      _/_/_/    _/_/_/  _/    _/  _/    _/    _/_/_/  _/            

                                                              ~* by Mr-D4r|<  """
print(logo)

print("==========================================================================")
print("                             ~~ D4RK SCAN ~~                              ")
print("==========================================================================")
print("         1 ==> IP SCAN                                                    ")
print("                                                                          ")
print("         2 ==> YOUR RANGE ACTIVE DEVICE                                   ")
print("==========================================================================")
opt = int(input("*Enter your option:*:"))
if opt == 1 :
    ipscan()
if opt == 2 :
    mrad()
else : print("invalid option")
