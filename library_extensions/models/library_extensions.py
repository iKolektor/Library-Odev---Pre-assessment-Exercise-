# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryExtensions(models.Model):
    _inherit = "library.book"

    # Added a new author_id field - Task 2: Add an author field to the book model
    author_id = fields.Many2one("res.partner", string="Author", required=True)
    category_ids = fields.Many2many("library.book.category", string="Category")