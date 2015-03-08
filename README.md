# k8svp
Kubernetes Vagrant Provisioning and management script

###usage
```bash
Usage: main.py [-h] [-s [SSH [SSH ...]]] [-c [COMMAND [COMMAND ...]]]
               [-f [SSHCONFIG [SSHCONFIG ...]]] [-u UP] [-d] [-k HALT]
               [-q PROVISION] [-r [RELOAD [RELOAD ...]]] [-a] [-t] [-w WAIT]
               [-l [LOCALIZEMACHINE [LOCALIZEMACHINE ...]]] [-p] [-x]

Vagrant controller, argument 'all' is whole cluster

optional arguments:
  -h, --help            show this help message and exit
  -s [SSH [SSH ...]], --ssh [SSH [SSH ...]]
                        vagrant ssh
  -c [COMMAND [COMMAND ...]], --command [COMMAND [COMMAND ...]]
                        execute command on cluster
  -f [SSHCONFIG [SSHCONFIG ...]], --status [SSHCONFIG [SSHCONFIG ...]]
                        status of cluster or when name is given print config
                        of ssh connections
  -u UP, --up UP        vagrant up
  -d, --destroy         vagrant destroy -f
  -k HALT, --halt HALT  vagrant halt
  -q PROVISION, --provision PROVISION
                        provision server with playbook (server:playbook)
  -r [RELOAD [RELOAD ...]], --reload [RELOAD [RELOAD ...]]
                        vagrant reload
  -a, --replacecloudconfig
                        replacecloudconfigs and reboot
  -t, --token           print a new token
  -w WAIT, --wait WAIT  wait between server (-1 == enter)
  -l [LOCALIZEMACHINE [LOCALIZEMACHINE ...]], --localizemachine [LOCALIZEMACHINE [LOCALIZEMACHINE ...]]
                        apply specific configuration for a machine
  -p, --parallel        parallel execution
  -x, --check           ansible-playbook dry-run
```

###pip
(https://pypi.python.org/pypi/k8svp)[https://pypi.python.org/pypi/k8svp]

```
"Programming Language :: Python",
"Programming Language :: Python :: 3",
"Development Status :: 4 - Beta ",
"Intended Audience :: Developers",
"License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
"Operating System :: POSIX",
"Topic :: Software Development :: Libraries :: Python Modules",
"Topic :: System :: Clustering",
"Topic :: System :: Distributed Computing",
"Topic :: System",
```