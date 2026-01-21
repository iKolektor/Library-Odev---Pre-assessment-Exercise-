# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    ###################
    # Default methods #
    ###################
    name = fields.Char(string="Name", required=True)

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    _sql_constraints = [
        ("name_unique", "unique(name)", "The category name must be unique.")
    ]

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
