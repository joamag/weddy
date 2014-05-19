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
        username = self.session["username"]
        instance = weddy.Instance.get(username = username, rules = False)
        instance.oauth_token = oauth_token
        instance.oauth_token_secret = oauth_token_secret
        instance.save()
        self.redirect(
            self.url_for("base.index")
        )
