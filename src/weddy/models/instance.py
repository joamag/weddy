#!/usr/bin/python
# -*- coding: utf-8 -*-

import flickr
import appier
import appier_extras

class Instance(appier_extras.admin.Account):
    
    oauth_token = appier.field()
    
    oauth_token_secret = appier.field()
    
    @classmethod
    def login(cls, username, password): 
        account = super(Instance, cls).login(username, password)        
        return account


        #self.oauth_token = kwargs.get("oauth_token", None)
        #self.oauth_token_secret = kwargs.get("oauth_token_secret", None)

    def get_api(self):
        return flickr.Api(oauth_token = oauth_token)