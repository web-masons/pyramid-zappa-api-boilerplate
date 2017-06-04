# -*- mode: ruby -*-
# vi: set ft=ruby :

# -*- mode: ruby -*-
# vi: set ft=ruby :

# README!
#
# IF you have cloned the bootstrap for your project, you will want to search/replace the following
# values for your new project.
#
# The name of the configuration node:
#   pyzappi-boilerplate
#
# The hostname of your Vagrant Box:
#   pyzappi
#
# The IP Address that Vagrant will put itself at for use with vagrant-hostmanager. You'll want to change these
# so that you don't end up with ip address space collisions on your local machine.
#   192.168.33.50
#
# The URL that vagrant-hostmanager will put in your hosts file for you:
#   pyzappi.web-masons.org


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # Get rid of that pesky "stdin: is not a tty" error
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/ubuntu-16.04"

  # Setup hostmanager config to update the host files
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  config.vm.define 'pyzappi-boilerplate' do |node|
      node.vm.hostname = 'pyzappi'
      node.vm.network :private_network, ip: '192.168.33.41'
      node.hostmanager.aliases = %w(pyzappi.localdomain pyzappi.web-masons.org)
  end

  # Forward SSH keys to the Guest VM
  config.ssh.forward_agent = true

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.41", hostname: "pyzappi"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/vagrant",
    :nfs => true,
    :mount_options => ['nolock,vers=3,udp,noatime,actimeo=1']

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # We're going to use the shell provider to install Ansible so that we can run
  # it within the Guest VM, not outside
  config.vm.provision "shell",
      :privileged => true,
      :keep_color => true,
      :inline => "/vagrant/script/bootstrap vagrant"

end