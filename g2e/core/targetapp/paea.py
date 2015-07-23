"""Handles the Principle Angle Enrichment Analysis (PAEA) API. For more
information, see: http://amp.pharm.mssm.edu/PAEA/.

__authors__ = "Gregory Gundersen, Zichen Wang"
__contact__ = "avi.maayan@mssm.edu"
"""


import json
import requests


POST_URL = 'http://amp.pharm.mssm.edu/Enrichr/addList'
GET_URL  = 'http://amp.pharm.mssm.edu/PAEA?id='


def get_link(genes, description):
    """Returns a shareable link to PAEA data.
    """
    print 'Calculating principle angle enrichment analysis'

    gene_list = ''
    for gene, coeff in genes:
        gene_list += '%s,%s\n' % (gene, coeff)
    
    payload = {
        'list': gene_list,
        'inputMethod': 'PAEA',
        'description': description
    }
    resp = requests.post(POST_URL, files=payload)

    if resp.status_code == 200:
        link = GET_URL + str(json.loads(resp.text)['userListId'])
        print 'Link to PAEA: ' + link
        return link
    else:
        print 'Error with PAEA'
        return None