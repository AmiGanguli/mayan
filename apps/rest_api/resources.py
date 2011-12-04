from django.core.urlresolvers import reverse

from djangorestframework.resources import ModelResource

from documents.models import Document
from converter.exceptions import UnknownFileFormat, UnkownConvertError


class DocumentResourceSimple(ModelResource):
    model = Document
    fields = ('url', 'pk', 'document_type', 'uuid', 'date_added', 'description', 'tags', 'comments', 'expensive_methods', 'versions')
   
    def versions(self, instance):
        return [
            {
                'version': version.get_formated_version(),
                'major': version.major,
                'minor': version.minor,
                'micro': version.micro,
                'release_level': version.release_level,
                'serial': version.serial,
                'timestamp': version.timestamp,
                'comment': version.comment,
                'mimetype': version.mimetype,
                'encoding': version.encoding,
                'filename': version.filename,
                'checksum': version.checksum,
                'download': reverse('document_version_download', args=[version.pk]),
                'stored_filename': version.file.name,
                # TODO: Add transformations
                'pages': [
                    {
                        'content': page.content,
                        'page_label': page.page_label,
                        'page_number': page.page_number,
                    }
                    for page in version.pages.all()
                ]
                
            }
            for version in instance.versions.all()
        ]
            
        '''
        return [
            {
                'version': 1,
                'mimetype': instance.file_mimetype,
                'encoding': instance.file_mime_encoding,
                'filename': instance.filename,
                'date_updated': instance.date_updated,
                'checksum': instance.checksum,
                'size': instance.size,
                'exists': instance.exists(),
                'pages': [
                    {
                        'page_numer': page.page_number,
                        'page_label': page.page_label,
                        'is_zoomable': reverse('documents-expensive-is_zoomable', args=[instance.pk, page.page_number]),
                        
                        #'content':
                    }
                    for page in instance.documentpage_set.all()
                ]
            }
        ]
        '''
    def expensive_methods(self, instance):
        return []
