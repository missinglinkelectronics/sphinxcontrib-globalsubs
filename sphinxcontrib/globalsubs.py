# -*- coding: utf-8 -*-
"""
    sphinxcontrib.globalsubs
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Adds support for global substitutions to conf.py.

    :copyright: Copyright 2018-2023 by Stefan Wiehler
                <sphinx_contribute@missinglinkelectronics.com>.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.utils import new_document

from sphinx.transforms import SphinxTransform
from sphinx.util import logging
from sphinx.util.docutils import LoggingReporter
from sphinx import version_info

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA


logger = logging.getLogger(__name__)


class GlobalSubstitutions(SphinxTransform):
    # run after DefaultSubstitutions and before Substitutions
    default_priority = 211

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        if version_info[0] >= 9:
            self.parser = self.app.registry.create_source_parser('rst', env=self.document.settings.env, config=self.document.settings.env.config)
        else:
            self.parser = self.app.registry.create_source_parser(self.app, 'rst')

    def apply(self):
        # type: () -> None
        config = self.document.settings.env.config
        settings, source = self.document.settings, self.document['source']
        global_substitutions = config['global_substitutions']
        to_handle = (set(global_substitutions.keys())
                - set(self.document.substitution_defs))

        for ref in self.document.findall(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = global_substitutions[refname]

                doc = new_document(source, settings)
                doc.reporter = LoggingReporter.from_reporter(doc.reporter)
                self.parser.parse(text, doc)

                substitution = doc.next_node()
                # Remove encapsulating paragraph
                if isinstance(substitution, nodes.paragraph):
                    substitution = substitution.next_node()
                # Deal with possible parse failure
                if substitution is None:
                    continue
                ref.replace_self(substitution)


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_config_value('global_substitutions', {}, None)
    app.add_transform(GlobalSubstitutions)

    return {'version': '0.1.0', 'parallel_read_safe': True}
