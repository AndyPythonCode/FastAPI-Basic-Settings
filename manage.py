# This file is uses to create new app with 'python manage.py --app <name>'
import os
import sys
from plugin import examples

folder_base: str = '\\apps'
folder_url: str = f"{os.getcwd()}{folder_base}"

for index, command in enumerate(sys.argv):
    # Create new app
    if command == '--app':
        if not os.path.exists(f'{folder_url}\\{sys.argv[index+1]}'):
            os.makedirs(f'{folder_url}\\{sys.argv[index+1]}')
            content = {
                '__init__.py': '',
                'models.py': examples.models(),
                'routers.py': examples.routers(),
                'schemas.py': examples.schemas(),
            }
            for document in content:
                #Write - Opens a file for writing, creates the file if it does not exist
                with open (f'{folder_url}\\{sys.argv[index+1]}\\{document}', 'w') as f:
                    f.write(content[document])
                    f.close()
        else:
            raise FileExistsError('You already has this folder, try another name')
