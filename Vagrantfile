Vagrant.configure("2") do |config|
  config.vm.define:"ansible-node01" do |cfg|
    cfg.vm.box = "centos/7"
    cfg.vm.provider:virtualbox do |vb|
        vb.name="Ansible-Node01"
        vb.customize ["modifyvm", :id, "--cpus", 1]
        vb.customize ["modifyvm", :id, "--memory", 1024]
    end
    cfg.vm.host_name="ansible-node01"
    cfg.vm.synced_folder ".", "/vagrant", disabled: false
    # cfg.vm.network "public_network", ip: "172.20.10.11"
    cfg.vm.network "forwarded_port", guest: 22, host: 19511, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 80, host: 10080
    cfg.vm.provision "shell", path: "bash_ssh_conf_4_CentOS.sh"
  end

  config.vm.define:"ansible-node02" do |cfg|
    cfg.vm.box = "centos/7"
    cfg.vm.provider:virtualbox do |vb|
        vb.name="Ansible-Node02"
        vb.customize ["modifyvm", :id, "--cpus", 1]
        vb.customize ["modifyvm", :id, "--memory", 1024]
    end
    cfg.vm.host_name="ansible-node02"
    cfg.vm.synced_folder ".", "/vagrant", disabled: false
    # cfg.vm.network "public_network", ip: "172.20.10.12"
    cfg.vm.network "forwarded_port", guest: 22, host: 19512, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 80, host: 20080
    cfg.vm.provision "shell", path: "bash_ssh_conf_4_CentOS.sh"
  end

  config.vm.define:"ansible-node03" do |cfg|
    cfg.vm.box = "ubuntu/trusty64"
    cfg.vm.provider:virtualbox do |vb|
        vb.name="Ansible-Node03"
        vb.customize ["modifyvm", :id, "--cpus", 1]
        vb.customize ["modifyvm", :id, "--memory", 1024]
    end
    cfg.vm.host_name="ansible-node03"
    cfg.vm.synced_folder ".", "/vagrant", disabled: true
    # cfg.vm.network "public_network", ip: "172.20.10.13"
    cfg.vm.network "forwarded_port", guest: 22, host: 19513, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 80, host: 30080
    # cfg.vm.provision "shell", path: "bash_ssh_conf_4_CentOS.sh"
  end

  config.vm.define:"ansible-server" do |cfg|
    cfg.vm.box = "centos/7"
    cfg.vm.provider:virtualbox do |vb|
        vb.name="Ansible-Server"
        vb.customize ["modifyvm", :id, "--cpus", 2]
        vb.customize ["modifyvm", :id, "--memory", 2048]
    end
    cfg.vm.host_name="ansible-server"
    cfg.vm.synced_folder ".", "/vagrant", disabled: false
    # cfg.vm.network "public_network", ip: "172.20.10.10"
    cfg.vm.network "forwarded_port", guest: 22, host: 19510, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 8080, host: 58080
    # cfg.vm.network "forwarded_port", guest: 9000, host: 59000
    cfg.vm.provision "shell", path: "bootstrap.sh"  
    # cfg.vm.provision "file", source: "Ansible_env_ready.yml", destination: "Ansible_env_ready.yml"
    # cfg.vm.provision "shell", inline: "ansible-playbook Ansible_env_ready.yml"
    # cfg.vm.provision "shell", path: "add_ssh_auth.sh", privileged: false

    # cfg.vm.provision "file", source: "Ansible_ssh_conf_4_CentOS.yml", destination: "Ansible_ssh_conf_4_CentOS.yml"
    # cfg.vm.provision "shell", inline: "ansible-playbook Ansible_ssh_conf_4_CentOS.yml"
  end
end
