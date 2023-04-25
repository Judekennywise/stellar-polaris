from django.apps import AppConfig

class AnchorConfig(AppConfig):
    name = 'polaris_anchor'

    def ready(self):
        
        from polaris.integrations import register_integrations
        from .sep1 import return_toml_contents
       #from .deposit import AnchorDeposit
        #from .withdrawal import AnchorWithdraw

        register_integrations(
            toml=return_toml_contents,
            #deposit=AnchorDeposit(),
            #withdraw=AnchorWithdraw()
        )