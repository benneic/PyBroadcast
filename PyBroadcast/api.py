

import requests
import simplejson as json
from .models import Email, Facebook, Foursquare, Twitter
import utils


class Broadcast(object):

  def __init__(self, base_url=None):
    self.base_url = base_url


  def add_endpoints(self):
    self.email = Email(self)
    self.facebook = Facebook(self)
    self.foursquare = Foursquare(self)
    self.twitter = Twitter(self)

  def post(self, path, data, **kwargs):
    """Expects data to be a dict."""
    url = self.base_url + path
    kwargs = utils.kwargs_converter(kwargs)
    payload = json.dumps(data, default=utils.json_dumps_handler)
    response = self.session.post(url, data=payload, params=kwargs)
    response.raise_for_status()
    if response.content:
      content = json.loads(response.content)
      content = utils.response_converter(content)
      return content
    return response.content


class Endpoint(object):

  def __init__(self, api):
        self.api = api


class Email(Endpoint):

  def member_new(self, member_email, member_name):
    body = self.api.post('/email/member/new', {'member_email': member_email, 'member_name':member_name})
    return Email.fromDict(body['response'])

class Facebook(Endpoint):

  def status_new(self,ll, facebook_token, facebook_timeline_enabled, venue_name, activity_id, photo_uri, message):
    body = self.api.post('/broadcast/facebook/status/new', {'ll':ll, 'facebook_token':facebook_token,
                        'facebook_timeline_enabled':facebook_timeline_enabled, 'venue_name':venue_name,
                        'activity_id':activity_id, 'photo_uri':photo_uri, 'message':message})
    return Facebook.fromDict(body['response'])

  def checkin_new(self,ll, facebook_token, facebook_venue_id):
    body = self.api.post('/broadcast/facebook/checkin/new', {'ll':ll, 'facebook_token':facebook_token,
                                                             'facebook_venue_id':facebook_venue_id})
    return Facebook.fromDict(body['response'])

class Twitter(Endpoint):

  def status_new(self,ll, twitter_token,twitter_secret, venue_name, activity_id, message):
    body = self.api.post('/broadcast/twitter/status/new', {'ll':ll, 'twitter_token':twitter_token, 'twitter_secret':twitter_secret,
                                                           'venue_name':venue_name, 'activity_id':activity_id,'message':message })
    return Twitter.fromDict(body['response'])

class Foursquare(Endpoint):

  def checkin_new(self,ll, foursquare_token, venue_name, activity_id, photo_uri, message):
    body = self.api.post('/broadcast/foursquare/checkin/new', {'ll':ll, 'foursquare_token':foursquare_token,
                          'venue_name':venue_name, 'activity_id':activity_id, 'photo_uri':photo_uri, 'message':message})
    return Foursquare.fromDict(body['response'])
  
    