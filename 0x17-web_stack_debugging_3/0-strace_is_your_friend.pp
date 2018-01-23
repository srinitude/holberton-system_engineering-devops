# Finds typo in wp-settings
$module_stdlib = 'puppetlabs-stdlib'
exec { 'puppet_module_stdlib':
  command => "puppet module install ${module_stdlib}",
  unless  => "puppet module list | grep ${module_stdlib}",
  path    => ['/bin', '/usr/bin']
}
-> file { '/var/www/html/wp-settings.php':
  ensure => present
}
-> file_line { 'replace':
  path    => '/var/www/html/wp-settings.php',
  replace => true,
  line    => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match   => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"
}
