from azure.identity import DefaultAzureCredential
from threading import Lock


class AzureCredentialSingleton:
    """
    Singleton class to encapsulate DefaultAzureCredential.
    Ensures only one instance of DefaultAzureCredential is created and reused.
    """

    _instance = None  # Class-level attribute to hold the singleton instance
    _lock = Lock()  # Lock for thread-safe initialization

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:  # Double-checked locking
                    cls._instance = super(AzureCredentialSingleton, cls).__new__(cls)
                    cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, *args, **kwargs):
        """
        Initialize the DefaultAzureCredential instance.
        """
        self.credential = DefaultAzureCredential(*args, **kwargs)

    def get_credential(self):
        """
        Get the DefaultAzureCredential instance.
        """
        return self.credential
