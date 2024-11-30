import os
from jinja2 import Environment, FileSystemLoader

def generate_file(template_name, output_path, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(context)

    with open(output_path, 'w') as f:
        f.write(output)

if __name__ == '__main__':
    package_name = 'my_ros2_package'
    maintainer = 'Your Name'
    maintainer_email = 'your_email@example.com'
    description = 'Example ROS 2 package'

    # Create package directory
    os.makedirs(package_name, exist_ok=True)

    # Generate setup.py
    generate_file('setup.py.template', f'{package_name}/setup.py', {
        'package_name': package_name,
        'maintainer': maintainer,
        'maintainer_email': maintainer_email,
        'description': description
    })

    # Generate package.xml
    generate_file('package.xml.template', f'{package_name}/package.xml', {
        'package_name': package_name,
        'maintainer': maintainer,
        'maintainer_email': maintainer_email,
        'description': description
    })