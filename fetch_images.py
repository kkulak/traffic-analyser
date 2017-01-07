import requests
from bs4 import BeautifulSoup


def take_snapshot_from_camera(camera_name):
    return _get_image(
        _direct_link_to_image(
            _direct_link_to_camera(camera_name=camera_name,
                                   base_url='http://www.gddkia.gov.pl',
                                   all_cameras_suffix='/pl/22')
        )
    )


def _direct_link_to_camera(camera_name, base_url, all_cameras_suffix):
    main_page = requests.get(base_url + all_cameras_suffix)
    as_soup = BeautifulSoup(main_page.text, "html.parser")
    camera_anchor = as_soup.find('a', {'class': 'punkt'}, text=camera_name)
    return base_url + camera_anchor['href']


def _direct_link_to_image(link_to_camera):
    camera_page = requests.get(link_to_camera)
    as_soup = BeautifulSoup(camera_page.text, "html.parser")
    img_element = as_soup.find('img', {'class': 'camera'})
    return img_element['src']


def _get_image(url):
    return requests.get(url).content
