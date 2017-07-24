PyZAPI README
==================

Getting Started
---------------

Please ensure you are in a vagrant environment to deploy your project
--Vagrant destroy - Destroys your current vagrant if you so require
--Vagrant up - Starts your Vagrant 
--Vagrant provision - Provisions vagrant

--vagrant ssh - Logs you into your vagrant environment


Afetr you have run vagrant provision, the virtualenv should of been created in home/vagrant/python3.6/

--cd /home/vagrant/python3.6/

Start your virtualenv
--source bin/activate

Setup your AWS credentials for Zappa
--aws configure
get key and secret from aws (create a user under the IAM and copy the keys)

Enter the folder where the project has been created
--cd /vagrant/

install pyramid / zappa
--pip3 install pyramid
--pip3 install zappa

create your project scaffold (already done for this project)
--pcreate -s alchemy PyZAPI
--cd PyZAPI

Setup your pyramid
--python3 setup.py develop Or pip install -e .

Update the ini files with your database credentials
--vi development.ini / production.ini
edit the sqlalchemy.url with your database connection details
Setup your Database
--initialize_PyZAPI_db development.ini

Setup Zappa
--zappa init
Make sure to set the runtime to python3.6
"runtime": "python3.6"

deploy your zappa enviroment
--zappa deploy 
--zappa update (if enviroment exists)

Start pyramid (if required)
--pserve development.ini --reload

