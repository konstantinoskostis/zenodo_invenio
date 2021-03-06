# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from invenio.legacy.dbquery import run_sql

depends_on = ['invenio_release_1_1_0']

def info():
    return """Adds a new column to bibfmt for knowing when a second pass
              is required on the cached template"""

def do_upgrade():
    create_statement = run_sql('SHOW CREATE TABLE bibfmt')[0][1]
    if 'needs_2nd_pass' not in create_statement:
        run_sql("ALTER TABLE bibfmt ADD COLUMN needs_2nd_pass TINYINT(1) DEFAULT 0")

def estimate():
    """  Estimate running time of upgrade in seconds (optional). """
    count_rows = run_sql("SELECT COUNT(*) FROM bibfmt")[0][0]
    return count_rows / 40
