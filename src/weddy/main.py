#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from weddy import models

class WeddyApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(
            self,
            name = "weddy",
            parts = (
                appier_extras.AdminPart(
                    account_c = models.Instance
                ),
            )
        )

    @appier.exception_handler(appier.OAuthAccessError)
    def oauth_error(self, error):
        instance = models.Instance.from_session(rules = False)
        instance.invalidate_s()
        return self.redirect(
            self.url_for("base.index")
        )

if __name__ == "__main__":
    app = WeddyApp()
    app.serve()
