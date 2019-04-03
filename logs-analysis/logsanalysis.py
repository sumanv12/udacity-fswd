#!/usr/bin/env python
"""
Udacity Full Stack Web Developer Nanodegree - Jan 2019, IND.
Project 1 : Logs Analysis

"""
import psycopg2
import datetime


def popular_articles(cursor):
    """Query and print out the 3 most popular articles.

    Parameters
    ----------
    cursor: psycopg2 PostgreSQL database cursor object.

    """
    query = '''
            SELECT title, count(*) as num
            FROM   log, articles
            WHERE  concat('/article/', articles.slug) = log.path
            GROUP BY title
            ORDER BY num DESC limit 3;

            '''
    cursor.execute(query)
    results = cursor.fetchall()

    print('The three most popular articles of the news dataset are:')
    for title, views in results:
        print('{:<40} -- {:>10} views'.format(title, views))

    print('')

    return


def popular_authors(cursor):
    """Query and print out the most popular authors.

    Parameters
    ----------
    cursor: psycopg2 PostgreSQL database cursor object.

    """
    query = '''
            SELECT name, count(*) as num
            FROM log, articles, authors
            WHERE concat('/article/', articles.slug) = log.path and
                  authors.id = articles.author
            GROUP BY name
            ORDER BY num desc;

            '''
    cursor.execute(query)
    results = cursor.fetchall()

    print('The most popular authors of the news dataset are:')
    for author, views in results:
        print('{:<40} -- {:>10} views'.format(author, views))

    print('')

    return


def error_days(cursor):
    """Query and print out days where the error rate is greater than 1%.

    Parameters
    ----------
    cursor: psycopg2 PostgreSQL database cursor object.

    """
    query = '''
            SELECT time::date,
                   (100*error::decimal / total)::decimal(3, 2) as perc_err
            FROM   errorlog
            WHERE  error > total::decimal * 0.01

            '''
    cursor.execute(query)
    results = cursor.fetchall()

    print('The days where error rate is greater than 1% are:')
    for day, err in results:
        print('{:<40} -- {:10.2f} % err'.format(
            day.strftime('%B %d %Y'), err))

    print('')

    return


def main():
    """Connects to the news database, and executes required queries."""
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
    except (DatabaseError):
        print("Failed to connect to the PostgreSQL database.")
        return

    print('Solutions to the Logs Analysis project.')
    print('Udacity Full Stack Web Developer Nanodegree 2019.\n')

    popular_articles(cursor)
    popular_authors(cursor)
    error_days(cursor)

    db.close()


if __name__ == "__main__":
    main()
