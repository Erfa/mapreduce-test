from flask import Flask

from google.appengine.ext import ndb
from mapreduce import mapreduce_pipeline
import pipeline


class User(ndb.Model):
    name = ndb.StringProperty()

app = Flask(__name__)

def appengine_mapper(user):
    print user.name

class TouchPipeline(pipeline.Pipeline):
    """
    Pipeline to update the timestamp of entities.
    """

    def run(self, *args, **kwargs):
        """ run """
        mapper_params = {
            "entity_kind": "app.User",
        }
        yield mapreduce_pipeline.MapperPipeline(
            "Print all usernames",
            handler_spec="app.appengine_mapper",
            input_reader_spec="mapreduce.input_readers.DatastoreInputReader",
            params=mapper_params,
        )

@app.route('/create_users')
def create_users():
    for i in range(5000):
        User(name=u'User {}'.format(i)).put()

    return ('', 204)

@app.route('/run_job')
def run_job():
    pipeline = TouchPipeline()
    pipeline.start()

    return 'Job started'