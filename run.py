#!/usr/bin/env python
import config as cfg
from app import app
app.run(host=cfg.HOST, port=cfg.PORT)

