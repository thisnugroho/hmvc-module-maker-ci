#!/usr/bin/env python3
import sys,os
####################### Default Config #############################
path                = "YOUR_PATH"                                  #
controller          = "controller"                                 #
views               = "views"                                      #
args                = sys.argv                                     #
separator           = "/" if sys.platform == 'linux' else "\\"     #
name                = args[2]                                      #
command             = args[1]                                      #
capitalize          = lambda s: s[:1].lower() + s[1:] if s else '' #
controller_name     = capitalize(name)                             #
####################################################################
controller_content = """<?php
defined('BASEPATH') or exit('No Direct Script Access Allowed');

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
        print("created\n\n")
        # End module

        # Start controller
        print("creating controller...\n")
        os.mkdir(path+name.lower() + separator + controller)
        f=open(path+name.lower() + separator + controller + separator + controller_name + ".php", "w+")
        f.write(controller_content)
        f.close()
        # Controller end

        # Start Views
        print("creating views...\n")
        os.mkdir(path+name.lower() + separator + views)
        f=open(path+name.lower() + separator + views + separator + "V_"+ name.lower() + ".php", "w+")
        f.write("<?php")
        f.close()

    except FileExistsError:
        print(name+  " is already exists")
