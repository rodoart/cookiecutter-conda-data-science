from cookiecutter.main import cookiecutter

from datetime import datetime

cookiecutter(
    'cookiecutter-django',
    extra_context={'timestamp': datetime.utcnow().isoformat()}
)