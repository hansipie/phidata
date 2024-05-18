from phi.tools import Toolkit
from phi.utils.log import logger


class DNSLookupTools(Toolkit):
    def __init__(
        self,
        get_ipfromhostname: bool = True,
        get_hostnameformip: bool = True,
    ):
        super().__init__(name="dnslookup_tools")

        if get_ipfromhostname:
            self.register(self.get_ipfromhostname)
        if get_hostnameformip:
            self.register(self.get_hostnameformip)

    def get_ipfromhostname(self, hostname: str) -> str:
        """This function looks up a hostname’s IP address.

        :param hostname: Hostname targeted.
        :return: IP corresponding to the hostname.
        """
        import socket

        logger.info(f"hostname: {hostname}")
        try:
            ip = socket.gethostbyname(hostname)
            logger.debug(f"IP: {ip}")
            return ip
        except Exception as e:
            logger.warning(f"Error executing DNS Lookup: {e}")
            return f"Error executing DNS Lookup: {e}"

    def get_hostnameformip(self, ip: str) -> str:
        """This function gets hostname from IP address

        :param ip: IP adress targeted.
        :return: Hostname.
        """
        import socket

        logger.info(f"IP: {ip}")
        try:
            host = socket.gethostbyaddr(ip)
            logger.debug(f"Hostname: {host[0]}")
            return host[0]
        except Exception as e:
            logger.warning(f"Error getting hostname: {e}")
            return f"Error getting hostname: {e}"
