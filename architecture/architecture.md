# RetailX Enterprise ETL Pipeline Architecture

```text
               +-------------------------+
               |   Data Generator        |
               |      (Python)           |
               +-----------+-------------+
                           |
                           v
                  CSV Files (Raw Data)
                           |
                           v
                Extract → Transform
                           |
                           v
                      Validate Data
                           |
                           v
                     Load to PostgreSQL
                           |
                           v
                   SQL Analytics Views
                           |
                           v
                 Power BI Dashboard
```
