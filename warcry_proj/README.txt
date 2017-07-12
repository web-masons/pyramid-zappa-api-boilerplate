warcry_proj README
==================

Getting Started
---------------

- Login to Vagrant
* vagrant up
* vagrant ssh

- Ensure the bootstrap script is run to configure and install all required packages
* sudo script/bootstrap vagrant

- Install Pyramid
* easy_install pyramid

- Create the project scaffold in pyramid
*pcreate -s battleCry warcry_proj
*python setup.py develop
*initialize_warcry_proj_db development.ini
*pserve development.ini

