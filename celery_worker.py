import subprocess
import os, sys

from celery import Celery
from time import sleep
from dotenv import load_dotenv

sys.path.append('/home/repo')
sys.path.append('/home/repo/presentation')

from presentation.scripts.run_0 import train, classify


load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task(name='create_task')
def create_task():
    os.chdir("repo")
    config_file = 'presentation/pipeline/config/template.toml'

    root_folder = os.environ['CONFIG_FOLDER']
    print(root_folder)

    train(config_file,
          history_path='results/history.csv',
          step='pretraining',
          pipeline_id=None,
          gpu=0)
