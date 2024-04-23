# Configures Client File
file { '~/.ssh/ssh_config':
  ensure => present,
  mode 	 => '0600',
  owner  => 'ubuntu',
  content=> '
      Host 98.98.98.98
        HostName 98.98.98.98
        User ubuntu
        IdentityFile ~/.ssh/school
	PasswordAuthentication no
  ',
}
