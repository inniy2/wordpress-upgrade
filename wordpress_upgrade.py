#!/usr/bin/python

import subprocess

out = subprocess.check_output(["echo", "cp debian_upgrade.cnf /etc/mysql/"])
print("note = " + out)
subprocess.call("cp debian_upgrade.cnf /etc/mysql/", shell=True)

out = subprocess.check_output(["echo", "apt-get -y purge mysql-server"])
print("note = " + out)
subprocess.call("apt-get -y purge mysql-server", shell=True)

out = subprocess.check_output(["echo", "apt-get -y autoremove"])
print("note = " + out)
subprocess.call("apt-get -y autoremove", shell=True)

out = subprocess.check_output(["echo", "rm -rf  /etc/apt/sources.list.d/mysql.list"])
print("note = " + out)
subprocess.call("rm -rf  /etc/apt/sources.list.d/mysql.list", shell=True)

out = subprocess.check_output(["echo", "wget https://repo.percona.com/apt/percona-release_0.1-6.$(lsb_release -sc)_all.deb"])
print("note = " + out)
subprocess.call("wget https://repo.percona.com/apt/percona-release_0.1-6.$(lsb_release -sc)_all.deb", shell=True)

out = subprocess.check_output(["echo", "dpkg -i percona-release_0.1-6.$(lsb_release -sc)_all.deb"])
print("note = " + out)
subprocess.call("dpkg -i percona-release_0.1-6.$(lsb_release -sc)_all.deb", shell=True)

out = subprocess.check_output(["echo", "apt-get -y update "])
print("note = " + out)
subprocess.call("apt-get -y update", shell=True)

out = subprocess.check_output(["echo", "apt-get -y upgrade "])
print("note = " + out)
subprocess.call("apt-get -y upgrade", shell=True)

out = subprocess.check_output(["echo", "apt-get -y install percona-server-server-5.7"])
print("note = " + out)
subprocess.call("apt-get -y install percona-server-server-5.7", shell=True)

out = subprocess.check_output(["echo", "mysql_upgrade --defaults-file=/etc/mysql/debian_upgrade.cnf"])
print("note = " + out)
subprocess.call("mysql_upgrade --defaults-file=/etc/mysql/debian_upgrade.cnf", shell=True)

out = subprocess.check_output(["echo", "apt -y install python-pip"])
print("note = " + out)
subprocess.call("apt -y install python-pip", shell=True)

out = subprocess.check_output(["echo", "pip install mysql-connector"])
print("note = " + out)
subprocess.call("pip install mysql-connector", shell=True)

import alter_tables

