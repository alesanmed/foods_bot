# encoding: utf-8
"""
logger

Created by Donzok on 19/06/2017.
Copyright (c) 2017 . All rights reserved.
"""

# -*- coding: utf-8 -*-
import logging


def init_logger():
    log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("files/mealsbot.log")
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

def get_logger():
    return logging.getLogger()