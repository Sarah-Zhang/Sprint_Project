# team Sprinkle
# members: Chenxi Ge, Dixin Yan, Xiaowen(Sarah) Zhang, Yue Lan

import paramiko

def deploy(path_to_ssh_key_private_key = 'credentials/sprinkle.pem',
           server_address = 'ec2-54-202-17-67.us-west-2.compute.amazonaws.com',
           prefix = 'test_file'): 
    
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
    
    print 'Setting up crontab task'
    try:
    	# this is one way
    	ssh.exec_command('echo "*/5 * * * * python ~/Sprinkle/sample_script.py ' + prefix + '" > task.txt')
    	ssh.exec_command('crontab task.txt')
    	ssh.exec_command('rm task.txt')

    	# this is another way
    	# ssh.exec_command('crontab -e')
    	# ssh.exec_command('*/5 * * * * python sample_script.py')
    	# ssh.exec_command(':wq')

    	print 'Crontab set' 

    except:
    	print 'Failed setting up crontab'
    	return


    ssh.close()
    
    
# deploy()