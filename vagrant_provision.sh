#!/bin/bash
REPO_ROOT="/vagrant/"
USER="vagrant"

# Update
apt-get update -y
apt-get upgrade -y
# Install required packages
apt-get install python-pip python-dev -y
pip install -Iv ansible==1.9.3

cd "$REPO_ROOT/ansible"
for i in `find . -type f \( -name "hosts" \)`; do    sed -i 's/\r//' $i ; done
# chmod +x "$REPO_ROOT/ansible/dex"
rm -f "/home/$USER/.ssh/id_rsa" "/home/$USER/.ssh/id_rsa.pub"
mkdir -p /root/.ssh/
# Command to deploy
read -r -d '' DEPLOY <<EOF
#!/bin/bash
cd "$REPO_ROOT/ansible"
ansible-playbook -i inventories/dev site.yml
EOF
echo "$DEPLOY" | tee /usr/local/bin/deploy_local > /dev/null
chmod +x /usr/local/bin/deploy_local

su $USER <<EOF
ssh-keygen -t rsa -N "" -f "/home/$USER/.ssh/id_rsa"
EOF
cat "/home/$USER/.ssh/id_rsa.pub" | tee -a /root/.ssh/authorized_keys
su $USER <<EOF
ssh-keyscan localhost > ~/.ssh/known_hosts
cd "$REPO_ROOT/ansible"
deploy_local
EOF