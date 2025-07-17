from nordvpn_connect import initialize_vpn, rotate_vpn, close_vpn_connection

destination = "italy"

nordvpn_username = ""
nordvpn_password = ""

settings = initialize_vpn(destination)
rotate_vpn(settings)

# YOUR STUFF

close_vpn_connection(settings)
