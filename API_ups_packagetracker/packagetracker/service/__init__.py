
class BaseInterface():
    """
    Base class for tracking interfaces

    Args:
        config: ConfigParser object
        testing (bool): True to run in test-only mode, if supported

    """
    click_url = "http://invalid_url/{num}"


    def __init__(self, config, testing=False):
        self.config = config
        self.testing = testing

    def cleanup_number(self, num):
        """
        Cleans up the tracking number by removing spaces and uppercasing it.

        Args:
            num (str): tracking number
        Returns:
            str: clean tracking number
        """
        return num.upper().replace(' ', '')


    def identify(self, num):
        """
        Identify a package.

        Args:
            num (str): Tracking number

        Returns:
            bool: true if this service can track this package
        """
        raise NotImplementedError


    def track(self, num):
        """
        Track a package.

        Args:
            num (str): Tracking number

        Raises:
            InvalidTrackingNumber
            TrackFailed
        """
        raise NotImplementedError


    def url(self, num):
        """
        Return a clickable URL to track a given package.
        Subclasses should have a 'click_url' property!

        Args:
            num (str): tracking number

        Returns:
            str: a URL
        """
        return self.click_url.format(num=num)
