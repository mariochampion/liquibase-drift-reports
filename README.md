# liquibase-drift-reports
## A quick python setup for automating diff reports (aka drift reports) using the new Liquibase Pro diff as json capability


## Purpose & Goal
Liquibase Pro can help you automate drift detection at scale in your database schemas with a new structured and machine readable diff output as json. This additional capability is an Pro extension to the existing community command "diff", and is invoked with a new --format option.  
`$> liquibase diff --format=json`

This outputs a JSON structured object listing the differences between two databases (as configured in your liquibase.properties or Maven POM file under the "url" and "referenceUrl" keys.) By default, the result is output to STDOUT, which provides you with maximum flexibility to pipe the result into other tools or a processing pipeline. You can also have the output delivered to a file, using the `"--outputFile=<filename>"` global parameter, as in  
`$> liquibase --outputFile=myfile.json diff --format=json `

Whether you choose STDOUT or a collection of files, you can then process this data to generate reports, to trigger actions, from alerts to diffChangeLogs, to updates, or whatever make sense for how you use Liquibase.




## Getting Started
1. cd to your Liquibase project, which is typically the dir where you have your liquibase.properties file and   
`git clone https://github.com/mariochampion/liquibase-drift-reports.git`

2. In my setup, I have kept some values in liquibase.properties, including username, password, referenceUsername, and referencePassword.


Your directories should look like this:
```
├── my_liquibase_project
|  ├── sql
|  |  ├── liquibase.properties
|  |  ├── my_sql_changelog.mysql.sql
|  |  ├── drift_dblist.txt
|  |  ├── drift_reports_conf.py
|  |  ├── drift_reports.py
|  |  ├── drift_reports (a generated directory on first run)
|  |  |  ├── <timestamp-dir> (a generated directory on every run)
|  |  |  |  ├── drift-refdb-db01-to-db02.json
|  |  |  |  ├── drift-refdb-db01-to-db05.json
|  |  |  |  ├── <and so on>

```


3. Configure `drift_reports_conf.py` for your usage. Pay most attention to where you store your 
* reference database
* list of target databases

4. Enjoy!

### Prerequisites

#### software
* Liquibase (<a href="https://liquibase.com/">https://liquibase.com/</a>) 
* Python3 (<a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>)
* Terminal/Command Line familiarity


#### permissions
* Internet Access
* File and directory creation permissions
* Optional: Create aliases in ~/.bash_profile (or equivalent)


## Installing

```
git clone https://github.com/mariochampion/liquibase-drift-reports.git
```

Et voila, you are ready to explore!

## Usage:
```
python drift_reports.py
```
#### As a shortcut, add an alias in your .bash_profile to launch it via alias 'drift_reports' at the command line:
```
nano ~/.bash_profile
```

Then add this line to your bash_profile and save
```
alias drift_reports="cd path/to/install/dir/;python drift_report.py"
```

Then you can launch it with 
```$> drift_reports```



## Contributing

I am very open to issues and pull requests. Looking for a place to start helping?<br>
https://github.com/mariochampion/liquibase-drift-reports

## Authors

* **Mario Champion** - *Initial work* - [mariochampion](https://github.com/mariochampion)

Contributions, Issues, and Pull requests Welcome!

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Liquibase Community
* StackExchange
* Python

## thanks and always remember: this robot loves you. 
## boop boop!