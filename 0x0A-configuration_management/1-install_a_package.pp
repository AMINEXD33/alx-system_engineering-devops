# Install flask version 2.1.0

$base_package = 'flask'
package { $base_package:
ensure => '2.1.0',
provider => 'pip3
}
