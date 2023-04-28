from setuptools import setup, find_namespace_packages

setup(name='bot', 
      version='0.0.2',
      description='Bot',
      url='https://github.com/melser68/modul_7_task',
      author='melser68',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts':['bot = bot_2.0:__main__']}      
       )