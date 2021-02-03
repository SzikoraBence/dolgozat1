import os
import time
def main():
    while True:
        felhsz = input ("Add meg a felhasználót: ")
        jelszo = input ("Add meg a jelszót: ")

        if felhsz == 'Sziko' and jelszo == 'sziko1234':
            time.sleep(1)
            print ("Sikerült be lépni")
            logged()

        else:
            print ("Valami nem jó :c")

def logged():
    time.sleep(1)
   
main()