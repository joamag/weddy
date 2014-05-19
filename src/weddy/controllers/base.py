#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import abstract

class BaseController(abstract.AbstractController):

    @appier.route("/", "GET")
    @appier.route("/index", "GET")
    def index(self):
        return self.template(
            "index.html.tpl"
        )

    @appier.route("/oauth", "GET")
    def oauth(self):
        #@todo vou ter de fazer a associacao entre o user
        # que esta em sessao e os tokens atuais !!! cenas !!!
        return self.template(
            "index.html.tpl"
        )
