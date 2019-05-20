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

from .namespaces import STYLENS
from .element import Element


def StyleElement(**args):
    e = Element(**args)
    if args.get('check_grammar', True) == True:
        if 'displayname' not in args:
            e.setAttrNS(STYLENS,'display-name', args.get('name'))
    return e

# Autogenerated


def BackgroundImage(**args):
    return Element(qname=(STYLENS,'background-image'), **args)


def ChartProperties(**args):
    return Element(qname=(STYLENS,'chart-properties'), **args)


def Column(**args):
    return Element(qname=(STYLENS,'column'), **args)


def ColumnSep(**args):
    return Element(qname=(STYLENS,'column-sep'), **args)


def Columns(**args):
    return Element(qname=(STYLENS,'columns'), **args)


def DefaultStyle(**args):
    return Element(qname=(STYLENS,'default-style'), **args)


def DrawingPageProperties(**args):
    return Element(qname=(STYLENS,'drawing-page-properties'), **args)


def DropCap(**args):
    return Element(qname=(STYLENS,'drop-cap'), **args)


def FontFace(**args):
    return Element(qname=(STYLENS,'font-face'), **args)


def Footer(**args):
    return Element(qname=(STYLENS,'footer'), **args)


def FooterLeft(**args):
    return Element(qname=(STYLENS,'footer-left'), **args)


def FooterStyle(**args):
    return Element(qname=(STYLENS,'footer-style'), **args)


def FootnoteSep(**args):
    return Element(qname=(STYLENS,'footnote-sep'), **args)


def GraphicProperties(**args):
    return Element(qname=(STYLENS,'graphic-properties'), **args)


def HandoutMaster(**args):
    return Element(qname=(STYLENS,'handout-master'), **args)


def Header(**args):
    return Element(qname=(STYLENS,'header'), **args)


def HeaderFooterProperties(**args):
    return Element(qname=(STYLENS,'header-footer-properties'), **args)


def HeaderLeft(**args):
    return Element(qname=(STYLENS,'header-left'), **args)


def HeaderStyle(**args):
    return Element(qname=(STYLENS,'header-style'), **args)


def ListLevelProperties(**args):
    return Element(qname=(STYLENS,'list-level-properties'), **args)


def Map(**args):
    return Element(qname=(STYLENS,'map'), **args)


def MasterPage(**args):
    return StyleElement(qname=(STYLENS,'master-page'), **args)


def PageLayout(**args):
    return Element(qname=(STYLENS,'page-layout'), **args)


def PageLayoutProperties(**args):
    return Element(qname=(STYLENS,'page-layout-properties'), **args)


def ParagraphProperties(**args):
    return Element(qname=(STYLENS,'paragraph-properties'), **args)


def PresentationPageLayout(**args):
    return StyleElement(qname=(STYLENS,'presentation-page-layout'), **args)


def RegionCenter(**args):
    return Element(qname=(STYLENS,'region-center'), **args)


def RegionLeft(**args):
    return Element(qname=(STYLENS,'region-left'), **args)


def RegionRight(**args):
    return Element(qname=(STYLENS,'region-right'), **args)


def RubyProperties(**args):
    return Element(qname=(STYLENS,'ruby-properties'), **args)


def SectionProperties(**args):
    return Element(qname=(STYLENS,'section-properties'), **args)


def Style(**args):
    return StyleElement(qname=(STYLENS,'style'), **args)


def TabStop(**args):
    return Element(qname=(STYLENS,'tab-stop'), **args)


def TabStops(**args):
    return Element(qname=(STYLENS,'tab-stops'), **args)


def TableCellProperties(**args):
    return Element(qname=(STYLENS,'table-cell-properties'), **args)


def TableColumnProperties(**args):
    return Element(qname=(STYLENS,'table-column-properties'), **args)


def TableProperties(**args):
    return Element(qname=(STYLENS,'table-properties'), **args)


def TableRowProperties(**args):
    return Element(qname=(STYLENS,'table-row-properties'), **args)


def TextProperties(**args):
    return Element(qname=(STYLENS,'text-properties'), **args)
