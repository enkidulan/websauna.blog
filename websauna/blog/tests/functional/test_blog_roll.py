"""Functional tests."""

from sqlalchemy.orm.session import Session
from splinter.driver import DriverAPI


def test_empty_blog(web_server: str, browser: DriverAPI, dbsession: Session):
    """We can render empty blog."""

    # Direct Splinter browser to the website
    b = browser
    b.visit(web_server + "/blog/")

    # After login we see a profile link to our profile
    assert b.is_element_visible_by_css("#blog-no-posts")


def test_no_unpublished_in_blog_roll(web_server: str, browser: DriverAPI, dbsession: Session, unpublished_post_id):
    """Visitors should not see unpublished posts in blog roll."""

    # Direct Splinter browser to the website
    b = browser
    b.visit(web_server + "/blog/")

    # After login we see a profile link to our profile
    assert b.is_element_visible_by_css("#blog-no-posts")


def test_published_excerpt(web_server: str, browser: DriverAPI, dbsession: Session, published_post_id):
    """When posts are published they become visible in blog roll."""

    # Direct Splinter browser to the website
    b = browser
    b.visit(web_server + "/blog/")

    # After login we see a profile link to our profile
    assert b.is_element_visible_by_css(".excerpt")