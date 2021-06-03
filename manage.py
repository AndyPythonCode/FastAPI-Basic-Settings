# This file is uses to create new app with 'python manage.py --app <name>'
import os
import sys
import plugin

FOLDER_BASE: str = '\\apps'
FOLDER_URL: str = f"{os.getcwd()}{FOLDER_BASE}"

for index, command in enumerate(sys.argv):
    # Create new app
    if command == '--app':
        if not os.path.exists(f'{FOLDER_URL}\\{sys.argv[index+1]}'):
            os.makedirs(f'{FOLDER_URL}\\{sys.argv[index+1]}')
            content = {
                '__init__.py': '',
                'models.py': plugin.examples.models(sys.argv[-1]),
                'routers.py': plugin.examples.routers(sys.argv[-1]),
                'schemas.py': plugin.examples.schemas(sys.argv[-1]),
            }
            for document in content:
                #Write - Opens a file for writing, creates the file if it does not exist
                with open (f'{FOLDER_URL}\\{sys.argv[index+1]}\\{document}', 'w') as f:
                    f.write(content[document])
                    f.close()
        else:
            raise FileExistsError('You already has this folder, try another name')