#!/usr/bin/env python
'''
liquibase-drift-reports - config file

A quick python setup for automating diff reports (aka drift reports) using the new Liquibase Pro diff as JSON capability
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



################### core configs


## this is the master dir for subsequent timestamped drift report dirs and .json files
driftreports_dir = "drift_reports"

## setup the vars for the command line call
app = "liquibase"
connection_string = "jdbc:mysql://"	#### CHANGE THIS
targethost = "<sub.domain.tld:3306>"	#### CHANGE THIS
urldb = "--url="
file="--outputFile="
appcmd = "diff --format=json"
defext = ".json"



################### this is the master/model/reference database, aka referenceURL
refurl = "--referenceUrl="
refdbname = "<refdbname>"		#### CHANGE THIS
refconnstring = "jdbc:mysql://<sub.domain.tld:3306>/"+ refdbname +"?autoReconnect=true"	#### CHANGE THIS
 

################### get list of dbs to diff against referenceUrl or 'refurl' 
## this txt file contains one db name per line, used to complete the "--url" param
base_localpath = "."
localfile = "drift_dblist.txt"	#### CHANGE THIS







################### some useful shortcuts for coloring console output

# pinched and tweaked from https://github.com/impshum/Multi-Quote/blob/master/run.py
class color:
  white, cyan, blue, red, green, yellow, magenta, black, gray, bold = '\033[0m', '\033[96m','\033[94m', '\033[91m','\033[92m','\033[93m','\033[95m', '\033[30m', '\033[30m', "\033[1m"  

# maybe add bks, bolds, etc from https://godoc.org/github.com/whitedevops/colors
class bkcolor:
  resetall = "\033[0m"
  default      = "\033[49m"
  black        = "\033[40m"
  red          = "\033[41m"
  green        = "\033[42m"
  yellow       = "\033[43m"
  blue         = "\033[44m"
  magenta      = "\033[45m"
  cyan         = "\033[46m"
  lightgray    = "\033[47m"
  darkgray     = "\033[100m"
  lightred     = "\033[101m"
  lightgreen   = "\033[102m"
  lightyellow  = "\033[103m"
  lightblue    = "\033[104m"
  lightmagenta = "\033[105m"
  lightcyan    = "\033[106m"
  white        = "\033[107m"



