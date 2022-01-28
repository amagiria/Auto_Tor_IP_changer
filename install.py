import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/rr')
    run('cp autoTOR.py /usr/share/rr/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/rr/autoTOR.py "$@"')
    with open('/usr/bin/rr','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/rr & chmod +x /usr/share/rr/autoTOR.py')
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42mrr\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/rr ')
    run('rm /usr/bin/rr ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
