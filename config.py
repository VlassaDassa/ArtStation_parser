from requests_html import HTMLSession



DEFAULT_count_pages = 30
DEFAULT_page = 2

DEFAULT_height = 1080
DEFAULT_width = 1920

project_link = 'https://www.artstation.com/projects/_project_id_.json'
channel_url = 'https://www.artstation.com/api/v2/community/channels/projects.json?channel_id=_channel_id_&page=_page_&sorting=_sort_&dimension=all&per_page=_count_pages_'
all_projects_url = 'https://www.artstation.com/api/v2/community/explore/projects/_sort_.json?page=_page_&dimension=all&per_page=_count_page_'
search_url = 'https://www.artstation.com/api/v2/search/projects.json'


path_to_old_links = './old_links.txt'
path_to_images = './images'

tags = []

sort = 'trending'
# sort = 'latest'
# sort = 'popular' 
# sort = 'community'

session = HTMLSession()

# Протестить get_response
# Наверное нужно как-то внедрить поиск по фильтрам/категории/все. Все ресурсы для этого есть

cookies = {
    'PRIVATE-CSRF-TOKEN': 'RBWf7sU%2BqK%2FCuvwSd2bJViRSWQ3BjevN2JKewv1Ecl0%3D',
    'SLG_G_WPT_TO': 'ru',
    'SLG_GWPT_Show_Hide_tmp': '1',
    'SLG_wptGlobTipTmp': '0',
    'visitor-uuid': '3d8f4330-1366-42f9-9acb-b6b5c5e576bb',
    'referrer-host': 'yandex.ru',
    'g_state': '{"i_p":1716238269291,"i_l":3}',
    '__cf_bm': 'tvTGTEJrObG_ZBjrlcZBpnncYe39xwLMbLijhRwyH9o-1715686545-1.0.1.1-Sx9sDDQzi2OLaFH4Kq1ZDeXZ4mgTS9FpZIhJNPljkDHNhPTMRplZW5faFPRR_O3LJ2ZPiZwNEKSnfiZHQyf1lwN37ynacqHw8snFMDSlLhk',
    '_ArtStation_session': 'TVZ4cGpjUFlwT0FzQWpZNXBZeXlRK00zMFcxOTl2TUpYaGJFUkEvdk1NMnp3NHE0M2xzUEhRRExPNDZTTE50UXBvYUU0OGtkNlp2ZkY3VkVtWVF2cnY0TlpwNXpUcHkycEN3Z21BQlVyT2dLQWpFWTdsR1NrU0RORmxDN0IrMkxtYWZCSFlCUC9lcHcrWkc3cnVxczFnPT0tLVd6M0lYbUZtZTZMMXg2WHdLamtKeHc9PQ%3D%3D--a6376cee8b87fc9bc5e813bc94becd606fd18f35',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.artstation.com',
    'public-csrf-token': '5lw0i3Pz8r3FSuChKvbcQy1tlOAT+OU/o4e/omTxbbOiSatlts1aEgfwHLNdkBUVCT/N7dJ1DvJ7FSFgmbUf7g==',
    'referer': 'https://www.artstation.com/search?sort_by=relevance&tags_include=Concept%20Art,Lighting',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition Yx GX 03)',
}

search_data = {
    'query': '',
    'page': 1,
    'per_page': 50,
    'sorting': 'relevance',
    'pro_first': '1',
    'filters': [
        {
            'field': 'tags',
            'method': 'include',
            'value': [
                'Concept Art',
                'Lighting',
            ],
        },
    ],
    'additional_fields': [],
}

categories = {
    "total_count": 60,
    "data": [
        {
            "id": 70,
            "name": "Abstract",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/070/20200605094018/thumb/thumb.jpg?1591368018",
            "uri": "abstract",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/070/20200605094018/thumb/thumb.jpg?1591368018",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 69,
            "name": "Anatomy",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/069/20221213144048/thumb/thumb.jpg?1670964048",
            "uri": "anatomy",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/icon_image/000/000/069/20230130125303/thumb/thumb.jpg?1675104783",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 71,
            "name": "Animals \u0026 Wildlife",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/071/20200505104307/thumb/thumb.jpg?1588693387",
            "uri": "animals_wildlife",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/071/20200505104307/thumb/thumb.jpg?1588693387",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 72,
            "name": "Anime \u0026 Manga",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/072/20200505105925/thumb/thumb.jpg?1588694365",
            "uri": "anime_manga",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/072/20200505105925/thumb/thumb.jpg?1588694365",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 101,
            "name": "Architectural Concepts",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/101/20200506153102/thumb/thumb.jpg?1588797062",
            "uri": "architectural_concepts",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/101/20200506153102/thumb/thumb.jpg?1588797062",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 73,
            "name": "Architectural Visualization",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/073/20200505111414/thumb/thumb.jpg?1588695254",
            "uri": "architectural_visualization",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/073/20200505111414/thumb/thumb.jpg?1588695254",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 5
        },
        {
            "id": 128,
            "name": "Automotive",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/128/20200921120322/thumb/thumb.jpg?1600707802",
            "uri": "automotive",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/128/20200921120322/thumb/thumb.jpg?1600707802",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 6
        },
        {
            "id": 103,
            "name": "Board and Card Game Art",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/103/20221213133129/thumb/thumb.jpg?1670959889",
            "uri": "board_and_card_game_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/103/20221213133129/thumb/thumb.jpg?1670959889",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 104,
            "name": "Book Illustration",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/104/20200505112310/thumb/thumb.jpg?1588695790",
            "uri": "book_illustration",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/104/20200505112310/thumb/thumb.jpg?1588695790",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 1
        },
        {
            "id": 105,
            "name": "Character Animation",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/105/20200505112355/thumb/thumb.jpg?1588695835",
            "uri": "character_animation",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/105/20200505112355/thumb/thumb.jpg?1588695835",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 3
        },
        {
            "id": 74,
            "name": "Character Design",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/074/20200505132748/thumb/thumb.jpg?1588703268",
            "uri": "character_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/074/20200505132748/thumb/thumb.jpg?1588703268",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 75,
            "name": "Character Modeling",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/075/20200505133346/thumb/thumb.jpg?1588703626",
            "uri": "character_modeling",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/075/20200505133346/thumb/thumb.jpg?1588703626",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 77,
            "name": "Children's Art",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/077/20200505141007/thumb/thumb.jpg?1588705807",
            "uri": "childrens_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/077/20200505141007/thumb/thumb.jpg?1588705807",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 78,
            "name": "Comic Art",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/078/20221213135111/thumb/thumb.jpg?1670961071",
            "uri": "comic_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/icon_image/000/000/078/20221213135211/thumb/thumb.jpg?1670961131",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 84,
            "name": "Cover Art",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/084/20200505142912/thumb/thumb.jpg?1588706952",
            "uri": "cover_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/084/20200505142912/thumb/thumb.jpg?1588706952",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 8
        },
        {
            "id": 80,
            "name": "Creatures \u0026 Monsters",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/080/20221213135848/thumb/thumb.jpg?1670961528",
            "uri": "creatures_and_monsters",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/080/20221213135848/thumb/thumb.jpg?1670961528",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 76,
            "name": "Editorial Illustration",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/076/20200505161321/thumb/thumb.jpg?1588713201",
            "uri": "editorial_illustration",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/076/20200505161321/thumb/thumb.jpg?1588713201",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 81,
            "name": "Environmental Concept Art \u0026 Design",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/081/20200505141625/thumb/thumb.jpg?1588706185",
            "uri": "environmental_concept_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/081/20200505141625/thumb/thumb.jpg?1588706185",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 82,
            "name": "Fan Art",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/082/20200505142057/thumb/thumb.jpg?1588706457",
            "uri": "fan_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/082/20200505142057/thumb/thumb.jpg?1588706457",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 83,
            "name": "Fantasy",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/083/20221213135330/thumb/thumb.jpg?1670961210",
            "uri": "fantasy",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/083/20221213135330/thumb/thumb.jpg?1670961210",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 9
        },
        {
            "id": 106,
            "name": "Fashion \u0026 Costume Design",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/106/20200722082416/thumb/thumb.jpg?1595424256",
            "uri": "fashion_and_costume_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/106/20200722082416/thumb/thumb.jpg?1595424256",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "description": "Explore artwork that showcases fashion and clothing design. See armour, costumes, uniforms, and more related to the appearance of characters."
        },
        {
            "id": 85,
            "name": "Game Art",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/085/20200505143053/thumb/thumb.jpg?1588707053",
            "uri": "game_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/085/20200505143053/thumb/thumb.jpg?1588707053",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 2
        },
        {
            "id": 107,
            "name": "Gameplay \u0026 Level Design",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/107/20200505143242/thumb/thumb.jpg?1588707162",
            "uri": "gameplay_and_level_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/107/20200505143242/thumb/thumb.jpg?1588707162",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 108,
            "name": "Games and Real-Time 3D Environment Art",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/108/20200505143443/thumb/thumb.jpg?1588707283",
            "uri": "games_real-time_3d_environment",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/108/20200505143443/thumb/thumb.jpg?1588707283",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 87,
            "name": "Graphic Design",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/087/20200506085257/thumb/thumb.jpg?1588773177",
            "uri": "graphic_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/087/20200506085257/thumb/thumb.jpg?1588773177",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 109,
            "name": "Hard Surface",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/109/20200505163049/thumb/thumb.jpg?1588714249",
            "uri": "hard_surface",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/109/20200505163049/thumb/thumb.jpg?1588714249",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 86,
            "name": "Horror",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/086/20200505144044/thumb/thumb.jpg?1588707644",
            "uri": "horror",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/086/20200505144044/thumb/thumb.jpg?1588707644",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 88,
            "name": "Illustration",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/088/20200505144412/thumb/thumb.jpg?1588707852",
            "uri": "illustration",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/088/20200505144412/thumb/thumb.jpg?1588707852",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 89,
            "name": "Industrial \u0026 Product Design",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/089/20200505144756/thumb/thumb.jpg?1588708076",
            "uri": "industrial_and_product_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/089/20200505144756/thumb/thumb.jpg?1588708076",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 90,
            "name": "Lighting",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/090/20200505144911/thumb/thumb.jpg?1588708151",
            "uri": "lighting",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/090/20200505144911/thumb/thumb.jpg?1588708151",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 91,
            "name": "Matte Painting",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/091/20200505145111/thumb/thumb.jpg?1588708271",
            "uri": "matte_painting",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/091/20200505145111/thumb/thumb.jpg?1588708271",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 92,
            "name": "Mecha",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/092/20200505145646/thumb/thumb.jpg?1588708606",
            "uri": "mecha",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/092/20200505145646/thumb/thumb.jpg?1588708606",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 110,
            "name": "Mechanical Design",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/110/20200505145520/thumb/thumb.jpg?1588708520",
            "uri": "mechanical_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/110/20200505145520/thumb/thumb.jpg?1588708520",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 111,
            "name": "Motion Graphics",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/111/20200505150123/thumb/thumb.jpg?1588708883",
            "uri": "motion_graphics",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/111/20200505150123/thumb/thumb.jpg?1588708883",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 112,
            "name": "Photogrammetry \u0026 3D Scanning",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/112/20200505150309/thumb/thumb.jpg?1588708989",
            "uri": "photogrammetry_3d_scanning",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/112/20200505150309/thumb/thumb.jpg?1588708989",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 93,
            "name": "Pixel \u0026 Voxel",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/093/20200505150401/thumb/thumb.jpg?1588709041",
            "uri": "pixel_voxel",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/093/20200505150401/thumb/thumb.jpg?1588709041",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 113,
            "name": "Portraits",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/113/20200505150619/thumb/thumb.jpg?1588709179",
            "uri": "portraits",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/113/20200505150619/thumb/thumb.jpg?1588709179",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 94,
            "name": "Props",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/094/20200505150754/thumb/thumb.jpg?1588709274",
            "uri": "props",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/094/20200505150754/thumb/thumb.jpg?1588709274",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 114,
            "name": "Realism",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/114/20200505150951/thumb/thumb.jpg?1588709391",
            "uri": "realism",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/114/20200505150951/thumb/thumb.jpg?1588709391",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 8064,
            "name": "RealityScan",
            "image_url": None,
            "uri": "Reality",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": None,
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 7,
            "description": "RealityScan"
        },
        {
            "id": 95,
            "name": "Science Fiction",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/095/20200505151104/thumb/thumb.jpg?1588709464",
            "uri": "science_fiction",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/095/20200505151104/thumb/thumb.jpg?1588709464",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 115,
            "name": "Scientific Illustration \u0026 Visualization",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/115/20200505151501/thumb/thumb.jpg?1588709701",
            "uri": "scientific_visualization",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/115/20200505151501/thumb/thumb.jpg?1588709701",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 116,
            "name": "Scripts \u0026 Tools",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/116/20200505151829/thumb/thumb.jpg?1588709909",
            "uri": "scripts_tools",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/116/20200505151829/thumb/thumb.jpg?1588709909",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 117,
            "name": "Sketches",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/117/20200505151934/thumb/thumb.jpg?1588709974",
            "uri": "sketches",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/117/20200505151934/thumb/thumb.jpg?1588709974",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 118,
            "name": "Still Life",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/118/20200505152214/thumb/thumb.jpg?1588710134",
            "uri": "still_life",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/118/20200505152214/thumb/thumb.jpg?1588710134",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 96,
            "name": "Storyboards",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/096/20200722085432/thumb/thumb.jpg?1595426072",
            "uri": "storyboards",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/096/20200722085432/thumb/thumb.jpg?1595426072",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 119,
            "name": "Stylized",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/119/20200505155012/thumb/thumb.jpg?1588711812",
            "uri": "stylized",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/119/20200505155012/thumb/thumb.jpg?1588711812",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 120,
            "name": "Technical Art",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/120/20200505155804/thumb/thumb.jpg?1588712284",
            "uri": "technical_art",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/120/20200505155804/thumb/thumb.jpg?1588712284",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 97,
            "name": "Textures \u0026 Materials",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/097/20200505154041/thumb/thumb.jpg?1588711241",
            "uri": "textures_materials",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/097/20200505154041/thumb/thumb.jpg?1588711241",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 121,
            "name": "Toys \u0026 Collectibles",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/121/20200505154250/thumb/thumb.jpg?1588711370",
            "uri": "toys_collectibles",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/121/20200505154250/thumb/thumb.jpg?1588711370",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 98,
            "name": "Tutorials",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/098/20200505154419/thumb/thumb.jpg?1588711459",
            "uri": "tutorials",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/098/20200505154419/thumb/thumb.jpg?1588711459",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 127,
            "name": "Unreal Engine",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/127/20221213134653/thumb/thumb.jpg?1670960813",
            "uri": "unreal",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/127/20221213134653/thumb/thumb.jpg?1670960813",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 0,
            "description": "Unreal Engine is the world’s most open and advanced real-time 3D creation tool. Continuously evolving to serve not only its original purpose as a state-of-the-art game engine, today it gives creators across industries the freedom and control to deliver cutting-edge content, interactive experiences, and immersive virtual worlds. "
        },
        {
            "id": 99,
            "name": "User Interface",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/099/20200505154703/thumb/thumb.jpg?1588711623",
            "uri": "user_interface",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/099/20200505154703/thumb/thumb.jpg?1588711623",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 100,
            "name": "Vehicles",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/100/20200505154900/thumb/thumb.jpg?1588711740",
            "uri": "vehicles",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/100/20200505154900/thumb/thumb.jpg?1588711740",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 122,
            "name": "VFX for Film, TV \u0026 Animation ",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/122/20200505155429/thumb/thumb.jpg?1588712069",
            "uri": "vfx_for_film_tv_animation",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/122/20200505155429/thumb/thumb.jpg?1588712069",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 123,
            "name": "VFX for Real-Time \u0026 Games",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/123/20200505155506/thumb/thumb.jpg?1588712106",
            "uri": "vfx_for_realtime_and_games",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/123/20200505155506/thumb/thumb.jpg?1588712106",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 124,
            "name": "Virtual and Augmented Reality",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/124/20200505160051/thumb/thumb.jpg?1588712451",
            "uri": "virtual_and_augmented_reality",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/124/20200505160051/thumb/thumb.jpg?1588712451",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None,
            "favorite_position": 4
        },
        {
            "id": 125,
            "name": "Visual Development",
            "image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/125/20200505160217/thumb/thumb.jpg?1588712537",
            "uri": "visual_development",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdnb.artstation.com/p/channels/covers/000/000/125/20200505160217/thumb/thumb.jpg?1588712537",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 126,
            "name": "Weapons",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/126/20200505160937/thumb/thumb.jpg?1588712977",
            "uri": "weapons",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/126/20200505160937/thumb/thumb.jpg?1588712977",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        },
        {
            "id": 102,
            "name": "Web and App Design",
            "image_url": "https://cdna.artstation.com/p/channels/covers/000/000/102/20200505161153/thumb/thumb.jpg?1588713113",
            "uri": "web_app_design",
            "state": "published",
            "featured": False,
            "type": "global",
            "icon_image_url": "https://cdna.artstation.com/p/channels/covers/000/000/102/20200505161153/thumb/thumb.jpg?1588713113",
            "is_ad": False,
            "advertiser": None,
            "advertisement_paid_by": None
        }
    ]
}
