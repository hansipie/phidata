from phi.tools import Toolkit
from phi.utils.log import logger


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
            logger.debug(f"GET response status code: {response.status_code}")
            logger.debug(f"GET response size: {response.headers['Content-Length']}")
            return response.text
        except Exception as e:
            logger.warning(f"Error making GET request: {e}")
            return f"Error making GET request: {e}"

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
            logger.debug(f"POST response status code: {response.status_code}")
            logger.debug(f"POST response size: {response.headers['Content-Length']}")
            return response.text
        except Exception as e:
            logger.warning(f"Error making POST request: {e}")
            return f"Error making POST request: {e}"
