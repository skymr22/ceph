Simplemail
==========

Simplemail is a module to send an email message from localhost


Enabling
--------

The module is enabled with::

  ceph mgr module enable simplemail


Configuration
-------------

sending from localhost requires the local SMTP server to be configured for to allow sending to remote servers for example using exim or dovecot. Without this it will raise a connection refused error.

The recipient email address(es) can either be specified in two ways:

* the config.py file in the sendmail module mgr directory or

* putting in the addresses directly with the command as shown in the next section


Commands
--------

* If recipients are already specified in config.py

::

  ceph simplemail

* If no recipients specified in config.py

::

  ceph simplemail example@example.com

  *for a single recipient* or

::

  ceph simplemail example1@example.com,example2@example.com

  *for multiple recipients* (separated by a comma)
