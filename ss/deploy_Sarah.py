import paramiko

def deploy(ssh_key, server, prefix):

	# Login, via SSH to the server.
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username = 'testtest', key_filename = ssh_key)

	# Clone your repository (and only your repository) to the server, in the home directory.
	ssh.exec_command('sudo yum install git -y')
	ssh.exec_command('cd; git clone https://github.com/ylan7/Sprinkle')

	# Set crontab to run sample script every 5 minutes
	ssh.exec_command('crontab -e')
	ssh.exec_command('*/5 * * * * python /home/' + username + '/Sprinkle/sample_script.py ' + prefix)
	
	# Logout
	ssh.close()

deploy('path_to_ssh_key_private_key', 'server-address', 'prefix')
