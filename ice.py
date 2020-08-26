#!/usr/bin/env python3

import sys,os

separator        = "/" if sys.platform == 'linux' else "\\"     
back_path        = os.path.dirname(os.path.realpath(__file__)) + separator + 'admin' + separator + 'application' + separator +'modules'+ separator
front_path       = os.path.dirname(os.path.realpath(__file__)) + separator + 'application' + separator + 'modules' + separator
controller       = "controllers"                                
views            = "views"                                      
args             = sys.argv                                     

try:                                                               
    command             = args[1]
    name                = args[2]                                  
    tipe                = args[3]                                  
except IndexError:                                                 
    print("wrong command,please use py ice.py -cm (name)")          
    sys.exit(0)                                                    

controller_name     = name[0].upper() + name[1:]                                 
controller_content = """<?php
defined('BASEPATH') or exit('No Direct Script Access Allowed');
class {0} extends MX_Controller {{

    public function __construct() {{
        parent::__construct();

    }}
    public function index() {{

    }}

    public function save() {{

    }}

    public function delete() {{
        
    }}
}}
""".format(name[0].upper() + name[1:])

if tipe == 'back':
    path = back_path
else:
    path = front_path


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
        f=open(path+name.lower() + separator + views + separator + "V_index" + ".php", "w+")
        f.close()
        print("Views Created")

    except FileExistsError:
        print(name+  " is already exists")
else:
    print("that command doesnt exists")
