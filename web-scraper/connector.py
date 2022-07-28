from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, _check_health

logger = get_logger('web_scraper')


class WebScraper(Connector):

    def execute(self, config, operation, params, **kwargs):
        action = operations.get(operation)
        return action(config, params)

    def check_health(self, config):
        _check_health(config)
