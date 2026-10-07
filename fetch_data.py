"""Clone upstream into a temporary directory and retain only our selected PEPs."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PEPS = (483, 484, 526, 544, 563, 585, 586, 589, 591, 593, 604, 612,
        613, 646, 647, 649, 655, 673, 675, 681, 692, 695, 696, 698,
        705, 724, 742, 749)


def main():
    destination = ROOT / 'data' / 'peps'
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='typing-peps-') as temporary:
        clone = Path(temporary) / 'upstream'
        subprocess.run(['git', 'clone', '--depth', '1',
                        'https://github.com/python/peps.git', str(clone)], check=True)
        revision = subprocess.check_output(['git', '-C', str(clone), 'rev-parse',
                                            'HEAD'], text=True).strip()
        copied, missing = [], []
        for number in PEPS:
            name = f'pep-{number:04d}.rst'
            source = clone / 'peps' / name
            if source.exists():
                shutil.copy2(source, destination / name)
                copied.append(number)
            else:
                missing.append(number)
                print(f'Skipping missing PEP {number}')
        # Record provenance without introducing any additional graph input files.
        (destination.parent / 'source.json').write_text(json.dumps({
            'repository': 'https://github.com/python/peps', 'revision': revision,
            'copied': copied, 'missing': missing}, indent=2) + '\n', encoding='utf-8')
    print(f'Copied {len(copied)} PEPs to {destination}')


if __name__ == '__main__':
    main()
