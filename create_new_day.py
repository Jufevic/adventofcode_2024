import os
from pathlib import Path
from datetime import datetime
import shutil
from aocd import data

day = datetime.now().day
root_dir = Path(__file__).parent
day_dir = root_dir / f"day_{day:02}"
if not os.path.exists(day_dir):
    os.makedirs(day_dir)
    with open(Path(day_dir / "input.txt"), "w") as f:
        f.write(data)
    Path(day_dir / "demo_input.txt").touch()

    shutil.copyfile(root_dir / "template.py", day_dir / "part_1.txt")
    Path(day_dir / "part_2.txt").touch()
