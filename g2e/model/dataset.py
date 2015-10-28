"""Parent class for GEO record subclasses: GeoDataset (GDS), GeoProfile (GSE),
and GeoPlatform (GPL).

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


from g2e import db


class Dataset(db.Model):

    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    file_path = db.Column(db.Text, nullable=False)
    record_type = db.Column(db.String(32), nullable=False)
    summary = db.Column(db.Text)
    organism = db.Column(db.String(255))

    __mapper_args__ = {'polymorphic_on': record_type}

    # Back references.
    soft_files = db.relationship('SoftFile', backref=db.backref('dataset', order_by=id))

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.file_path = kwargs['file_path']
        if 'summary' in kwargs:
            self.summary = kwargs['summary']
        if 'organism' in kwargs:
            self.organism = kwargs['organism']

    def __repr__(self):
        return '<Dataset %r>' % self.id
