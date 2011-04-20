from haystack.indexes import *
from haystack import site
from school.models import School, Member

class MemberIndex(SearchIndex):
    text = CharField(document=True, use_template=True, template_name='indexes/member_text.txt')
    gpa = FloatField(model_attr="gpa", null=True)
    school = CharField(faceted=True, model_attr="school__name")
    boost = FloatField()

    def get_queryset(self):
        return Member.objects.all()
        
    def prepare_boost(self, object):
        boost = 1.0
        if object.id == 45:
            boost *= 5
        return boost

class SchoolIndex(SearchIndex):
    text

site.register(Member, MemberIndex)
