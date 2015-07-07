# webconfig-php-pecl-mailparse

Forked version of webconfig-php-pecl-mailparse with ClearOS changes applied

## Update usage
  Add __#kojibuild__ to commit message to automatically build

* git clone git+ssh://git@github.com/clearos/webconfig-php-pecl-mailparse.git
* cd webconfig-php-pecl-mailparse
* git checkout epel7
* git remote add upstream git://pkgs.fedoraproject.org/php-pecl-mailparse.git
* git pull upstream epel7
* git checkout clear7
* git merge --no-commit epel7
* git commit
