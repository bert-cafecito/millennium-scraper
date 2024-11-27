# Millennium Scraper

Millennium Scraper is a Scrapy project designed to scrape Yu-Gi-Oh! card data.

## Data Sources

This project scrapes data from the following sources:

1. [**Yu-Gi-Oh! Card Database**](https://www.db.yugioh-card.com/yugiohdb/): The official database for all Yu-Gi-Oh! cards, providing comprehensive information about each card, including card name, type, attribute, level/rank, attack/defense points, and card text.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bert-cafecito/millennium-scraper.git
    cd millennium-scraper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Importance of Creating a Virtual Environment

Creating a virtual environment is an important step in managing dependencies for your project. Here are some key reasons why:

1. **Dependency Management**: A virtual environment allows you to manage project-specific dependencies without interfering with the global Python installation. This ensures that the dependencies required for your project do not conflict with those of other projects.

2. **Isolation**: Each virtual environment is isolated from others, meaning you can have different versions of the same package in different projects. This is particularly useful when working on multiple projects that require different versions of a library.

3. **Reproducibility**: By using a virtual environment, you can ensure that your project runs with the exact dependencies specified in your `requirements.txt` file. This makes it easier to reproduce the development environment on different machines, which is crucial for collaboration and deployment.

4. **Ease of Use**: Virtual environments are easy to create and manage using tools like `venv` or `virtualenv`. They integrate seamlessly with package managers like `pip`, making it straightforward to install and update dependencies.

5. **Security**: Isolating dependencies in a virtual environment can also enhance security by reducing the risk of dependency conflicts and ensuring that your project uses only the packages it needs.

## Configuration

This project uses environment variables to configure various settings. You can set these variables in a `.env` file in the root directory of the project. An example `.env` file is provided as `.env.example`.

    ```properties
    BOT_NAME=millennium_scraper
    CONCURRENT_REQUESTS_PER_IP=8
    DOWNLOAD_DELAY=0
    LOG_ENABLED=True
    LOG_FILE=logs/scrapy.log
    LOG_LEVEL=INFO
    ROBOTSTXT_OBEY=True
    TELNETCONSOLE_ENABLED=False
    USER_AGENT=millennium_scraper (+https://github.com/bert-cafecito/millennium-scraper)
    ```

### Using the .env File

1. Copy the .env.example file to .env:
    ```sh
    cp .env.example .env
    ```

2. Modify the .env file to suit your needs.

The environment variables in the .env file will be loaded automatically when you run the project.

## Usage

### Crawling Responsibly

When scraping websites, it is important to do so responsibly to avoid overloading the server and to respect the website's terms of service. Here are some guidelines to follow:

1. **Identify Yourself**: Use a custom `User-Agent` string to identify your scraper. This helps website administrators understand who is accessing their site. You can set this in the `settings.py` file:
    ```python
    USER_AGENT = "millennium_scraper (+https://github.com/bert-cafecito/millennium-scraper)"
    ```

2. **Obey `robots.txt` Rules**: Respect the `robots.txt` file of the website you are scraping. This file contains rules about which parts of the site can be accessed by crawlers. You can enable this in the `settings.py` file:
    ```python
    ROBOTSTXT_OBEY = True
    ```

3. **Throttle Requests**: Avoid sending too many requests in a short period. Use the `DOWNLOAD_DELAY` setting to introduce a delay between requests:
    ```python
    DOWNLOAD_DELAY = 3  # Delay in seconds
    ```

4. **Limit Concurrent Requests**: Limit the number of concurrent requests to the same domain or IP address:
    ```python
    CONCURRENT_REQUESTS_PER_DOMAIN = 8
    CONCURRENT_REQUESTS_PER_IP = 8
    ```

5. **Handle Errors Gracefully**: Implement error handling to manage failed requests and avoid repeatedly hitting the server with the same request.

By following these guidelines, you can ensure that your scraping activities are respectful and do not negatively impact the websites you are accessing.

### What is a Spider?

In the context of Scrapy, a spider is a class that you define to scrape information from a website (or a group of websites). Spiders contain the logic for navigating through the website and extracting the data you need. Each spider is responsible for a specific site (or a group of sites).

### Spiders

This project contains the following spiders:

1. **YugiohDBCardsSpider**: Scrapes card details from the Yu-Gi-Oh! Card Database. You can find the implementation in [`millennium_scraper.spiders.yugiohdb`](millennium_scraper/spiders/yugiohdb.py).

To list all available spiders, use the following command:

```sh
scrapy list
```

### Running the Spiders

To run the spiders, use the following command:

```sh
scrapy crawl yugiohdb_cards
```

### Outputs

The outputs of the spiders will be saved in the `outputs` directory. For example, the `YugiohDBCardsSpider` will save its output in `outputs/yugiohdb/cards.json`.

### Logs

The outputs of the spiders will be saved in the `logs` directory. For example, the `YugiohDBCardsSpider` will save its logs in `logs/yugiohdb/cards.json`.


## Development

To contribute to the development of this project, follow these steps:

1. **Fork the Repository**: Fork the [Millennium Scraper repository](https://github.com/bert-cafecito/millennium-scraper) to your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine:
    ```sh
    git clone https://github.com/<your-username>/millennium-scraper.git
    cd millennium-scraper
    ```

3. **Create a Virtual Environment**: Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install Dependencies**: Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. **Create a Branch**: Create a new branch for your feature or bug fix:
    ```sh
    git checkout -b feature-or-bugfix-name
    ```

6. **Make Changes**: Make your changes to the codebase.

7. **Commit Changes**: Commit your changes with a descriptive commit message:
    ```sh
    git add .
    git commit -m "Description of the changes"
    ```

8. **Push Changes**: Push your changes to your forked repository:
    ```sh
    git push origin feature-or-bugfix-name
    ```

9. **Create a Pull Request**: Open a pull request to the main repository. Provide a detailed description of your changes and any relevant information.

### Note on Development Container

This project includes a `.devcontainer` configuration for Visual Studio Code. If you are using VS Code, you can open the project in a development container to ensure a consistent development environment. The container will automatically install the required dependencies specified in the `requirements.txt` file.

We appreciate your contributions to the project!

## Support

If you encounter any issues or have questions about the Millennium Scraper project, please feel free to reach out for support. Here are some ways you can get help:

### Reporting Issues

If you find a bug or have a feature request, please open an issue on the [GitHub Issues](https://github.com/bert-cafecito/millennium-scraper/issues) page. Provide as much detail as possible to help us understand and resolve the issue quickly.

### Star the Repository

If you find this project useful, please consider starring the repository on GitHub. Starring a repository helps increase its visibility and lets others know that the project is valuable. It also provides motivation and support to the maintainers to continue improving the project.

We appreciate your feedback and contributions to the project!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.