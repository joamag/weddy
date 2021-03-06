#!/usr/bin/python
# -*- coding: utf-8 -*-

import flickr
import appier
import appier_extras

class Instance(appier_extras.admin.Account):

    client_key = appier.field(
        index = True
    )

    client_secret = appier.field(
        private = True
    )

    oauth_token = appier.field(
        private = True
    )

    oauth_token_secret = appier.field(
        private = True
    )

    oauth_temporary = appier.field(
        type = bool,
        private = True
    )

    @classmethod
    def login(cls, username, password):
        account = super(Instance, cls).login(username, password)
        return account

    @classmethod
    def from_session(cls, *args, **kwargs):
        session = appier.get_session()
        username = session["username"]
        return cls.get(username = username, *args, **kwargs)

    def tokens_s(self, oauth_token, oauth_token_secret, temporary = True):
        instance = self.reload(rules = False)
        instance.oauth_token = oauth_token
        instance.oauth_token_secret = oauth_token_secret
        instance.oauth_temporary = temporary
        instance.save()

    def invalidate_s(self):
        self.tokens_s(None, None, temporary = True)

    def get_api(self, redirect_url = None):
        instance = self.reload(rules = False)
        return flickr.API(
            client_key = instance.client_key,
            client_secret = instance.client_secret,
            oauth_token = instance.oauth_token,
            oauth_token_secret = instance.oauth_token_secret,
            redirect_url = redirect_url
        )
