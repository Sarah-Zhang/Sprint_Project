# team Sprinkle
# members: Chenxi Ge, Dixin Yan, Xiaowen(Sarah) Zhang, Yue Lan

import paramiko

def deploy(path_to_ssh_key_private_key = 'credentials/sprinkle.pem',
           server_address = 'ec2-54-202-17-67.us-west-2.compute.amazonaws.com',
           prefix = 'default_tracking_prefix'):
    
    if server_address.count('@') == 1:
        usr, addr = server_address.split('@')
    else:
        usr = 'testtest'
        addr = server_address
    
    print 'Connecting to the box'
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(addr , username = usr, key_filename = path_to_ssh_key_private_key)
        print 'Connected' 
    except:
        print 'Failed connecting' 
        return
    
    print 'Cloning application scripts'
    try:
        ssh.exec_command('rm -rf Sprinkle')
        ssh.exec_command('git clone https://github.com/ylan7/Sprinkle.git')
        # ssh.exec_command('cd Sprinkle')
        print 'Folder cloned'
    except:
        print 'Failed cloning'
        return
    
    print 'Starting Flask'
    try:
    	# this is one way
        ssh.exec_command('screen')
        ssh.exec_command('pkill -f my_flask.py')
        ssh.exec_command('python ~/Sprinkle/my_flask.py ' + prefix)
        ssh.exec_command('screen -d')
        print 'Flask Running'
    except:
        print 'Failed to start Flask'
        return

    ssh.close()
    
if __name__ == '__main__':
    deploy()