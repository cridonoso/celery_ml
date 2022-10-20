import subprocess
import os, sys

from celery import Celery
from time import sleep
from dotenv import load_dotenv

sys.path.append('/home/refactoring')
sys.path.append('/home/refactoring/presentation')

from presentation.scripts.run_0 import train


load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name='create_task')
def create_task():
    print(os.getcwd())
    os.chdir("refactoring")
    config_file = 'presentation/pipeline/config/template.toml'

    train(config_file,
          history_path='results/history.csv',
          step='pretraining',
          pipeline_id=None)
