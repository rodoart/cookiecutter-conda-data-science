from cookiecutter.main import cookiecutter
from datetime import datetime
import os.path


def run():
    template = os.path.dirname(os.path.abspath(__file__))


    today = datetime.today()
    date = today.date().isoformat()

    cookiecutter(
        template,
        extra_context={
            'timestamp': date,
        },
    )

if __name__ == '__main__':
    run()