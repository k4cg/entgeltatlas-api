"""
    Arbeitsagentur Entgeltatlas API

    Eine Datenbank zu Entgelten für Berufstätigkeiten in Deutschland durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** c4f0d292-9d0f-4763-87dd-d3f9e78fb006  **ClientSecret:** 566c4dd6-942f-4cda-aad6-8d611c577107   **Achtung**: Der generierte Token muss bei folgenden GET-requests an rest.arbeitsagentur.de/infosysbub/entgeltatlas/pc/v1/entgelte/[KldB-Schlüssel] im header als 'OAuthAccessToken' inkludiert werden. KldB meint in diesem Fall die Klassifikation der Berufe 2010 (vgl. rest.arbeitsagentur.de/infosysbub/dkz-rest/pc/v1/kldb2010). Beispielsweise repräsentiert der KldB-Schlüssel 84304 \"Berufe in der Hochschullehre und -forschung - hoch komplexe Tätigkeiten\"    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.entgeltatlas.model.response_inner_region import ResponseInnerRegion

from deutschland import entgeltatlas


class TestResponseInnerRegion(unittest.TestCase):
    """ResponseInnerRegion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseInnerRegion(self):
        """Test ResponseInnerRegion"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseInnerRegion()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
