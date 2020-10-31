try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


class DefaultPage:
	BASE_URL = 'http://virusmusic.fun'
	PATH = ''

	def __init__(self, driver):
		self.driver = driver

	def open(self):
		url = urlparse.urljoin(self.BASE_URL, self.PATH)
		self.driver.get(url)
		self.driver.maximize_window()


class Component:
	def __init__(self, driver):
		self.driver = driver
