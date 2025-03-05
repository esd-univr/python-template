#!/bin/bash
poetry run ruff check --fix $PROJECT_SOURCE_DIR $PROJECT_TEST_DIR
poetry run ruff format $PROJECT_SOURCE_DIR $PROJECT_TEST_DIR
poetry run lizard $PROJECT_SOURCE_DIR $PROJECT_TEST_DIR -w
