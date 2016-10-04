from flask import Flask

from google.appengine.ext.mapreduce.mapreduce_pipeline import MapreducePipeline


app = Flask(__name__)

def appengine_mapper(e):
    pass

def appengine_reduce(e):
    pass

@app.route('/')
def hello_world():
    pipeline = MapreducePipeline(
        '',
        'app.appengine_mapper',
        'app.appengine_reduce',
        'mapreduce.input_readers.DatastoreInputReader',
        mapper_params={
            'entity_kind': 'SomeEntity',
        },
    )

    pipeline.start()
