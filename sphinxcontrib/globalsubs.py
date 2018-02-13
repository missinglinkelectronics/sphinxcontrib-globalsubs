# -*- coding: utf-8 -*-
"""
    sphinxcontrib.globalsubs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Adds global substitutions to conf.py.

    :copyright: Copyright 2018 by Stefan Wiehler
                <stefan.wiehler@missinglinkelectronics.com>.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import Parser as RSTParser
from docutils.utils import new_document

from sphinx.transforms import SphinxTransform
from sphinx.util import logging

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA

logger = logging.getLogger(__name__)


class GlobalSubstitutions(SphinxTransform):
    # run after DefaultSubstitutions and before Substitutions
    default_priority = 211

    def apply(self):
        # type: () -> None
        config = self.document.settings.env.config
        settings, source = self.document.settings, self.document['source']
        global_substitutions = config['global_substitutions']
        to_handle = set(global_substitutions.keys()) - set(self.document.substitution_defs)
        for ref in self.document.traverse(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = global_substitutions[refname]

                doc = new_document(source, settings)
                parser = RSTParser()
                parser.parse(text, doc)

                substitution = doc.next_node().next_node()
                ref.replace_self(substitution)


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_config_value('global_substitutions', {}, None)
    app.add_transform(GlobalSubstitutions)
    return {'version': '0.9.0', 'parallel_read_safe': True}
