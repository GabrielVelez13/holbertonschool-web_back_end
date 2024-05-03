# Pagination

This README provides an overview of pagination and covers the following learning objectives:

1. How to paginate a dataset with simple page and page_size parameters
2. How to paginate a dataset with hypermedia metadata
3. How to paginate in a deletion-resilient manner

## 1. How to paginate a dataset with simple page and page_size parameters

Pagination is a technique used to divide a large dataset into smaller, more manageable chunks called pages. One common approach is to use simple page and page_size parameters to control the pagination.

To paginate a dataset with simple page and page_size parameters, follow these steps:

1. Determine the total number of items in the dataset.
2. Calculate the total number of pages based on the page_size.
3. Retrieve the desired page by specifying the page number and page_size in the API request.
4. Return the paginated results to the client.

Example API request: `GET /api/data?page=2&page_size=10`

## 2. How to paginate a dataset with hypermedia metadata

Another approach to pagination is to use hypermedia metadata, which provides additional information about the pagination in the API response.

To paginate a dataset with hypermedia metadata, follow these steps:

1. Determine the total number of items in the dataset.
2. Calculate the total number of pages based on the page_size.
3. Retrieve the desired page by specifying the page number and page_size in the API request.
4. Include hypermedia metadata in the API response, such as links to the first, previous, next, and last pages.
5. Return the paginated results along with the hypermedia metadata to the client.

Example API response:
```JSON
{
    "data": [
        {
            "id": 1,
            "name": "John Doe"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        },
        {
            "id": 3,
            "name": "Alice Johnson"
        }
    ],
    "pagination": {
        "total_items": 100,
        "total_pages": 10,
        "current_page": 2,
        "page_size": 10,
        "links": {
            "first": "/api/data?page=1&page_size=10",
            "previous": "/api/data?page=1&page_size=10",
            "next": "/api/data?page=3&page_size=10",
            "last": "/api/data?page=10&page_size=10"
        }
    }
}
```