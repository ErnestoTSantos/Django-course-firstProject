from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):

    def test_make_pagination_range_returns_a_pagination_range(self):

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

    def test_pagination_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501

        # Current page = 1 - amount page = 2 - middle page = 4
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

        # Current page = 2 - amount page = 2 - middle page = 4
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

        # Current page = 3 - amount page = 2 - middle page = 3
        # Here range should change
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=3,
        )['pagination']
        self.assertEqual([1, 2, 3, 4, 5], pagination)

        # Current page = 4 - amount page = 2 - middle page = 4
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=4,
        )['pagination']
        self.assertEqual([2, 3, 4, 5, 6], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=5,
        )['pagination']
        self.assertEqual([3, 4, 5, 6, 7], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=6,
        )['pagination']
        self.assertEqual([4, 5, 6, 7, 8], pagination)

    def test_pagination_make_sure_middle_ranges_are_correct(self):  # noqa: E501

        # Current page = 10 - amount_pages = 5 - middle page 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=10,
        )['pagination']
        self.assertEqual([8, 9, 10, 11, 12], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=11,
        )['pagination']
        self.assertEqual([9, 10, 11, 12, 13], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=18,
        )['pagination']
        self.assertEqual([16, 17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=19,
        )['pagination']
        self.assertEqual([16, 17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            amount_pages=5,
            current_page=20,
        )['pagination']
        self.assertEqual([16, 17, 18, 19, 20], pagination)
