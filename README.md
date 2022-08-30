# Importing_CSV_into_Django

The code for uploading files is written as an example for the project API_YAMDB (https://github.com/AMRedichkina/API_YaMDb_).


The project provides a management command **load_data** to upload files in the **csv** format to the database via Django ORM.


To upload data to the database, you need to group files with the following names in the directory:

- category.csv 
- genre.csv 
- titles.csv 
- users.csv 
- genre_title.csv 
- review.csv 
- comments.csv 

## Requirements for file fields
Below you will find the minimum set of fields required in each file for the download to be successful.

#### * **category.csv** 
| *id*        | *name*          | *slug* |
|:----------:|:-------------:| :-----:|
| 1      | Film | film |
| 2      | Book | book |

#### * **genre.csv** 
| *id*        | *name*           | *slug* |
| :-------------: |:-------------:|:-----:|
| 1      | Drama | drama |
| 2      | Comedy | comedy |

#### * **titles.csv** 
| *id*  | *name*          | *year* | *category_id* | *description* |
|:---:|:-------------:|:-----:|:-----:|:-----:|
| 1   | A ball of bread | 1873 | 2 | A ball of bread |
| 2   | Back to the Future | 1985 | 1 |  |

#### * **users.csv** 
| *id*  | *username*          | *email* | *role* | *first_name* | *last_name* | 
|:---:|:-------------:|:-----:|:-----:|:-----:|:-------|
| 100   | spider | sppitpark@aveng.com | user | Piter | Parker  |
| 101   | VolanDeMort | slizerin@hogwarts.com | admin |  |     |

#### * **genre_title.csv**
| *id*        | *title_id*          | *genre_id* |
|:----------:|:-------------:| :-----:|
| 1      | 1 | 1 |
| 2      | 2 | 1 |

#### * **review.csv** 
| *id*  | *title_id*          | *text* | *author_id* | *score* | *pub_date* | 
|:---:|:-------------:|:-----:|:-----:|:-----:|:-------:|
| 1   | 1 | This was amazing | 100| 10 | 2019-09-24T21:08:21.567Z  |
| 2   | 1 | Avada Kedavra | 101 | 1 |  2019-09-24T21:08:21.567Z   |

#### * **comments.csv** 
| *id*  | *review_id*          | *text* | *author_id* | *pub_date* | 
|:---:|:-------------:|:-----:|:-----:|:-------:|
| 1   | 1 | Bullshit | 70 |2019-09-24T21:08:21.567Z  |
| 2   | 6 | Lumus | 60 |2019-09-24T21:08:21.567Z   |

## Loading data

You can upload data using the command

```shell
python3 manage.py load_data
```
