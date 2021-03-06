#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from weddy import models

class WeddyApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "weddy",
            parts = (
                appier_extras.AdminPart(
                    account_c = models.Instance
                ),
            ),
            *args, **kwargs
        )

    @appier.exception_handler(appier.OAuthAccessError)
    def oauth_error(self, error):
        instance = models.Instance.from_session(rules = False)
        instance.invalidate_s()
        return self.redirect(
            self.url_for(self.request.location)
        )

    def get_pager(self, base, **kwargs):
        def pager(page):
            return self.url_for(
                base,
                page = page,
                **kwargs
            )
        return pager

if __name__ == "__main__":
    app = WeddyApp()
    app.serve()
else:
    __path__ = []
