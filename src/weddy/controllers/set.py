#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

class SetController(appier.Controller):

    @appier.route("/sets", "GET")
    @appier.private
    def list(self):
        return self.template(
            "index.html.tpl"
        )
