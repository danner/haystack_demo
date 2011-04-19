from haystack.indexes import *
from haystack import site
from school.models import School, Member

class MemberIndex(SearchIndex):
    text = CharField(document=True, use_template=True, template_name='indexes/member_text.txt')
    gpa = FloatField(model_attr="gpa", null=True)
    school = CharField(faceted=True, model_attr="school__name")

    def get_queryset(self):
        return Member.objects.all()

site.register(Member, MemberIndex)
