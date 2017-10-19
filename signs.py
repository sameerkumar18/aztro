import requests
import pytz
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from utils import _setup_debug_logger

SERVER_TIMEZONE = 'America/New_York'
TIMEDELTA_DAYS = {
    'yesterday': -1,
    'today': 0,
    'tomorrow': 1
}

logger = _setup_debug_logger(__name__)


def get_day_based_on_tz(arg_day, tz):
    """Gets the client date() based on tz passed as parameter.
    """
    server_day = datetime.now(tz=pytz.timezone(SERVER_TIMEZONE))
    day = 'today'
    if tz is not None and tz in pytz.all_timezones:
        client_day = server_day.astimezone(pytz.timezone(tz)).date()
        # else not necessary, same day
        asked = TIMEDELTA_DAYS[arg_day]
        asked_date = client_day + timedelta(days=asked)
        if asked_date > server_day.date():
            day = 'tomorrow'
        elif asked_date < server_day.date():
            day = 'yesterday'
    return day


def getData(sign, day, tz=None):
    """Endpoint to parse data from astrology site.
    """
    day = get_day_based_on_tz(day, tz)
    try:
        base_url = "http://astrology.kudosmedia.net/m/"
        payload = {'day': str(day)}

        data = requests.get(str(base_url) + str(sign), params=payload)
        soup = BeautifulSoup(str(data.content), 'lxml')

        date_range = str(
            soup.find("td", {"style": "vertical-align:middle;"}).text) \
            .partition("\n\n\t\t\t\t\t")[2] \
            .partition("\t\t\t\t")[0]
        current_date = soup.find(
            "p", {"style": "font-weight: bold; color: #336699;"}) \
            .text.partition(":")[2].replace("\t", "")

        description = soup.find("p", {"style": "color: #333333;"}).text

        details = soup.find(
            "ul",
            {"style": "margin: 0pt; padding: 0px; list-style-type: none;"
                      " list-style-image: none; list-style-position: outside;"
                      " color: #336699; font-size: 0.9em; "}).find_all("li")

        compatibility = details[0].text.partition(":")[2]
        mood = details[1].text.partition(":")[2]
        color = details[2].text.partition(":")[2]
        lucky_number = details[3].text.partition(":")[2]
        lucky_time = details[4].text.partition(":")[2]
        json_tbreturned = {
            'date_range': str(date_range),
            'current_date': str(current_date),
            'description': str(description),
            'compatibility': str(compatibility),
            'mood': str(mood),
            'color': str(color),
            'lucky_number': str(lucky_number),
            'lucky_time': str(lucky_time)
        }
        return json_tbreturned
    except Exception as e:
        logger.error("{}".format(e))
        return str('<div>null <br> Try Again? <br> Seems to be some kind of problem in the parameters :) </div>')
