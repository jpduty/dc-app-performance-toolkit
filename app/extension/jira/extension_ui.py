def app_specific_action(webdriver, datasets):
    issue_page = Issue(webdriver, issue_key=datasets['issue_key'])

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:view_pagerduty_sidebar")
        def sub_measure():
            issue_page.go_to()
            issue_page.wait_for_page_loaded()
            issue_page.wait_until_available_to_switch((By.ID, "pagerudty-addon-issue-sidebar-iframe"))
            issue_page.wait_until_visible((By.CLASS_NAME, "issue-sidebar-footer"))  
            issue_page.return_to_parent_frame()
        sub_measure()
    measure()
