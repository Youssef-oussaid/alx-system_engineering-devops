#Install flask version 2.1.0
class { 'python':
  pip => 'pip3',
}

package { 'flask':
  ensure => '2.1.0',
  provider => 'pip',
}
