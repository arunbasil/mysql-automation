# Project Title (Replace with Actual Project Title)

A brief description of what this project does.

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   **Python 3.x**: Download from [python.org](https://www.python.org/downloads/)
*   **Pip**: Usually comes with Python. If not, see [installing pip](https://pip.pypa.io/en/stable/installation/).
*   **Docker**: Required for running a local SQL Server instance. Download from [Docker Desktop](https://www.docker.com/products/docker-desktop).
*   **Microsoft ODBC Driver for SQL Server (macOS)**: This project uses `pyodbc` to connect to SQL Server, which requires this driver.
    *   Install using Homebrew:
        ```bash
        brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
        brew update
        brew install msodbcsql17 mssql-tools
        ```
        *(You may need to use `msodbcsql18` depending on your SQL Server version and preferences.)*
        For other operating systems, please refer to the official Microsoft documentation.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Set up SQL Server with AdventureWorks using Docker:**
    *   Pull the SQL Server image for Linux (works on Mac with Docker Desktop):
        ```bash
        docker pull mcr.microsoft.com/mssql/server:2019-latest # Or your preferred version
        ```
    *   Run the SQL Server container. Replace `YourStrongPassword!` with a strong password for the `SA` user. This password will be needed for the `config.ini`.
        ```bash
        docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourStrongPassword!" \
           -p 1433:1433 --name sqlserver_adventureworks -d \
           mcr.microsoft.com/mssql/server:2019-latest
        ```
    *   **Restore AdventureWorks Database:**
        *   Download the AdventureWorksLT2019.bak (or another version) backup file from [Microsoft's GitHub releases](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks).
        *   Copy the backup file into your running Docker container:
            ```bash
            docker cp /path/to/your/AdventureWorksLT2019.bak sqlserver_adventureworks:/var/opt/mssql/backup/AdventureWorksLT2019.bak
            ```
        *   Connect to the SQL Server instance inside Docker using `sqlcmd` (installed with `mssql-tools` or you can run it inside the container):
            ```bash
            sqlcmd -S localhost -U SA -P "YourStrongPassword!"
            ```
        *   Inside the `sqlcmd` prompt, run the following T-SQL commands:
            ```sql
            RESTORE DATABASE AdventureWorksLT2019
            FROM DISK = '/var/opt/mssql/backup/AdventureWorksLT2019.bak'
            WITH MOVE 'AdventureWorksLT2012_Data' TO '/var/opt/mssql/data/AdventureWorksLT2019.mdf',
            MOVE 'AdventureWorksLT2012_Log' TO '/var/opt/mssql/data/AdventureWorksLT2019_Log.ldf';
            GO
            ```
            *(Adjust filenames and paths if you used a different AdventureWorks version or backup file name.)*
            Type `EXIT` to leave `sqlcmd`.

3.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure the database connection:**
    *   Locate the `config/config.ini` file. It should look like this:
        ```ini
        [database]
        DRIVER={ODBC Driver 17 for SQL Server}
        SERVER=localhost,1433
        DATABASE=AdventureWorksLT2019 ; Or your AdventureWorks DB name
        UID=SA ; Or your SQL Server username
        PWD=YourStrongPassword! ; The password you set when running the Docker container
        ```
    *   **Important:**
        *   Update `SERVER` if your SQL Server is not running on `localhost` or port `1433`. For Docker on Mac, `localhost` or `127.0.0.1` should work when connecting from the host.
        *   Update `DATABASE` to the name you used when restoring AdventureWorks (e.g., `AdventureWorksLT2019`).
        *   Update `UID` to your SQL Server username (e.g., `SA`).
        *   Update `PWD` with the actual password you set for the SQL Server user.

## Running the Application

*(Please add instructions here on how to run the main part of your application, if applicable. For example, `python main.py`)*

Currently, the primary way to verify functionality is by running tests.

## Running Tests

This project uses `pytest` for testing.

1.  Ensure your SQL Server Docker container is running and `config/config.ini` is correctly configured.
2.  From the root directory of the project, run:
    ```bash
    pytest
    ```
    You should see output indicating whether the tests passed or failed. The `test_connection.py` specifically checks the database connection.

## Database Connection Details

*   This application connects to a SQL Server database.
*   The connection parameters are managed in `config/config.ini`.
*   The Python library `pyodbc` is used for the database connection (see `db/connection.py`).

## Troubleshooting

*   **ODBC Driver Issues**:
    *   "Can't open lib 'ODBC Driver 17 for SQL Server' : file not found": Ensure the driver is installed correctly and the name in `config.ini` matches an installed driver. You can list installed ODBC drivers using `odbcinst -q -d`.
*   **Connection Timeouts**:
    *   Ensure your Docker SQL Server container is running.
    *   Verify the `SERVER` and port in `config.ini` are correct and that SQL Server is accessible (e.g., no firewall blocking).
*   **Login Failed for User**:
    *   Double-check `UID` and `PWD` in `config.ini`.
    *   Ensure the user has permissions to access the specified `DATABASE`.
    *   If using `SA`, ensure the password matches the `MSSQL_SA_PASSWORD` you set for the Docker container.

---

*This README was last updated on YYYY-MM-DD.*
*(Consider adding a section on Project Structure if it's complex, or Contribution Guidelines if it's an open project).*
