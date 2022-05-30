from logging import getLogger

from pytracking.django import OpenTrackingView as _OpenTrackingView
from pytracking.webhook import send_webhook

from .utils import get_tracking_configuration

logger = getLogger(__name__)


class OpenTrackingView(_OpenTrackingView):
    def notify_tracking_event(self, tracking_result):
        logger.info(tracking_result)
        send_webhook(tracking_result)

    def notify_decoding_error(self, exception, request):
        logger.error(exception)

    def get_configuration(self):
        return get_tracking_configuration()
