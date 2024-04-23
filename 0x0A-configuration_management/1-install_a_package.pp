#Install flask version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask',
  unless  => '/usr/bin/pip3 show Flask',
}
