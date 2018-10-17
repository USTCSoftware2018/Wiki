# This is an extension for Markdown-py to adjust the output format

from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.util import etree


FIRST = True


class H2Block(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('## ')

    def run(self, parent, blocks):
        global FIRST

        heading = blocks.pop(0)

        if FIRST:
            FIRST = False
        else:
            divider = etree.SubElement(parent, 'div')
            divider.set('class', 'divider')

        h2 = etree.SubElement(parent, 'h2')
        h2.text = heading[3:]


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


class GenAdjustExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors.add(
            'gen_adjust',
            H3Block(md.parser),
            '<indent'
        )
        md.parser.blockprocessors.add(
            'gen_adjust',
            H2Block(md.parser),
            '<indent'
        )


def makeExtension(**kwargs):
    return GenAdjustExtension(**kwargs)
