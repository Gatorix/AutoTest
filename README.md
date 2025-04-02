# Zhang Wu You Automation Testing Project
## Development Environment
- python 3.8
- Refer to requirements.txt for others

## Continuous Integration
- Jenkins 2.361.x LTS

## Framework Description
- The framework adopts a PO model design, divided into three layers: Base, Page, Case
  - Base Layer
    - Login: Encapsulates the manager and accountant login interfaces
    - Actions: Inherits from SeleniumBase, optimizes test case post-steps, browser initialization, file download, and other functions
    - Elements: XPath positioning of page elements
  - Page Layer
    - Inherits from the Base layer, combining actions and elements
  - Case Layer
    - Inherits from the Page layer, combining operations on various page elements into complete test cases
- Test Case Writing Specifications
  - **Do not write absolute XPath paths in the base layer**
  - Try to write comments for unconventional operations in the page layer
  - Use allure to mark the functionality to which the test case belongs (epic, feature, story, tag)
  - Use allure.title to mark the test case title
  - Use allure.step to mark the test case steps as detailed as possible
  - Test cases are managed through pytest.mark grouping, **each test case must have at least one mark**
- Other Functions of the Framework
  - Excel file comparison, supporting xls and xlsx
  - PDF text extraction
- Test Case Execution
  - Local debugging execution environment: Modify DEFAULT_TEST_ENV in config.py
  - Command line parameters
    - Use mark: pytest -m [mark]
    - Use test case path: pytest [test case path]
    - Enable multi-threading: -n [number of threads (auto by default)]
    - Retry on failure: --reruns [number of retries]
- Logging
  - Use the logging module, managed through a yml configuration file; UI automation test cases only have login logs, while interface test cases have all logs for login and interface requests
- Test Report
  - After the test case execution is completed, the test results are saved in the allure\allure_result\{build id} folder, and detailed reports can be viewed in the corresponding build in Jenkins

## Directory Structure
- allure
  - allure_result: Stores test results
    - Execute test cases and save test results: pytest -s testcases/test.py --alluredir=allure/allure_result --clean-alluredir -n auto
  - allure_report: Stores test reports
    - Generate test reports: allure generate allure/allure_result -o allure/allure_report -c
    - View test reports: allure serve allure/allure_report
- backup
  - Accountant backup account sets
- base
  - base_case: 
    - BaseTestCase inherits from BaseCase, all page classes must inherit from this class
    - Defines global teardown, saving screenshots to allure result when a test case fails
    - Overrides driver, supporting chrome, firefox, edge, ie
    - Supplements BaseCase functionality
  - base_cookies: Used to obtain manager and accountant login cookies
  - base_login: Zhang Wu You login page element xpath
  - accounting/manager: Encapsulates page element xpath
- common: Defines exception classes
- config
  - environment.yml: Environment configuration information
  - config.py: Global variables
  - logging.yml: Log configuration file
- download_tmp: Stores temporary files downloaded during test case execution
- page: Page classes
  - web_ui
    - manager: Stores manager page classes
    - accounting: Stores accountant page classes
  - api
    - manager: Encapsulates commonly used manager interfaces
    - accounting: Encapsulates commonly used accountant interfaces
- template: Stores excel template files for file comparison
- testcases
  - web_ui
    - manager: Stores manager test cases
    - accounting: Stores accountant test cases
  - api
    - manager: Stores manager interface test cases
    - accounting: Stores accountant interface test cases
- utils: Encapsulates other tools
- jenkins_config.bat: Batch script in Jenkins
- pytest.ini: Defines test case marks
- requirements.txt: Dependency list
- run.py: Test case launcher

## Jenkins Related
- Disable CSRF
  - hudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true
