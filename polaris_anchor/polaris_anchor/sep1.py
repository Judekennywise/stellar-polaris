from rest_framework.request import Request

def return_toml_contents(request, *args, **kwargs):
    return {
        "DOCUMENTATION": {
            "ORG_NAME": "Payme",
            "ORG_URL": "http://payme.com",
            "ORG_LOGO": "",
            "ORG_DESCRIPTION": "A payment platform",
            "ORG_OFFICIAL_EMAIL": "payme@gmail.com",
            "ORG_SUPPORT_EMAIL": "contactpayme@gmail.com"
        },
    }