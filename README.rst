NPC Generator
=============

Introduction
------------

A very generic NPC generator with lots of user defined data.  It should be:

 #. Something that generates a (nearly) ready to use NPCs.
 #. Something that generates interesting NPCs.
 #. Something that generates intricate NPCs.
 #. Something that is reusable between systems and settings all supported
    by simple configurations.
 #. Something that will help others which would include Unix, Windows, and web
    interfaces as well as (possibly) an app and an API/library so it can be 
    used within other projects. 
 #. The code is in Python, the data is plain text.

Example
-------

+---------------------+--------------------------------------------------------+
| What                | Description                                            |
+=====================+========================================================+
| Name                | **Madeira**; ♀ *Letícia* - ♂ *Itocravo*                |
+---------------------+--------------------------------------------------------+
| Personality         | (Promoter) Action oriented, logical problem solvers    |
+---------------------+--------------------------------------------------------+
| Demeanor            | Malevolent.                                            |
+---------------------+--------------------------------------------------------+
| Physical            | Amber eyes, black hair, and Asian complexion.          |
+---------------------+--------------------------------------------------------+
| Body type           | Average endomorph (hourglass).                         |
+---------------------+--------------------------------------------------------+
| Fear                | (Leaning) Claustrophobia, fear of enclosed spaces.     |
+---------------------+--------------------------------------------------------+
| Primary skills      | Smuggler (-2) Terrible.                                |
+---------------------+--------------------------------------------------------+
| Secondary skills    | Doctor (MD) (+5) Superb.                               |
+---------------------+--------------------------------------------------------+
| Hobby skills        | Police (+2) Fair.                                      |
+---------------------+--------------------------------------------------------+
| Major past event    | Prestige.                                              |
+---------------------+--------------------------------------------------------+
| Minor past event    | Law sympathies.                                        |
+---------------------+--------------------------------------------------------+

Based on the above, this background is but one posibility:

*The beautiful Dr Letícia Madeira was a prestigious pathologist in the
Police force.  She left under strange circumstances and was for a time a
local MD at a free clinique and is now trying to help by getting (read:
smuggling) drugs to those in need.  Sadly, she is rubbish at it and has
not been caught by either the Law or gangs because of her past Police
contacts. However, this cannot last...*


.. _`a little documentation goes a long way`: http://www.martinaspeli.net/articles/a-little-documentation-goes-a-long-way

Pull requests
-------------

When you make a pull request, please make sure that all your code has unit 
tests (100% test coverage), that it conforms to PEP8, and that it is fully 
documented.

Credits
-------

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template
