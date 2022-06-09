from cookiecutter.main import cookiecutter

from datetime import datetime

cookiecutter(
    'cookiecutter_conda_data_science',
    extra_context={'timestamp': datetime.utcnow().isoformat()}
)