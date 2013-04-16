from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Events Functional Tests

class EventsTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_event_via_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        # admin user
        username_field.send_keys("admin")
        password_field= self.browser.find_element_by_name("password")
        # admin user password
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        #self.assertIn('Latech administration', body.text)
        #self.fail('finish this test')
        event_links = self.browser.find_elements_by_link_text('Events')
        self.assertEquals(len(event_links), 2)
        event_links[1].click()

        #body = self.browser.find_element_by_tag_name('body')
        #self.assertIn('Events are not created yet.', body.text)

        #new_event_link = self.browser.find_elements_by_link_text('Add event')
        #new_event_link.click()

