#!/bin/bash
REPO_ROOT=`pwd`
if [ -z "$1" ]; then
    echo 'Need first arg: user'
    exit 0
fi
USER="$1"
if [ -n "$2" ]; then
    REPO_ROOT="$2"
fi

# Update
apt-get update -y
apt-get upgrade -y
# Install required packages
apt-get install python-pip python-dev -y
pip install -Iv ansible==1.9.3

cd "$REPO_ROOT/ansible"
for i in `find . -type f \( -name "hosts" \)`; do    sed -i 's/\r//' $i && chmod +x $i ; done
rm -f "/home/$USER/.ssh/id_rsa" "/home/$USER/.ssh/id_rsa.pub"
mkdir -p /root/.ssh/

# Command to deploy
for d in $REPO_ROOT/ansible/inventories/*
do
    target=`basename $d`
    read -r -d '' DEPLOY <<EOF
#!/bin/bash
CMD="cd \"$REPO_ROOT/ansible\" && ansible-playbook -i \"inventories/$target\" site.yml"
echo "command need to be executed as user: $USER"
if [ \$USER = "$USER" ]; then
    eval "\$CMD"
else
    su $USER <<XXX
eval "\$CMD"
XXX
fi
EOF
    echo "$DEPLOY" | tee "/usr/local/bin/deploy_$target" > /dev/null
    chmod +x "/usr/local/bin/deploy_$target"
done

su $USER <<EOF
ssh-keygen -t rsa -N "" -f "/home/$USER/.ssh/id_rsa"
EOF
cat "/home/$USER/.ssh/id_rsa.pub" | tee -a /root/.ssh/authorized_keys
su $USER <<EOF
ssh-keyscan localhost > ~/.ssh/known_hosts
EOF
