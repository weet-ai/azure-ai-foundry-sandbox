from src.utils import AzureCredentialSingleton
import logging

logging.basicConfig(level = "DEBUG")

def main():

    credential = AzureCredentialSingleton().get_credential()
    token = credential.get_token(".default")
    logging.info(f"Token: {token}")


if __name__ == "__main__":

    main()