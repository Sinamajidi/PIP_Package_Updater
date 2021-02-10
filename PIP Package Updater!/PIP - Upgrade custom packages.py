from subprocess import getoutput
from re import findall


pkgs = str(input('''Enter the Package(s) name that you want to Upgrade (separate them by | ) :
'''))


pkg_list = getoutput('python -m pip freeze').split('\n')
new_pkg = []
for i in pkg_list:
    findall(r"^(.*)\=\=.*", str(i))
    new = findall(r"^(.*)\=\=.*", str(i))[0]
    new_pkg.append(str(new))

selected_pkg = []

if '|' in pkgs:
    pkgs = pkgs.split('|')
    for package in pkgs:
        if not package in new_pkg:
            print('Package ' + str(package) + ' Not Found in PIP List :(')
            exit()
        else:
            selected_pkg.append(str(package))
else:
    if pkgs in new_pkg:
        selected_pkg.append(str(pkgs))
    else:
        print('Your Selected Package Didn\'t Found in PIP List :(')
        exit()

if len(selected_pkg) > 1:

    for x in selected_pkg:
        print('\n')
        print('Upgrading ' + str(selected_pkg.index(x)+1) +
              ' of ' + str(len(selected_pkg)) + '\n')
        print(getoutput('python -m pip install '+str(x)+' --upgrade'))
        print('\n')
        print('=================================================\n')

else:
    for x in selected_pkg:
        print('\n')
        print('Upgrading ' + str(x) + ' ... ' + '\n')
        print(getoutput('python -m pip install '+str(x)+' --upgrade'))
        print('\n')
        print('=================================================\n')

print('Done!')
