#!/usr/bin/env python3

import sys,os
####################### Default Config #############################
path                = "C:\wamp64\www\crudCI\\"                     #
controller          = "controllers"                                #
views               = "views"                                      #
args                = sys.argv                                     #
separator           = "/" if sys.platform == 'linux' else "\\"     #
try:                                                               #
    name                = args[2]                                  #
    command             = args[1]                                  #
except IndexError:                                                 #
    print("wrong command,pleas use py ice.py -cm (name)")          #
    sys.exit(0)                                                    #
controller_name     = name.title()                                 #
####################################################################
controller_content = """<?php
defined('BASEPATH') or exit('No Direct Script Access Allowedi');

class {0} extends MX_Controller {{
    public function __construct() {{
        parent::__construct();
    }}
    public function index() {{

    }}
}}
""".format(name)
if command == "-cm":
    try:
        # Start module
        print("creating module...\n")
        os.mkdir(path+name.lower())
        print("Module Created\n")
        # End module

        # Start controller
        print("creating controller...\n")
        os.mkdir(path+name.lower() + separator + controller)
        f=open(path+name.lower() + separator + controller + separator + controller_name + ".php", "w+")
        f.write(controller_content)
        f.close()
        print("Controller Created\n")
        # Controller end

        # Start Views
        print("creating views...\n")
        os.mkdir(path+name.lower() + separator + views)
        f=open(path+name.lower() + separator + views + separator + "V_"+ name.lower() + ".php", "w+")
        f.write("<?php")
        f.close()
        print("Views Created")

    except FileExistsError:
        print(name+  " is already exists")
else:
    print("that command doesnt exists")

