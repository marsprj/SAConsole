#!/bin/sh

echo 'install tcsh'
if rpm -qa | grep tcsh
then
	echo 'tcsh alread installed'
else
	yum install tcsh.i686 -y
fi

echo 'install wxPython'
if rpm -qa | grep wxPython
then
	echo 'wxPython alread installed'
else
	yum install wxPython.i686 -y
fi

