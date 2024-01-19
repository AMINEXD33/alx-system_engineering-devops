# Install flask version 2.1.0

$base_package = 'Flask'
package { $base_package
ensure => '2.5.0',
name   => $base_pakage,
provider => 'pip'
}
