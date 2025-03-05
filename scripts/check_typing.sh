#!/bin/bash
poetry run mypy -p $PROJECT_SOURCE_DIR 
poetry run mypy -p $PROJECT_TEST_DIR
