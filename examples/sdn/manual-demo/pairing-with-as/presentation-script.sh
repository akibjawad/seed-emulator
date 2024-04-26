sudo ip link add name {bridge-name} type bridge
sudo ip link set dev {bridge-name} up

sudo ip link add veth-br type veth peer name veth-container

sudo ip link set dev veth-br master {bridge-name}
sudo ip link set dev veth-br up
sudo ip link set dev veth-container netns {container-name}
sudo ip link set veth-container up


sudo ovs-vsctl add-port br1 veth-faucet-ovs
sudo ip addr add 10.150.1.253/24 dev veth-faucet
sudo ip link set veth-faucet up
sudo ip link set veth-faucet-ovs up
