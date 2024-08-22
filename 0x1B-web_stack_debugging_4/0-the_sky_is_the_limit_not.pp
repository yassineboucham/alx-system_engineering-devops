#creasing the maximum number of open file descriptors (ulimit) for the Nginx
# web server by modifying the configuration file /etc/default/nginx.
exec { 'Increase ULIMIT for Nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/sbin', '/usr/bin'],
  user    => 'root',
}

# Restart the Nginx server
exec { 'Restart Nginx':
  command => 'service nginx restart',
  path    => ['/usr/local/bin', '/bin', '/usr/sbin', '/usr/bin'],
  user    => 'root',
  require => Exec['Increase ULIMIT for Nginx'],  # Ensure this runs after ULIMIT increase
}
