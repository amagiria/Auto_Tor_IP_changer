import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/accgen')
    run('cp autoTOR.py /usr/share/accgen/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/accgen/autoTOR.py "$@"')
    with open('/usr/bin/accgen','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/accgen & chmod +x /usr/share/accgen/autoTOR.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maccgen\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/accgen ')
    run('rm /usr/bin/accgen ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
