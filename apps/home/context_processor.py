from apps.company.models import Profile
def settings(request):
    #profile = Profile.objects.filter(id=1).values('CompanyName','Slogan')
    company_profile=Profile.objects.all()
    #Tables.objects.filter(DataBase_id=self.kwargs['pk'],DetailOf__DataSizeMB__isnull=False).values('id','Schema','Name','Status','CreateDate','TableCategory__Category','DetailOf__DataSizeMB').order_by('
    return {'settings': company_profile}