import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator, validate


class Label:
    """Class for defining string decorations"""
    PASS = '\033[1m\033[48;2;56;142;60m PASS \033[0m'
    FAIL = '\033[1m\033[48;2;211;47;47m FAIL \033[0m'


def schema_check(extension, script_dir, target_dir):
    """Validate the json schema of a specified target file"""
    print(f'\n> {extension}.json: checks\n')

    try:
        # Load and validate json schema file.
        schema_file = script_dir / 'Schemas' / f'{extension}.schema.json'
        schema_json = json.load(open(schema_file, 'r'))
        Draft7Validator.check_schema(schema_json)
    except Exception as e:
        print(f'{Label.FAIL} "{extension}.schema.json" is invalid!')
        print(f'\n\t{e.message if hasattr(e, "message") else e}\n')
        return

    # Validate each json files.
    target_files = target_dir.glob(f'**/*.{extension}.json')
    for target_file in list(target_files):
        try:
            target_json = json.load(open(target_file, 'r'))
            validate(target_json, schema_json)
            print(f'{Label.PASS} {target_file}')
        except Exception as e:
            print(f'{Label.FAIL} {target_file}')
            print(f'\n\t{e.message if hasattr(e, "message") else e}\n')


def main():
    script_dir = Path(__file__).parent
    # If no directory is defined in the argument, use the current directory.
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1])
    else:
        target_dir = Path('.')

    # Extract valid extensions from schema files.
    schema_files = list((script_dir / 'Schemas').iterdir())
    extensions = [s.name.replace('.schema.json', '') for s in schema_files]

    # Validate json schema in each extension.
    for e in extensions:
        schema_check(e, script_dir, target_dir)


if __name__ == '__main__':
    main()
