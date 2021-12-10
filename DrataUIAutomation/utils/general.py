from py.path import local
import os
import configparser
from usp.tree import sitemap_tree_for_homepage

project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_config():
    config_file_Path = os.path.join(project_path, "./config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser

def get_setting(parent, key):
    config = get_config()
    return config.get(parent, key)


def getListUniquePages(listPagesRaw):
    listPages = []
    for page in listPagesRaw:
        if page in listPages:
            pass
        else:
            listPages.append(page)
    return listPages

def getPagesFromSitemap(fullDomain):
    listPagesRaw = []
    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPagesRaw.append(page.url)

    return getListUniquePages(listPagesRaw)
