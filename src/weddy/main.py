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

if __name__ == "__main__":
    app = WeddyApp()
    app.serve()
