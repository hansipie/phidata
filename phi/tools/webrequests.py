from phi.tools import Toolkit
from phi.utils.log import logger
from requests.exceptions import HTTPError


class WebRequestsTools(Toolkit):
    def __init__(
        self,
        get_method: bool = True,
        post_method: bool = True,
    ):
        super().__init__(name="webrequests_tools")

        if get_method:
            self.register(self.get_method)
        if post_method:
            self.register(self.post_method)

    def get_method(self, url: str) -> str:
        """This function sends a GET request to a URL and returns the content.

        :param url: The url of the request.
        :return: Request's response.
        """
        import requests

        logger.info(f"GET request: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_e:
            logger.warning(f"HTTP error: {http_e}")
            return f"HTTP error: {http_e}"
        except Exception as e:
            logger.warning(f"Other error: {e}")
            return f"Other error: {e}"
        else:
            logger.debug(f"HTTP GET response status code: {response.status_code}")
            logger.debug(f"HTTP GET response size: {response.headers['Content-Length']}")
            return response.content

    def post_method(self, url: str, payload: str = "") -> str:
        """This function sends a POST request with an optionnal payload to a URL and returns the content.

        :param url: The url of the request.
        :param payload: The payload to send.
        :return: Request's response.
        """
        import requests

        logger.info(f"POST request: {url}")
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
        except HTTPError as http_e:
            logger.warning(f"HTTP error: {http_e}")
            return f"HTTP error: {http_e}"
        except Exception as e:
            logger.warning(f"Other HTTP error: {e}")
            return f"Other HTTP error: {e}"
        else:
            logger.debug(f"HTTP POST response status code: {response.status_code}")
            logger.debug(f"HPPT POST response size: {response.headers['Content-Length']}")
            return response.content
