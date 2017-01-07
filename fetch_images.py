import requests
from bs4 import BeautifulSoup


def take_snapshot_from_camera(camera_name):
    base_url = 'http://www.gddkia.gov.pl'
    cameras_suffix = '/pl/22'

    return _get_image(
        _direct_link_to_image(
            link_to_camera=_direct_link_to_camera(camera_name=camera_name,
                                                  base_url=base_url,
                                                  all_cameras_suffix=cameras_suffix),
            base_url=base_url
        )
    )


def _direct_link_to_camera(camera_name, base_url, all_cameras_suffix):
    main_page = requests.get(base_url + all_cameras_suffix)
    as_soup = BeautifulSoup(main_page.text, "html.parser")
    camera_anchor = as_soup.find('a', {'class': 'punkt'}, text=camera_name)
    return base_url + camera_anchor['href']


def _direct_link_to_image(link_to_camera, base_url):
    camera_page = requests.get(link_to_camera)
    as_soup = BeautifulSoup(camera_page.text, "html.parser")
    img_element = as_soup.find('img', {'class': 'camera'})
    absolute_url_or_suffix = img_element['src']
    return absolute_url_or_suffix if absolute_url_or_suffix.startswith('http') else base_url + absolute_url_or_suffix


def _get_image(url):
    return requests.get(url).content
