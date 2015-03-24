# k8svag
Kubernetes Vagrant Provisioning and management script

```
pip install k8svag
k8svag createproject myproject
k8svag up myproject
``

###usage
```bash
Vagrant cluster management

Usage:
    cryptobox vagrant [options] [--] <command> [<args>...]

Options:
    -h --help           Show this screen.
    -p --parallel           Execute commands in parallel (ansible style).
    -v --verbose            Verbose mode.
    -f --force              Do not ask for confirmation
    -w --wait=<ws>          Wait <ws> seconds between commands.
    -d --workingdir=<wrkd>  Directory to execute commands in, default is current working dir.

Commands:
    check                   Ansible-playbook dry-run
    coreostoken             Print coreos token to stdout
    clustercommand          Execute command on cluster
    createproject [<name>]  Create a Coreos Kubernetes cluster in local directory
    destroy                 Destroy vagrant cluster (vagrant destroy -f)
    halt [<name>]           Halt vagrant cluster (vagrant halt)
    localizemachine         Apply specific configuration for the host-machine
    ansibleplaybook         Provision server with ansible-playbook (server:playbook)
    reload                  Reload cluster (vagrant reload)
    replacecloudconfig      Replace all coreos-cloudconfigs and reboot
    ssh                     Make ssh connection into specific machine
    status                  Status of cluster or machine
    up [<name>]             Bring cluster up
    kubernetes              Kubernetes commands
```

###pip
[https://pypi.python.org/pypi/k8svag!](https://pypi.python.org/pypi/k8svag)

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