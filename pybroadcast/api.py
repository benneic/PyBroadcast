import requests
import simplejson as json
import models
import utils


class Broadcast(object):

  def __init__(self, base_url=None):
    self.base_url = base_url

    # Enable keep-alive and connection-pooling.
    self._session = requests.session()
    self._session.config.update({'max_retries':3})

    # Send and receive JSON.
    self._session.headers.update({'content-type': 'application/json'})
    self._session.headers.update({'Accept': 'application/json'})

    self._add_endpoints()


  def _add_endpoints(self):
    self.email = Email(self)
    self.facebook = Facebook(self)
    self.foursquare = Foursquare(self)
    self.twitter = Twitter(self)


  def get(self, path, **kwargs):
    kwargs = utils.kwargs_converter(kwargs)
    url = self.base_url + path
    response = self._session.get(url, params=kwargs)
    response.raise_for_status()
    content = json.loads(response.content)
    content = utils.response_converter(content)
    return content


  def post(self, path, data=None, **kwargs):
    """Expects data to be a dict."""
    url = self.base_url + path
    kwargs = utils.kwargs_converter(kwargs)
    if data:
      payload = json.dumps(data, default=utils.json_dumps_handler)
    else:
      payload = data
    response = self._session.put(url, data=payload, params=kwargs)
    response.raise_for_status()
    if response.content:
      content = json.loads(response.content)
      content = utils.response_converter(content)
      return content
    return response.content


  def put(self, path, data=None, **kwargs):
    """Expects data to be a dict."""
    url = self.base_url + path
    kwargs = utils.kwargs_converter(kwargs)
    if data:
      payload = json.dumps(data, default=utils.json_dumps_handler)
    else:
      payload = data
    response = self._session.put(url, data=payload, params=kwargs)
    response.raise_for_status()
    content = json.loads(response.content)
    content = utils.response_converter(content)
    return content


  def delete(self, path, **kwargs):
    url = self.base_url + path
    kwargs = utils.kwargs_converter(kwargs)
    response = self._session.delete(url, params=kwargs)
    response.raise_for_status()
    content = json.loads(response.content)
    content = utils.response_converter(content)
    return content



class Endpoint(object):

  def __init__(self, api):
        self._api = api


class Email(Endpoint):


  def new_member(self, member_email, member_name):
    body = self._api.post('email/member/new', {'member_email': member_email, 'member_name':member_name})
    return models.Email.fromDict(body['response'])


class Facebook(Endpoint):


  def status(self, ll, facebook_token, facebook_timeline_enabled, venue_name, activity_id, message=None, photo_uri=None):
    body = self._api.post('broadcast/facebook/status/new',
      ll=ll,
      facebook_token=facebook_token,
      facebook_timeline_enabled=facebook_timeline_enabled,
      venue_name=venue_name,
      activity_id=activity_id,
      message=message,
      photo_uri=photo_uri)
    return models.Facebook.fromDict(body['response'])


  def checkin(self, ll, facebook_token, facebook_venue_id):
    body = self._api.post('broadcast/facebook/checkin/new',
      ll=ll,
      facebook_token=facebook_token,
      facebook_venue_id=facebook_venue_id)
    return models.Facebook.fromDict(body['response'])


class Twitter(Endpoint):


  def status(self, ll, twitter_token, twitter_secret, venue_name, activity_id, message):
    body = self._api.post('broadcast/twitter/status/new',
      ll=ll,
      twitter_token=twitter_token,
      twitter_secret=twitter_secret,
      venue_name=venue_name,
      activity_id=activity_id,
      message=message)
    return models.Twitter.fromDict(body['response'])


class Foursquare(Endpoint):


  def checkin(self, ll, foursquare_token, venue_name, activity_id, photo_uri, message):
    body = self._api.post('broadcast/foursquare/checkin/new',
      ll=ll,
      foursquare_token=foursquare_token,
      venue_name=venue_name,
      activity_id=activity_id,
      photo_uri=photo_uri,
      message=message)
    return models.Foursquare.fromDict(body['response'])
  
    