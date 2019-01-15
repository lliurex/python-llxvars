# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
import os
import subprocess


setup(  name             = "python-llxvars",
        version          = "0.1",
        author           = "Hector Garcia Huerta",
        author_email     = "lliurex_devel1@edu.gva.es",
        url              = "http://lliurex.net/",
        package_dir      = {'': 'src'},
        packages         = ['lliurex.variables'],
     )


