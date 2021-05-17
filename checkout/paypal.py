import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AdEcMQm_v82Pu9wDvYYCeesPvZu2LOaCWCotlHwxL-z50Y1jYyzPY1if7YRLCpafkc9sAcwWSsj5h6TG"
        self.client_secret = "EC1YDsFC3WS4Ukhbz2HXrj0jgBkkjZ9SgTjGazFRi4W2ik5GwaWnsnGTul_gjF4r4xjJ38V5GXqkDZad"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
