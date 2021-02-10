from subprocess import getoutput
from re import findall

pkg_list = getoutput('python -m pip freeze')

pkg_list = pkg_list.split('\n')


new_pkg = []
for i in pkg_list:
    findall(r"^(.*)\=\=.*", str(i))
    new = findall(r"^(.*)==.*", str(i))[0]
    new_pkg.append(new)


for i in new_pkg:
    print('\n')
    print('Package ' + str(new_pkg.index(i)+1) +
          ' of ' + str(len(new_pkg)) + '\n')
    print(getoutput('python -m pip install '+str(i)+' --upgrade'))
    print('\n')
    print('=================================================\n')


print('Done!')
