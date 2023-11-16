import re
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox

class FacebookPostLinkExtractor:
    def __init__(self):
        self.pattern = re.compile(r'(value)*\w{9,11}[:"][:"]\d{15,17}')
        self.pattern2 = re.compile(r'value="(\d{15,16})"')
        self.pattern3 = re.compile(r'(id)*\w{15}')
        self.pattern4 = re.compile(r'"entity_id":"(\d{15,16})"')
        self.pattern5 = re.compile(r'fbid=(\w{15,16})')
        self.link_pattern = r'link href="https://www\.facebook\.com/[^/]+/posts/[^/]+/\d+/"'
        self.reel_pattern = r'link href="https://www\.facebook\.com/[^/]+/videos/[^/]+/\d+/"'
        self.complete_link_pattern = r'https://www\.facebook\.com/(\w*)/posts/(\d*)/'
        self.long_pattern = r'https://www\.facebook\.com/[^/]+/posts/[^/]+/\d+/"'
        self.permalink_pattern = r'story_fbid=(\d+)'
        self.id_pattern = r'"id":"(\d+)"'
        
    def get_facebook_post_link(self, link):
        link_types = {
            "watch?v=": self.extract_post_link_from_watch,
            "photo/?": self.extract_post_link_from_photo,
            "story.php?story_fbid=pfbid": self.extract_post_link_from_permalink,
            "reel": self.extract_post_link_from_reel,
            "permalink": self.extract_post_link_from_permalink,
            "story.php": self.extract_post_link_from_permalink,
        }
        for link_type, extractor in link_types.items():
            if link_type in link:
                try:
                    return extractor(link)
                except Exception as exc:
                    return str(exc)
        try:
            return self.extract_post_link_from_pfbid(link)
        except Exception as exc:
            return str(exc)
    
    def extract_post_link_from_permalink(self, link):
        link = link.replace("m.f", "www.f")
        res = requests.get(link)
        soup_data = BeautifulSoup(res.text, 'html.parser')
        
        link_match = re.search(self.permalink_pattern, soup_data.prettify())
        id_match = re.search(self.id_pattern, soup_data.prettify())
        
        if link_match:
            link = link_match.group()
            
            id_match = id_match.group()
            id = id_match.replace('"',"").split(':')[1]
            link2 = link.strip("'").split('=')[1]
            
            link3 = 'https://www.facebook.com/{}/posts/{}/'.format(id,link2)
            result = link3
        return result

    def extract_post_link_from_pfbid(self, link):
        link = link.replace("m.f", "www.f")
        res = requests.get(link)
        soup_data = BeautifulSoup(res.text, 'html.parser')
        
        match = re.search(self.complete_link_pattern, soup_data.prettify())


        if match:
            print(match.group())   ### Prints the whole link for testing purposes only.
            result = match.group()
        else:
            long_match = re.search(self.long_pattern, soup_data.prettify())
            long_match = long_match.group().split('/')
            result = 'https://www.facebook.com/{}/posts/{}/'.format(long_match[3],long_match[6].strip('"'))
        return result

    def extract_post_link_from_reel(self, link):
        res = requests.get(link)
        soup_data = BeautifulSoup(res.text, 'html.parser')
        match = re.search(self.reel_pattern, soup_data.prettify())
        if match:
            link = match.group()
            link2 = link.strip('link href=').strip('"').split('/')
            link3 = 'https://www.facebook.com/{}/videos/{}/'.format(link2[3], link2[6])
            result = link3
            return result
    
    def extract_post_link_from_watch(self, link):
        message = "This is a correct link, numeric ID is in the URL, process terminated."
        self.message_box("Warning", message)
        return link

    def extract_post_link_from_photo(self, link):
        message = "This is a correct link, numeric ID is in the URL, process terminated."
        self.message_box("Warning", message)
        return link
    
    def message_box(self, title,message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()