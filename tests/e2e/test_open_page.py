from .base_testcase import BaseTestCase


class TestLogin(BaseTestCase):
    """
    Test cases revolving around the logging in functionality of the site
    """
    def __init__(self, testname):
        super().__init__(testname, log_in=False)

    def test_sidebar_urls(self):
        self.log_in(user_id='instructor')
        self.click_class('sample')
        # self.get("/" + self.semester + "/sample/forum")
        pages = self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/aside/ul")
        pages = pages.find_elements_by_class_name("nav-row")
        urls = []
        for page in pages:
            urls.append(page.get_attribute("href"))
        print(urls)
        for url in urls:
            self.get(full_url=url)