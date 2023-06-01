# DBEXPORT

## Notes:
    - url to the db should start with postresql://
    - query string should be wrapped in executable object text() from sqlalchemy package
    ```
    db.execute(text("SELECT count(id) FROM reviews"))
    ```