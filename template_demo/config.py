from os import path

import template_demo

base_path = path.dirname(path.dirname(template_demo.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
