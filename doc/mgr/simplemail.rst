Simplemail
==========

Simplemail is a module to send a preset email message from localhost


Enabling
--------

The module is enabled with::

  ceph mgr module enable simplemail


Configuration
-------------

sending from localhost requires the local SMTP server to be configured for to allow sending to remote servers for example using exim or dovecot.

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


Modification
------------

The module can be modified to send from a different server other than localhost among others. 
This can be done as per the smtplib documentation_.
.. _documentation: https://docs.python.org/2/library/smtplib.html


Limitations
-----------

In the current format, the email messages might be flagged as spam at destination
