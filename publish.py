 

import json
import requests

from guru.util import read_file, write_file


def is_successful(result):
  """
  result could either be a boolean or the response object.
  """
  if isinstance(result, requests.models.Response):
    return int(result.status_code / 100) == 2
  else:
    return result


class Publisher:
  def __init__(self, g, name="", metadata=None, silent=False, dry_run=False):
    self.g = g
    self.name = name or self.__class__.__name__

    # manage the json config file.
    if metadata is not None:
      self.__metadata = metadata
    else:
      self.__metadata = json.loads(
        read_file("./%s.json" % self.name) or "{}"
      )
      if not self.__metadata:
        self.__metadata = {}
    
    self.silent = silent
    self.dry_run = dry_run
    self.__results = {}
