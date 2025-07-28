# pytest-saucedemo

Demo python test automation suite using [pytest](https://pytest.org/) and [Playwright](https://playwright.dev/python/) for testing of [saucedemo.com](https://www.saucedemo.com/)

## Features
 - Automated login tests
 - UI assertions for menus and products
 - [Coming Soon] Parameterized tests for randomization and error handling

## Setup 

1. Clone the repo:
    ```sh
    git clone https://github.com/<your-username>/pytest-saucedemo.git
    cd pytest-saucedemo
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    python -m playwright install
    ```
    
## Running Tests

```sh
pytest
```

## Tech Stack

- Python
- pytest
- Playwright
