#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import weddy

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
        oauth_verifier = self.field("oauth_verifier")
        api = self.get_api()
        oauth_token, oauth_token_secret = api.oauth_access(oauth_verifier)
        instance = weddy.Instance.from_session()
        instance.tokens_s(oauth_token, oauth_token_secret)
        self.redirect(
            self.url_for("base.index")
        )

    @appier.route("/oauth/invalidate", "GET")
    def oauth_invalidate(self):
        instance = weddy.Instance.from_session(rules = False)
        instance.invalidate_s()
        self.redirect(
            self.url_for("base.index")
        )
