from pathlib import Path

import resourses


def to_resource(relative_path):
    return str(Path(resourses.__file__).parent.joinpath(relative_path).absolute())
