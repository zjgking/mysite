from django import forms
from django.forms import ModelForm
from tableQuery.models import sw,fw




class QueryForm(forms.Form):

    rj45 = forms.IntegerField(required=False,min_value=0,initial=0,error_messages={'required':'必须为正整数'})
    ge_sfp = forms.IntegerField(required=False,min_value=0,initial=0,error_messages={'required':'必须为正整数'})
    g10c = forms.IntegerField(required=False,min_value=0,initial=0)
    sfpp = forms.IntegerField(required=False,min_value=0,initial=0)
    g25 = forms.IntegerField(required=False,min_value=0,initial=0)
    qsfpp = forms.IntegerField(required=False,min_value=0,initial=0)
    cfp = forms.IntegerField(required=False,min_value=0,initial=0)
    slot = forms.IntegerField(required=False,min_value=0,initial=0) #业务插槽数量
    thp = forms.FloatField(required=False,min_value=0,initial=0.00) #吞吐性能，thp名字必须与html form中name一样
    fc =forms.FloatField(required=False,min_value=0,initial=0.00)   #ipv4转发速率
    ccs = forms.FloatField(required=False,min_value=0,initial=0.00) #Concurrent_Sessions
    nss = forms.IntegerField(required=False,min_value=0,initial=0)  #New_Sessions_Sec


    #Interface_Module_Slots = forms.IntegerField(required=False)
    #Processor_Module_Slots = forms.IntegerField(required=False)

    #def cleannone(self):
    #    cp = self.cleaned_data.get('cp',None)
    #    if cp is None:
    #        return self.initial.get('cp', 0)
    #    return cp
class swform(ModelForm):
    class swmeta:
        module = sw
        fields = "__all__"

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()