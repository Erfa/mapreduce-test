from flask import Flask

from google.appengine.ext import ndb
from mapreduce import base_handler
from mapreduce.mapreduce_pipeline import MapreducePipeline
from mapreduce.output_writers import OutputWriter


class User(ndb.Model):
    name = ndb.StringProperty()

app = Flask(__name__)

def appengine_mapper(e):
    pass

def appengine_reduce(e):
    pass

class Pipeline(base_handler.PipelineBase):
    def run(self):
        output = yield MapreducePipeline(
            "index",
            "main.index_map",
            "main.index_reduce",
            "mapreduce.input_readers.DatastoreInputReader",
            params={
                "input_reader": {
                    "entity_kind": "app.User",
                }
            },
            shards=1
        )

        yield Output(output)

class Output(OutputWriter):
    def run(self, output):
        pass

@app.route('/')
def hello_world():
    pipeline = Pipeline()
    pipeline.start()
