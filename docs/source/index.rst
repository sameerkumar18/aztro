
#################################
Welcome to aztro's documentation!
#################################

.. image:: https://github.com/sameerkumar18/aztro/raw/master/aztro-bg.png
   :alt: aztro api logo
   :align: center

What is aztro?
==============
aztro REST API allows developers to access and integrate the functionality of aztro with other applications. The API retrieves daily horoscopes for yesterday, today, and tomorrow.

Feel free to contribute on `Github <http://github.com/sameerkumar18/aztro>`_.

Why aztro?
==========
aztro is for a developer who wants an API that provides horoscope info for sun signs such as Lucky Number, Lucky Color, Mood, Color, Compatibility with other sun signs, description of a sign for that day etc. 


.. toctree::
   :maxdepth: 4
   :titlesonly:


URL
===
.. code-block:: python

    POST: https://aztro.sameerkumar.website


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

    POST: https://aztro.sameerkumar.website?sign= <sign> &day= <day>


Example 
=======
Following example is for sign Aries


cURL
^^^^
.. code-block:: python

    curl -X POST \
    'https://aztro.sameerkumar.website/?sign=aries&day=today'


Python
^^^^^^
.. code-block:: python

    import requests

    params = (
    ('sign', 'aries'),
    ('day', 'today'),
    )

    requests.post('https://aztro.sameerkumar.website/', params=params)


Node.js
^^^^^^^
.. code-block:: javascript

    var request = require('request');

    var options = {
    url: 'https://aztro.sameerkumar.website/?sign=aries&day=today',
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

        //This fucntion can be used in any PHP framework like laravel, wordpress, drupal, cakephp etc.

        function aztro($sign, $day) {
            $aztro = curl_init('https://aztro.sameerkumar.website/?sign='.$sign.'&day='.$day);
            curl_setopt_array($aztro, array(
                CURLOPT_POST => TRUE,
                CURLOPT_RETURNTRANSFER => TRUE,
                CURLOPT_HTTPHEADER => array(
                    'Content-Type: application/json'
                )
            ));
            $response = curl_exec($aztro);
            if($response === FALSE){
                die(curl_error($aztro));
            }
            $responseData = json_decode($response, TRUE);
            return $responseData;
        }

        $ObjData = aztro('aries', 'today');
        var_dump($ObjData);

    ?>


Ajax
^^^^
.. code-block:: javascript

    $.ajax({
	 type:'POST',
	 url:'https://aztro.sameerkumar.website?sign=aries&day=today',
	 success:function(data){
	 console.log(data);
	 }
    });



ECMAScript (ES6)
^^^^^^
.. code-block:: javascript

    const URL = 'https://aztro.sameerkumar.website/?sign=aries&day=today';
    fetch(URL, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(json => {
        const date = json.current_date;
        console.log(date);
    });


Vue.JS using axios
^^^^^^
.. code-block:: html

    <ul id="aztro">
        <li>Current Date: {{data.current_date}}</li>
        <li>Compatibility: {{data.compatibility}}</li>
        <li>Lucky Number: {{data.lucky_number}}</li>
        <li>Lucky Time: {{data.lucky_time}}</li>
        <li>Color: {{data.color}}</li>
        <li>Date Range: {{data.date_range}}</li> 
        <li>Mood: {{data.mood}}</li>
        <li>Description: {{data.description}}</li>
    </ul>

.. code-block:: javascript

    const URL = 'https://aztro.sameerkumar.website/?sign=aries&day=today';
    new Vue({
        el: '#aztro',
        data() {
                return {
                data: {}
            }
        },
        created() {
            axios.post(URL).then((response) => {
                this.data = response.data
            })
        }
    })


ReactJS with ES6
^^^^^^
.. code-block:: jsx
    
    import React, { Component } from 'react';

    class Aztro extends Component {
        constructor(props){
            super(props);
            this.state = {
              json: {}
            }
        }
        
        componentDidMount () {
            const URL = 'https://aztro.sameerkumar.website/?sign=aries&day=today';
            fetch(URL, {
                method: 'POST'
            }).then(response => response.json())
            .then(json => { this.setState({json}); });
        }
        
        render() {
            return (
              <div>
                  Current Date: {this.state.json.current_date} <br />
                  Compatibility: {this.state.json.compatibility} <br />
                  Lucky Number: {this.state.json.lucky_number} <br />
                  Lucky Time: {this.state.json.lucky_time} <br />
                  Color: {this.state.json.color} <br />
                  Date Range: {this.state.json.date_range} <br />
                  Mood: {this.state.json.mood} <br />
                  Description: {this.state.json.description} <br />
              </div>
            );
        }
    }

    export default Aztro;


Response
^^^^^^^^
.. code-block:: json

    {"current_date": "June 23, 2017", "compatibility": " Cancer", "lucky_time": " 7am",
     "lucky_number": " 64", "color": " Spring Green", "date_range": "Mar 21 - Apr 20",
     "mood": " Relaxed", "description": "It's finally time for you to think about just
      one thing: what makes you happy. Fortunately, that happens to be a person who feels
      the same way. Give yourself the evening off. Refuse to be put in charge of anything."}



API Wrappers
============

For Python - `PyAztro <https://github.com/sameerkumar18/pyaztro>`_ (pip install pyaztro)

For NodeJS - `aztro-js <https://github.com/srijitcoder/aztro-js>`_ (npm install aztro-js)


License
=======

Copyright 2021 Sameer Kumar

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

Questions? Suggestions? Feel free to contact me at sam+aztro-docs@sameerkumar.website


Buy me a coffee 🥤
=====================

If this project help you reduce time to develop, please consider buying me a coffee :)

.. image:: https://media.giphy.com/media/513lZvPf6khjIQFibF/giphy.gif
    :target: https://www.buymeacoffee.com/sameerkumar



Credits
=======

"aztro" was created by `Sameer Kumar <https://sameerkumar.website>`_ and these awesome individual `contributors <https://github.com/sameerkumar18/aztro/graphs/contributors>`_

Source of horoscope updates - http://astrology.kudosmedia.net/

Please feel free to use and adapt this small API.



.. image:: https://readthedocs.org/projects/aztro/badge/?version=latest
    :target: https://aztro.readthedocs.io/en/latest/?badge=latest


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
