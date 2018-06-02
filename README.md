# selenium

Selenium tests for `python.org`. 

Tests automation with TestLink.


## Run Selenium tests

Install geckodriver:
```bash
https://github.com/mozilla/geckodriver/releases
```

Add to the PATH: `export PATH=$PATH:/path/to/directory/of/downloaded/executable/`

Preferable path: `/usr/local/bin`


## Managing TestLink

Setup tutorial.

### VM

Download
```url
https://bitnami.com/stack/testlink/virtual-machine
```

Log in with default `bitnami`/`bitnami`.


### Configuration file

```bash
$ vim /opt/bitnami/apps/testlink/htdocs/config.inc.php 
```

```
$tlCfg->api->enabled = TRUE;
...
$tlCfg->exec_cfg->enable_test_automation = ENABLED; 
```

### Start TestLink

```bash
$ sudo /opt/bitnami/ctlscript.sh start
```

Check your IP address:
```bash
$ sudo ifconfig
```

Type the address in your browser to access login page:
```url
192.168.8.134/login.php
```

Enter:
>Login: user
>Password: ybrI6m4eODIX


### Create Test Project

For this project it is:
>Name: Selenium
>Prefix: SE
>Project description: Test cases for web page 'python.org'

The rest is as default.


### Create Test Suite

In `Test Specification` select the new Test Project in the tree view, 
then hit toothed wheel (settings) and add button.


### Create Test Case

Go to `Test Specification` tab, then fill `Filters`.

>Test Case ID: Case
>Test title: First test case


### Create Test Plan

(tab) Project > Test Plan Management > (button) Create

>Name: Plan

Check boxes `public` and `active`.


### Create Test Build

(tab) Project > Builds / Releases > (button) Create

>Name: Build


### Generate personal API access key

My Settings > API Interface > (button) Generate a new key

Copy it to `run_test_module.py` along with proper IP address
and provide new properties (IDs etc.) for created test.


### Configure your project

```bash
source venv/bin/activate
pip install TestLink-API-Python-client 
```


#### Useful links:

- [tutorialspoint](https://www.tutorialspoint.com/testlink/testlink_add_project.htm)
