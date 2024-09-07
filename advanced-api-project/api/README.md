## API Endpoints

- **List Books**
  - **URL**: `/books/`
  - **Method**: `GET`
  - **Permissions**: Open to everyone

- **Create Book**
  - **URL**: `/books/`
  - **Method**: `POST`
  - **Permissions**: Open to everyone

- **Retrieve Book**
  - **URL**: `/books/<id>/`
  - **Method**: `GET`
  - **Permissions**: Authenticated users only

- **Update Book**
  - **URL**: `/books/<id>/`
  - **Method**: `PUT` or `PATCH`
  - **Permissions**: Authenticated users only

- **Delete Book**
  - **URL**: `/books/<id>/`
  - **Method**: `DELETE`
  - **Permissions**: Authenticated users only

  ## API Filtering, Searching, and Ordering

- **Filtering**: You can filter the book list by title, author, and publication year.
  - Example: `/api/books/?title=BookTitle&author=AuthorName&publication_year=2024`

- **Searching**: Use the `search` parameter to search across specified fields.
  - Example: `/api/books/?search=BookTitle`

- **Ordering**: Order the results by title or publication year. Prefix with `-` for descending order.
  - Example: `/api/books/?ordering=title`
  - Example: `/api/books/?ordering=-publication_year`



How to run the tests.
The structure of the tests.
Examples of test cases.
