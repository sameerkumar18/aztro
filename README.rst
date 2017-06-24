
#################################
Welcome to aztro's documentation!
#################################

.. image:: https://image.ibb.co/n3vNXk/aztro.jpg
   :height: 300px
   :width: 300px
   :alt: aztro api logo
   :align: center

What is aztro?
==============
aztro is a REST API made with Flask that provides you with daily horoscope (today, tomorrow and yesterday).
Feel free to contribute on `Github <http://github.com/sameerkumar18/aztro>`_.




Why aztro?
==========
aztro is perfect for a developer who wants an API that provides horoscope info for sun signs such as Lucky Number, Lucky Color, Mood, Color, Compatibility with other sun signs, description of a sign for that day etc.

URL
===
.. code-block:: python

    POST: https://aztro.herokuapp.com


Parameters
==========
sign : 
   Name of the sign.

   List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.


day : 
   Day can be today,tomorrow or yesterday


Usage
=====
.. code-block:: text

    POST: https://aztro.herokuapp.com?sign= :sign: &day= :day:


Example 
=======
The following example is for sun sign aries - 


cURL
^^^^
.. code-block:: python

    curl -X POST \
    'https://aztro.herokuapp.com/?sign=aries&day=today'


Python
^^^^^^
.. code-block:: python

    import requests

    params = (
    ('sign', 'aries'),
    ('day', 'today'),
    )

    requests.post('https://aztro.herokuapp.com/', params=params)


Node.js
^^^^^^^
.. code-block:: javascript

    var request = require('request');

    var options = {
    url: 'https://aztro.herokuapp.com/?sign=aries&day=today',
    method: 'POST'
    };

    function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
    }

    request(options, callback);


PHP
^^^
.. code-block:: php

    <?php
    include('vendor/rmccue/requests/library/Requests.php');
    Requests::register_autoloader();
    $headers = array();
    $response = Requests::post('https://aztro.herokuapp.com/?sign=aries&day=today', $headers);


Response
^^^^^^^^
.. code-block:: json

    {"current_date": "June 23, 2017", "compatibility": " Cancer", "lucky_time": " 7am",
     "lucky_number": " 64", "color": " Spring Green", "date_range": "Mar 21 - Apr 20",
     "mood": " Relaxed", "description": "It's finally time for you to think about just
      one thing: what makes you happy. Fortunately, that happens to be a person who feels
      the same way. Give yourself the evening off. Refuse to be put in charge of anything."}



License
=======

Copyright 2017 Sameer Kumar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Contact
=======

Questions? Suggestions? Feel free to contact me at sameer18051998@gmail.com



Credits
=======

"aztro" was created by `Sameer Kumar <http://www.sameerkumar.website>`_. 
Other Contributors - 
    * Harshit Sahni (for the idea)

Source of horoscope updates - http://astrology.kudosmedia.net/

and if I have neglected to mention someone, please let me know.

Please feel free to use and adapt this small API.



.. image:: https://readthedocs.org/projects/aztro/badge/?version=latest
    :target: http://aztro.readthedocs.io/en/latest/?badge=latest


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
