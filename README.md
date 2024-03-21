# WikiSearch

WikiSearch is a command-line tool that allows users to search and view Wikipedia articles directly from the terminal.

![WikiSearch](images/wikisearch.png)

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/WikiSearch.git
    ```

2. Navigate to the project directory:

    ```
    cd WikiSearch
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```
    python wikisearch.py
    ```

2. You will be greeted with a colorful banner and prompted to enter a search query.

3. Type any topic and press Enter. The tool will search Wikipedia for articles related to your query.

4. If search results are found, they will be displayed along with their indices.

5. Enter the number corresponding to the article you want to view, or enter `0` to search again.

6. The summary of the selected article will be displayed.

7. To exit the program, type `exit` when prompted for a search query.

## Dependencies

- Python 3.x
- mediawiki library

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
