#!/usr/bin/python

import subprocess
import os
import platform

if int(platform.release().split('.')[0]) < 13: # Mavericks
        raise Exception("On-demand Xcode Command Line Tools are not available in OS X below 10.9")

pkgs = [
	'"DTCommandLineTools" IN tags'
]

#os.environ['JAVA_INSTALL_ON_DEMAND'] = '1'
open('/tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress','a').close()

for pkg in pkgs:
	subprocess.call(['/usr/bin/python', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'predicate_installer.py'), pkg])
