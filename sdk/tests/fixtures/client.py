import pytest
import dotenv
import os
from src.utils import AzureCredentialSingleton


dotenv.load_dotenv()


@pytest.fixture
def ml_client():



    

