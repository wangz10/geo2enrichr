"""Interface for db module.
"""

from db import \
    save_gene_signature, \
    get_gene_signature, \
    get_geo_dataset, \
    get_num_gene_signatures, \
    get_soft_files_by_accession

from utils import \
    session_scope, \
    get_or_create