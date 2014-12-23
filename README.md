dreamhost-flask-project-template
================================

Dreamhost Shared Hosting Flask Project Template

Purpose
-------
This is the base setup I use specifically to launch new apps on Dreamhost's shared hosting plan (there are probably some optimizations that could be made to this). While this should work with other configurations as well, I have not tested in other environments.


Installation
------------
1. Setup your project domain in Dreamhost's web panel:
  - PHP 5.6.x FastCGI
  - Passenger Enabled (required!)
  - *Note: Dreamhost will default to using your domain as your app path, but you can change it to whatever you want. This value is referenced as `<DOMAIN PATH>` in these instructions as well as in your passenger_wsgi.py, and should be updated to the value you chose.*

2. Install newer version Python (optional - I used 3.4.2, but this works with 2.x as well)
    ```
    cd ~
    mkdir python
    cd python
    wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz
    tar xf Python-3.4.2.tar.xz
    cd Python-3.4.2
    ./configure --prefix=$HOME/python
    make
    make install
    echo 'export PATH=$HOME/python/bin:$PATH' >> ~/.bash_profile
    ```
  - log out and back in again - Python should default to the new installation
  - *Note: if you install python 3.x, use "python3" to start python*

3. Install a virtual environment
    ```
    cd ~
    wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-12.0.2.tar.gz
    tar xf virtualenv-12.0.2.tar.gz
    cd virtualenv-12.0.2
    python setup.py install
    *(or "python3 setup.py install" if you installed python 3.x)*
    cd ~
    mkdir env
    virtualenv env/wsgi
    ```
4. Install python libraries
5.
  ```
  source ~/env/wsgi/bin/activate
  pip install Flask
  ```

5. customize .bash_profile (Optional):

    ```
    # Restarts the Flask app
    alias restart='touch ~/<DOMAIN PATH>/tmp/restart.txt'
    alias main='cd ~/<DOMAIN PATH>/'

    # Activates virtualenv
    alias activate='source ~/env/wsgi/bin/activate'

    # Watch logs
    alias access='tail -500f ~/logs/<DOMAIN PATH>/http/access.log'
    alias error='tail -500f ~/logs/<DOMAIN PATH>/http/error.log'

    alias ls='ls --color=auto'

    # git
    alias gs='git status'
    alias gl='git log'

    # Shows what git branch i am currently on
    parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
    }
    export PS1="\[\033[00m\]\u@\h\[\033[01;34m\] \W \[\033[31m\]\$(parse_git_branch)
    \[\033[00m\]$\[\033[00m\] "
    ```

6. If the app doesn't start up automatically:

    ```
    touch ~/<DOMAIN PATH>/tmp/restart.txt
    ```

Author
------
Jonathan Prusik @jprusik [classynemesis.com](http://www.classynemesis.com)

License
-------
Dreamhost Shared Hosting Flask Project Template is released under the MIT License.
