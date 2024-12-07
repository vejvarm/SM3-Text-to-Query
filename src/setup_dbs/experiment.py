import requests
import json
from pathlib import Path
from typing import Optional, Dict, Union
import logging


class GraphDBClient:
    def __init__(self, server_url: str, repository_name: str):
        """
        Initialize GraphDB REST client

        Args:
            server_url: Base URL of GraphDB server (e.g., 'http://localhost:7200')
            repository_name: Name of the repository to work with
        """
        self.server_url = server_url.rstrip('/')
        self.repository_name = repository_name
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def create_repository(self, config_template: Optional[Dict] = None) -> bool:
        """
        Create a new repository using the GraphDB REST API

        Args:
            config_template: Optional repository configuration. If None, uses default.

        Returns:
            bool: True if repository was created successfully
        """
        if config_template is None:
            config_template = {
                "id": self.repository_name,
                "title": "",
                "type": "free",
                "ruleset": "owl-horst-optimized",
                "repositories": [{
                    "id": self.repository_name,
                    "location": "",
                    "params": {
                        "entityIndexSize": "10000000",
                        "entityIdSize": "32",
                        "throwOnValidationError": "false",
                        "validateRepositories": "true",
                    },
                    "title": "",
                    "type": "graphdb:FreeSailRepository"
                }]
            }

        url = f"{self.server_url}/rest/repositories"

        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=config_template
            )
            response.raise_for_status()
            self.logger.info(f"Repository '{self.repository_name}' created successfully")
            return True

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to create repository: {str(e)}")
            return False

    def upload_ttl_file(self, file_path: Union[str, Path],
                        context: Optional[str] = None,
                        batch_size: int = 100000) -> bool:
        """
        Upload a TTL file to the repository

        Args:
            file_path: Path to the TTL file
            context: Optional named graph URI
            batch_size: Number of statements to upload in each batch

        Returns:
            bool: True if file was uploaded successfully
        """
        file_path = Path(file_path)
        if not file_path.exists():
            self.logger.error(f"File not found: {file_path}")
            return False

        url = f"{self.server_url}/repositories/{self.repository_name}/statements"

        # Add context to URL if provided
        if context:
            url += f"?context=<{context}>"

        headers = {
            'Content-Type': 'text/turtle',
        }

        try:
            with open(file_path, 'rb') as f:
                response = requests.post(
                    url,
                    headers=headers,
                    data=f,
                )
                response.raise_for_status()
                self.logger.info(f"File '{file_path}' uploaded successfully")
                return True

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to upload file: {str(e)}")
            return False

    def check_repository_exists(self) -> bool:
        """Check if the repository exists"""
        url = f"{self.server_url}/rest/repositories/{self.repository_name}/size"
        try:
            response = requests.get(url, headers=self.headers)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def delete_repository(self) -> bool:
        """Delete the repository"""
        url = f"{self.server_url}/rest/repositories/{self.repository_name}"
        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            self.logger.info(f"Repository '{self.repository_name}' deleted successfully")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to delete repository: {str(e)}")
            return False


# Example usage
def main():
    # Initialize client
    client = GraphDBClient(
        server_url='http://localhost:7200',
        repository_name='sm3_t2'
    )

    # Create repository if it doesn't exist
    if not client.check_repository_exists():
        client.create_repository()

    # Upload TTL files
    ttl_files = [
        '/Users/workstation/Documents/GitHub/SM3-Text-to-Query-fork/src/setup_dbs/graphdb/synthea-rdf-converter-fork/temporary_ttl_files/allergy.ttl'
    ]

    for ttl_file in ttl_files:
        success = client.upload_ttl_file(
            file_path=ttl_file,
            context=f"http://example.org/graphs/{ttl_file}"
        )
        if not success:
            print(f"Failed to upload {ttl_file}")


if __name__ == "__main__":
    main()