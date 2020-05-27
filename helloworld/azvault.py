from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class AzVault():

    @staticmethod
    def getSecret(name, vaulturi = "https://djangoazvault.vault.azure.net/"):
        try:
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url = vaulturi, credential = credential)
            return client.get_secret(name)
        except:
            return None