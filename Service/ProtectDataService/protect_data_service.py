import ctypes
from contextlib import contextmanager


class ProtectDataService:

    @staticmethod
    @contextmanager
    def sensitive_data_context(data):

        try:
            yield data

        finally:
            if isinstance(data, (bytearray, bytes)):
                ctypes.memset(ctypes.addressof(data), 0, len(data))
