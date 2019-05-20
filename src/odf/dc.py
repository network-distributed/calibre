# -*- coding: utf-8 -*-
# Copyright (C) 2006-2007 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#

from .namespaces import DCNS
from .element import Element

# Autogenerated


def Creator(**args):
    return Element(qname=(DCNS,'creator'), **args)


def Date(**args):
    return Element(qname=(DCNS,'date'), **args)


def Description(**args):
    return Element(qname=(DCNS,'description'), **args)


def Language(**args):
    return Element(qname=(DCNS,'language'), **args)


def Subject(**args):
    return Element(qname=(DCNS,'subject'), **args)


def Title(**args):
    return Element(qname=(DCNS,'title'), **args)

# The following complete the Dublin Core elements, but there is no
# guarantee a compliant implementation of OpenDocument will preserve
# these elements

# def Contributor(**args):
#    return Element(qname = (DCNS,'contributor'), **args)

# def Coverage(**args):
#    return Element(qname = (DCNS,'coverage'), **args)

# def Format(**args):
#    return Element(qname = (DCNS,'format'), **args)

# def Identifier(**args):
#    return Element(qname = (DCNS,'identifier'), **args)

# def Publisher(**args):
#    return Element(qname = (DCNS,'publisher'), **args)

# def Relation(**args):
#    return Element(qname = (DCNS,'relation'), **args)

# def Rights(**args):
#    return Element(qname = (DCNS,'rights'), **args)

# def Source(**args):
#    return Element(qname = (DCNS,'source'), **args)

# def Type(**args):
#    return Element(qname = (DCNS,'type'), **args)
