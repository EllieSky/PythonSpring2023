import unittest

from fixtures.base_fixture import AdminLoginFixture


class MyTestCase(AdminLoginFixture):
    def test_open_localization_using_menu(self):
        self.main_menu.view_admin_localization()

        self.assertEqual(self.admin_local.HEADER, self.admin_local.get_header())
        self.assertEqual(self.admin_local.PAGE_URL, self.browser.current_url)


if __name__ == '__main__':
    unittest.main()
