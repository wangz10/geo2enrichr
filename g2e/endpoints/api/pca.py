"""Performs PCA.
"""

from flask import Blueprint, render_template, request, jsonify
import json

from g2e.db import dataaccess
from g2e.core.pca import pca
from g2e.config import Config

pca_api = Blueprint('pca', __name__, url_prefix=Config.BASE_URL + '/pca')


@pca_api.route('/<extraction_id>', methods=['GET'])
def perform_soft_file_pca(extraction_id):
    """Performs PCA on a SOFT file, referenced by extraction_id.
    """
    gene_signature = dataaccess.fetch_gene_signature(extraction_id)
    if gene_signature:
        pca_data = pca.from_soft_file(gene_signature.soft_file)
        pca_json = json.dumps(pca_data)
        return render_template('pca.html',
                               pca_data=pca_json,
                               results_url=Config.BASE_RESULTS_URL,
                               extraction_id=gene_signature.extraction_id)