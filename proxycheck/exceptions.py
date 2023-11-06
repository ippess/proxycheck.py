class ProxyCheckException(Exception):
    """
    Base exception for proxycheck.
    """


class ProxyCheckDenied(ProxyCheckException):
    """
    TODO: Add docstring
    """
    pass


class ProxyCheckError(ProxyCheckException):
    """
    TODO: Add docstring
    """
    pass