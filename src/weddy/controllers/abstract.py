#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import weddy

class AbstractController(appier.Controller):

    def ensure_api(self):
        username = self.session["username"]
        instance = weddy.Instance.get(username = username, rules = False)
        if instance.oauth_token and instance.oauth_token_secret: return
        api = self.get_api()
        url = api.oauth_authorize()
        instance.oauth_token = api.oauth_token
        instance.oauth_token_secret = api.oauth_token_secret
        instance.save()
        return url

    def get_api(self, redirect_url = None):
        username = self.session["username"]
        instance = weddy.Instance.get(username = username, rules = False)
        redirect_url = redirect_url or self.url_for("base.oauth", absolute = True)
        return instance.get_api(redirect_url = redirect_url)
