output "resource_group_id" {
  value = azurerm_resource_group.main.id
}

output "vnet_id" {
  value = azurerm_virtual_network.main.id
}

output "subnet_id" {
  value = azurerm_subnet.internal.id
}

output "public_ip" {
  value = azurerm_public_ip.main.ip_address
}
output "network_interface_id" {
  value = azurerm_network_interface.main.id
}
