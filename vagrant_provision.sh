#!/bin/bash
REPO_ROOT="/vagrant/"

# Update
sudo apt-get update -y
sudo apt-get upgrade -y
# Install required packages
sudo apt-get install python-pip python-dev -y
sudo pip install -Iv ansible==1.9.3

cd "$REPO_ROOT/ansible"
for i in `find . -type f \( -name "hosts" \)`; do    sed -i 's/\r//' $i ; done
sudo rm -f /home/vagrant/.ssh/id_rsa /home/vagrant/.ssh/id_rsa.pub
sudo mkdir -p /root/.ssh/
su vagrant <<EOF
ssh-keygen -t rsa -N "" -f /home/vagrant/.ssh/id_rsa
cat /home/vagrant/.ssh/id_rsa.pub | sudo tee -a /root/.ssh/authorized_keys
ssh-keyscan localhost > ~/.ssh/known_hosts
cd "$REPO_ROOT/ansible"
ansible-playbook -i inventories/dev site.yml
EOF