#!/usr/bin/env python
'''
liquibase-drift-reports - config file

A quick python setup for automating diff reports (aka drift reports) using the new Liquibase Pro diff as json capability
'''

## ===================================================================
## LICENSE AND CREDITS
## This app/collection of scripts at https://github.com/mariochampion/liquibase-drift-reports
## released under the Apache License 2.0. (http://www.apache.org/licenses/LICENSE-2.0)
##
## Latest Liquibase Release: https://github.com/liquibase/liquibase/releases
## Contribute code to Liquibase: https://github.com/liquibase/liquibase
##
## please open issues and pull requests,
## thanks and always remember: this robot loves you. 
## boop boop!
## ===================================================================



################################# love your library(s)
import os, sys, subprocess, time
import drift_reports_conf as cfg

#################################
## make a dir, if it doesn't exist
def findormakedir(path_to_thisdir, msg="create dir"):
  
  #make if needed
  if not os.path.exists(path_to_thisdir):
    os.makedirs(path_to_thisdir)
    print (msg + ":",cfg.color.cyan, path_to_thisdir, cfg.color.white)
    print
    status = True
  else:
    if os.path.exists(path_to_thisdir):
      print("Good news!\t",cfg.color.cyan, path_to_thisdir + " exists!", cfg.color.white )
      status = True
    else:
      print("Sorry no dir created:" + path_to_thisdir)
      status = False
  
  return status


#################################	 
## read some dbs to diff info from a local file

def builddriftreports(localfile):
   
  localfile_path = cfg.base_localpath +"/"+ localfile
  print("Database list: ",cfg.color.cyan, localfile_path)
  
  with open(localfile_path, "r") as thisfile:
    for line in thisfile:

        print (cfg.color.white)
        print("----------------------------------------------------------")
        print()

        ## this is the target database (the url key in liquibase.properties)   
        urldbname = line.strip() 
      
        ## provide a little feedback/update to user
        print (cfg.color.white, "ref/model db:\t", cfg.color.cyan, cfg.refdbname)
        print (cfg.color.white, "target db:\t", cfg.color.cyan, urldbname)
        print (cfg.color.white)

        ## build the diff command
        diffcmd = build_diffcmd(urldbname)

        ## tell the people what is about to happen  
        print("LBPRO command to run:")
        print(cfg.color.cyan + diffcmd)
        print(cfg.color.white)


        #### now for to be doing the real works
        #subprocess.call(diffcmd, shell=True)

   
  return



###################################
def build_diffcmd(urldbname):
  ## liquibase 
  ## --url=jdbc:dbtype://subdomain.domain.com:port/targetdbname
  ## --referenceURL= jdbc: dbtype://subdomain.domain.com:port/refdbname?autoReconnect=true
  ## --outputFile=drift_reports/yyyymmdd-hhmmss/drift-refdb-refdbname-to-targetdbname.json
  ## diff --format=json

  diffcmd = cfg.app +" "+ cfg.urldb+ cfg.connection_string + cfg.targethost + "/" +urldbname + " " +cfg.refurl + cfg.refconnstring + " " +cfg.file + cfg. driftreports_dir +"/"+ tstamp + "/drift-refdb-" + cfg. refdbname + "-to-" + urldbname + cfg.defext + " " + cfg.appcmd

  return diffcmd





###################################
## do some setup work

## make a root dir for all drift reports
findormakedir(cfg.driftreports_dir, "Root for Drift Reports")


## make a timestamp dir inside the root dir
ts = time.gmtime()
tstamp = time.strftime("%Y%m%d-%H%M%S", ts)

if os.path.exists(cfg.driftreports_dir):
  findormakedir(cfg.driftreports_dir+"/"+tstamp, "Today's Reports")
else:
  print (cfg.color.red)  
  print("ERROR2: " + cfg.driftreports_dir + " not found! Stopping.")
  print (cfg.color.white)  
  sys.exit(1)
  


###################################
## now do some main things


## build the reports please
if os.path.exists(cfg.driftreports_dir+"/"+tstamp):
  builddriftreports(cfg.localfile)
else:
  print (cfg.color.red)   
  print("ERROR: timestamp dir " + cfg.driftreports_dir + "/" + tstamp + " not found! Stopping.")
  print (cfg.color.white) 
  sys.exit(1)








