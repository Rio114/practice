# ref: https://gihyo.jp/admin/serial/01/ubuntu-recipe/0061

######### WIP ############

apt-get -y install ubuntu-vm-builder


mkdir ~/vm
cd ~/vm
ubuntu-vm-builder kvm intrepid --mirror=http://jp.archive.ubuntu.com/ubuntu

# cd ubuntu-kvm/
# ./run.sh