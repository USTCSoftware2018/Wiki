# This is an extension for Markdown-py to adjust the output format

from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


FIRST = True
COUNT = 0
TOP = None
HEADINGS = []


def filter(s):
    return s.replace('*', '')


class H1Block(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('# ')

    def run(self, parent, blocks):
        global TOP

        heading = blocks.pop(0)

        h1 = etree.SubElement(parent, 'h1')
        h1.text = heading[2:]

        TOP = filter(h1.text)


class H2Block(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('## ')

    def run(self, parent, blocks):
        global FIRST, COUNT, HEADINGS

        heading = blocks.pop(0)

        if FIRST:
            FIRST = False
        else:
            divider = etree.SubElement(parent, 'div')
            divider.set('class', 'divider')

        h2 = etree.SubElement(parent, 'h2')
        h2.text = heading[3:]

        COUNT = COUNT + 1
        h2.set('id', "header{}".format(COUNT))

        HEADINGS.append((filter(h2.text), 'header%d' % COUNT))


class H3Block(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('### ')

    def run(self, parent, blocks):
        global FIRST

        heading = blocks.pop(0)

        if FIRST:
            FIRST = False
        else:
            divider = etree.SubElement(parent, 'div')
            divider.set('class', 'divider')

        h3 = etree.SubElement(parent, 'h3')
        h3.text = heading[4:]


class Menu(Treeprocessor):
    def run(self, root):
        global HEADINGS, TOP

        grid = etree.Element('div')
        grid.set('class', 'ui grid')

        # Left
        c1 = etree.SubElement(grid, 'div')
        c1.set('class', 'one wide column')

        c2 = etree.SubElement(grid, 'div')
        c2.set('class', 'three wide column')

        c3 = etree.SubElement(c2, 'div')
        c3.set('class', "ui secondary vertical pointing menu")
        c3.set('id', 'leftnav')
        c3.set('style', "height: 100%;padding-top: 100px;width: 90%;")

        header_item = etree.SubElement(c3, 'div')
        header_item.set('class', 'header')
        header_item.text = filter(TOP)

        menu = etree.SubElement(c3, 'div')
        menu.set('class', 'menu')
        for heading in HEADINGS:
            a = etree.SubElement(menu, 'a')
            a.set('class', 'item leftnav-item')
            a.set("href", "#%s" % heading[1])
            a.text = heading[0]

        # Right
        right = etree.SubElement(grid, 'div')
        right.set('class', 'twelve wide column')
        container = etree.SubElement(right, 'div')
        container.set('class', 'inside-container')
        container.set('style', "height: 100%;padding-top: 100px;")
        container.append(root)

        # Toplevel
        toplevel = etree.Element('div')
        toplevel.append(grid)

        return toplevel


class GenAdjustExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors.add(
            'h3',
            H3Block(md.parser),
            '<indent'
        )
        md.parser.blockprocessors.add(
            'h2',
            H2Block(md.parser),
            '<indent'
        )
        md.parser.blockprocessors.add(
            'h1',
            H1Block(md.parser),
            '<indent'
        )
        md.treeprocessors.add(
            'menu',
            Menu(md),
            '_end'
        )


def makeExtension(**kwargs):
    return GenAdjustExtension(**kwargs)
