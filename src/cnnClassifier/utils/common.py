import os
from box.exception import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib 
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64