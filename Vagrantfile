# -*- mode: ruby -*-
#
# Vagrantfile for role tests
#
Vagrant.configure(2) do |config|
  config.vm.box = "debian/jessie64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000

#  config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "/home/vagrant/.ssh/id_rsa"
  config.vm.provision "shell", path: "vagrant_provision.sh"

  # Forward des connexions ssh
  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |v|
    v.name   = "insacloud-back"
    v.memory = 2048
#    v.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant", "1"]
  end
end