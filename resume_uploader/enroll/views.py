from django.shortcuts import render

# Create your views here.
from .forms import ResumeForm
from .models import Resume
from django.views import View

class Resumeview(View):
    def get(self,request):
        fm=ResumeForm()
        candidates=Resume.objects.all()
        return render(request,'enroll/home.html',{'form':fm,'candidates':candidates})
    
    def post(self, request):
        if request.method=='POST':
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'enroll/home.html', {'form': form})

class CandidateView(View):
    def get(self,request,pk):
        can=Resume.objects.get(id=pk)
        return render(request,'enroll/candidate.html',{'can':can})

"""def resumeview(request):
    context='my website'
    return render(request,'enroll/home.html',{'fm':context})"""