# Manifest that kills a process named `killmenow`
exec { 'killmenow':
  command  => 'pkill -f ./killmenow',
  cwd      => '/root',
  provider => 'shell',
}
